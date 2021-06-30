import os
import operator
from pprint import pprint

def compile_files(files_list):
    data = []
    for file in files_list:
        with open(file, encoding="utf-8") as f:
            file_data = f.readlines()
            data.append( (len(file_data), file, " ".join(file_data)))

    with open("result_data.txt", "w", encoding="utf-8") as new_file:
        for length, name, content in sorted(data, key=lambda x: x[0]):
            new_file.write(name+'\n')
            new_file.write(str(length)+'\n')
            new_file.write(content+'\n')
            print(length, name, content )

files = ["1.txt", "2.txt", "3.txt"]
compile_files(files)
