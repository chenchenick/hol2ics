# loop all JSON format files under relative folder, and count the number of files that has value "" in key "html"
# log file names and output the result to a file named "blankhtmlcount.txt"
# Usage: python count.py
import os
import json
import sys

# define path to the folder that contains all JSON files
path = "../storage/datasets/default/"

# set an array of key "html" value that need to be removed
html = ["", "OK", "Read the Latest", " ", "Read More\nRead More", "Read More\nRead More\nRead More\nRead More"]

def count_blank_html():
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            # print file name
            # print(file)
            # wait for user input
            # sys.stdin.read(1)
            if file.endswith(".json"):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for item in html:
                        if data['html'] == item:
                            count += 1
                            with open('blankhtmlcount.txt', 'a', encoding='utf-8') as f:
                                f.write(file + '\n')
    print(count)
    with open('blankhtmlcount.txt', 'a') as f:
        f.write(str(count))

if __name__ == "__main__":
    count_blank_html()

# Path: dataclean/extract.py
