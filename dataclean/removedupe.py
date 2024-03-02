# loop files in the folder, for each file, if the value of key "html" is less than 100 characters, 
# put value of key "html" into a list, and count the number of files that has the same value in the list
# output value list with count of each item as a table to a file named "simpleduplicate.txt"

import os
import json
import sys
import collections

# define path to the folder that contains all JSON files
path = "../storage/datasets/default/"

def extract_simple_duplicate():
    html = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".json"):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if len(data['html']) >= 100 and len(data['html']) <= 2000:
                        html.append(data['html'])
    counter = collections.Counter(html)

    # put dulicate files into to-be-delete.txt and only keep one
    with open('to-be-delete.txt', 'w', encoding='utf-8') as output:
        for item in counter.items():
            if(item[1] > 1):
                for root, dirs, files in os.walk(path):
                    for file in files:
                        if file.endswith(".json"):
                            with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                                data = json.load(f)
                                if data['html'] == item[0]:
                                    output.write(file + '\n')
                                    break
    
    # loop through to-be-delete.txt and delete the files
    with open('to-be-delete.txt', 'r', encoding='utf-8') as f:
        for line in f:
            os.remove(path + line.strip())



if __name__ == "__main__":
    extract_simple_duplicate()
    print("Simple duplicate extracted successfully!")
    sys.exit(0)
