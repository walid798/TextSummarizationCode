import json
import re
#import nltk
#nltk.download('punkt')
#from nltk.tokenize import sent_tokenize
from collections import Counter
def read_json(path):
    with open(path+'.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data
def remove_until(text):

  try:
    start_index = text.index("summary:")
  except ValueError:
    return text
  return text[start_index+9:]
def remove_text_until_word(text, word):
    # Find the position of the word in the text
    word_position = text.find(word)
    
    # If the word is found, return the substring starting from the word
    if word_position != -1:
        return text[word_position+8:]
    else:
        # If the word is not found, return the original text
        return text
    
def remove_until1(text):

  try:
    start_index = text.index("abstract")
  except ValueError:
    return text
  return text[start_index+9:]

def remove_text(str):
    parts = str.split(":\n\n", 1)  # Split the string into two parts at the first occurrence of ":"
    if len(parts) > 1:
        return parts[0].strip()  # Take the second part and remove leading/trailing whitespace
    return str  # If ":" is not found, return the original string

def process_str(in_str):
    
    str = in_str.replace("*","")
    str = str.replace("summary:","")
    str = remove_text_until_word(str, "summary:")
    str = remove_text(str)
    str = remove_until(str)
    

    re.sub(r"\Sure(.*?):", "", str)
    #str3 = remove_until1(str2)
    return str

if __name__ == '__main__':
    count = 1
    rootPath = ""
    #"NewsRoomTestAbs_gemma-7b-it_prompt#"+str(count),
    filesList = ["dataset_gemma-7b-it_prompt#"+str(count),"dataset_Llama-2-7b_prompt#"+str(count),
            "dataset_Llama-2-13b_prompt#"+str(count),"dataset_Llama-2-70b_prompt#"+str(count),
            "dataset_Mistral-7B-Instruct-v0.1_prompt#"+str(count),"dataset_Mixtral-8x7B-Instruct-v0.1_prompt#"+str(count),]
    for file in filesList:
        path = rootPath+file
        data = read_json(path=path)
        for doc in data:
            gen = doc['generated']
            p = gen.strip()

            if p.startswith("**") or p.startswith("##") or p.startswith("H"):
               re.sub(r'^.*?\n', ' ', p)
            item1 = remove_text_until_word(p, "\n\n")
            item1 = process_str(item1).strip()
            item1 = remove_text(item1)
            
            item2 = item1.replace("\n","")
            
        filePath = ""+file+".json" 
        with open(filePath, 'w') as fout:
            json.dump(data , fout, indent=4)
        for item in data[0:10]:
            print(item['generated'])
            print("=========================")




















