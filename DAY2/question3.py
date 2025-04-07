"""
Question-3:
Given a directory, find out the file Name 
having max size recursively 
"""
import os
def find_largest_file(directory) :
    largest_file = ''
    max_size = 0
    for root , _ , files in os.walk(directory) :
        for file in files :
            file_path = os.path.join(root,file)
            size = os.path.getsize(file_path)
            if size > max_size :
                max_size = size
                largest_file = file_path
    return largest_file,max_size

directory = r"C:\Users\Rahul\Desktop\Assignments"

largest_file, max_size = find_largest_file(directory)
print("Largest file:", largest_file)
print("Size:", max_size, "bytes")
