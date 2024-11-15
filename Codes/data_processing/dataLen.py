import argparse
from datetime import timedelta
import json
from operator import itemgetter
from time import time
from os.path import join, exists
def read_json(path):
    with open(path+".json", encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data

def load_jsonl(data_path):
    data = []
    start = time()
    print("Start Loading Data ")
    with open(data_path) as f:
        for line in f:
            data.append(json.loads(line))
    
    print('finished in {}'.format(timedelta(seconds=time()-start)))
    return data
def remove_until1(text):

  try:
    start_index = text.index("title")
  except ValueError:
    return text
  return text[start_index:]
if __name__ == "__main__":
    data = load_jsonl("dev-stats.jsonl")
    devList = []
    for item in data:
       devItem = {"title":item['title'] , "text":item['text'] , "summary":item['summary']}
       devList.append(devItem)
    with open("devList.json", 'w') as fout:
            json.dump(devList, fout , indent=4)
    """count = 3
    dataLen = []
    #"CNNDMTest_gemma-7b-it_prompt#"+str(count),
    filesList = ["CNNDMTest_gemma-7b-it_prompt#"+str(count),"CNNDMTest_Llama-2-7b_prompt#"+str(count),
            "CNNDMTest_Llama-2-13b_prompt#"+str(count),"CNNDMTest_Llama-2-70b_prompt#"+str(count),
            "CNNDMTest_Mistral-7B-Instruct-v0.1_prompt#"+str(count),"CNNDMTest_Mixtral-8x7B-Instruct-v0.1_prompt#"+str(count),]
    
    for file in filesList:
        path = "Temp_0.1\\prompt#"+str(count)+"\\"+file
        data = read_json(path=path)
        dataLen = []
        for doc in data:
            text = doc['text']
            gen = doc['generated']
            summ = doc['summary']
            l = {"textLen":len(text),"genLen":len(gen),"sumLen":len(summ)}
            dataLen.append(l)
        with open("Temp_0.1\\prompt#"+str(count)+"\\len\\"+file+"Len.json", 'w') as fout:
            json.dump(dataLen, fout)
    print("Done")"""
            #print(doc['generated'])
            #print("-------------------------")




