import json
import os
import time
from tqdm import tqdm
import math
import nltk
from nltk.tokenize import sent_tokenize

# Use NLTK for sentence tokenization.
def chunk_document(text, max_tokens=512):
    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = []
    current_length = 0

    for sentence in sentences:
        sentence_length = len(sentence.split())
        if current_length + sentence_length <= max_tokens:
            current_chunk.append(sentence)
            current_length += sentence_length
        else:
            chunks.append(' '.join(current_chunk))
            current_chunk = [sentence]
            current_length = sentence_length

    if current_chunk:
        chunks.append(' '.join(current_chunk))
    return chunks
def summarize_with_chunking(summarizer, text, max_tokens=512):

    # Ensure NLTK sentence tokenizer is downloaded.
    nltk.download('punkt')

    # Step 1: Chunk the document.
    chunks = chunk_document(text, max_tokens)
    
    # Step 2: Generate intermediate summaries for each chunk.
    intermediate_summaries = []
    for chunk in chunks:
        intermediate = summarizer.summarize(chunk)
        intermediate_summaries.append(intermediate)
    
    # Step 3: Combine intermediate summaries and generate final summary.
    combined_text = " ".join(intermediate_summaries)
    final_summary = summarizer.summarize(combined_text)
    return final_summary

def main():
    datasets = ["ArXivTestFull"]  # List of datasets to summarize. (Apply chunking for long documents)
    models = [ "llama2:7b-chat", "llama2:13b-chat", "gemma:7b-instruct", "llama2:70b-chat" , "mistral:7b-instruct-v0.1", "mixtral-8x7B-instruct-v0.1"]

    for dataset in datasets:
        input_file = f"{dataset}.json"
        
        for model in models:
            model_name = model.replace(":", "_")
            
            # Create a unique folder for each run.
            run_folder = f"{dataset}_summaries_{model_name}_{int(time.time())}"
            os.makedirs(run_folder, exist_ok=True)
            
            output_file = os.path.join(run_folder, "summaries.json")
            time_file = os.path.join(run_folder, "inference_times.txt")
            
            articles = read_json(input_file)
            summarizer = Summarizer(model_name=model) 
            
            # Write initial configuration details.
            with open(time_file, "w") as f:
                f.write(f"Model: {model}\n")
                f.write(f"Max tokens: {MAX_TOKENS}\n")
                f.write("Temperature: 0.1\n")
            
            results = []
            start_time = time.time()  # Start the overall timer
            
            for article in tqdm(articles, desc=f"Summarizing articles for {dataset} with {model_name}"):
                docID = article["docID"]
                text = article["text"]
                summary = article["summary"]
                
                # Start per-article timer.
                article_start_time = time.time()
                
                # Apply chunking strategy
                if dataset == "ArXivTestFull":
                    generated_summary = summarize_with_chunking(summarizer, text, max_tokens=512)
                else:
                    generated_summary = summarizer.summarize(text)
                
                article_end_time = time.time()
                inference_time = article_end_time - article_start_time
                
                with open(time_file, "a") as f:
                    f.write(f"Article {docID}: {inference_time:.2f} seconds\n")
                
                results.append({
                    "docID": docID,
                    "text": text,
                    "summary": summary,
                    "generated": generated_summary
                })
                write_json(results, output_file)
            
            end_time = time.time()  # End overall timer
            total_inference_time = end_time - start_time
            average_inference_time = total_inference_time / len(articles)
            
            with open(time_file, "a") as f:
                f.write(f"Total inference time: {total_inference_time:.2f} seconds\n")
                f.write(f"Average inference time per article: {average_inference_time:.2f} seconds\n")
            
            print(f"Summaries saved to {output_file}")
            print(f"Inference times saved to {time_file}")
            print(f"Total inference time: {total_inference_time:.2f} seconds")
            print(f"Average inference time per article: {average_inference_time:.2f} seconds")

if __name__ == "__main__":
    main()
