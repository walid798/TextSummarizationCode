import json
import re

def read_json(path):
    with open(path+'.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


if __name__ == '__main__':
    count = 3
    rootPath = ""
    filesList = ["Test_gemma-7b-it_prompt#"+str(count),"Test_Llama-2-7b_prompt#"+str(count),
            "Test_Llama-2-13b_prompt#"+str(count),"Test_Llama-2-70b_prompt#"+str(count),
            "Test_Mistral-7B-Instruct-v0.1_prompt#"+str(count),"Test_Mixtral-8x7B-Instruct-v0.1_prompt#"+str(count),]
    lenList = []
    for file in filesList:
        path = rootPath+file
        data = read_json(path=path)
        moldeLen = []
        for doc in data:
            gen = doc['generated']
            p = gen.strip()
            words = gen.split()
            wordCount = len(words)
            moldeLen.append(wordCount)
            #print(p)
            #print("==========")
           
        avgLen = sum(moldeLen) / len(moldeLen)
        lenList.append(round(avgLen,2))
    for item in lenList:
        print(item)



















