# read blankhtmlcount.txt
# and extract the file names to a list excluding the last line which is the count of blank html files
# delete the files in the list
import os
import sys

path = "../storage/datasets/default/"

def extract_file_names():
    with open('blankhtmlcount.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        file_names = lines[:-1]
        return file_names

def delete_files(file_names):
    for file_name in file_names:
        file_name = file_name.strip()
        os.remove(os.path.join(path, file_name))

if __name__ == "__main__":
    file_names = extract_file_names()
    delete_files(file_names)
    print("Files deleted successfully!")
    sys.exit(0)


