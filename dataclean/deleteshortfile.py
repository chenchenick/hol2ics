# loop files and delete files that have value of key "html" less than 100 characters

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
                    if len(data['html']) < 100:
                        html.append(data['html'])
                        # save file name to less100.txt
                        with open('less100.txt', 'a', encoding='utf-8') as output:
                            output.write(file + '\n')
    # loop through less100.txt and delete the files
    with open('less100.txt', 'r', encoding='utf-8') as f:
        for line in f:
            os.remove(path + line.strip())

if __name__ == "__main__":
    extract_simple_duplicate()
    print("Simple duplicate extracted successfully!")
    sys.exit(0)
    