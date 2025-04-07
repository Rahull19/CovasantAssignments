"""
Question-4:
Recursively go below a dir and based on filter, dump those files in to  single file 
(work with only text file)
"""
import os

def dump_filtered_files_to_single_file(root_dir, output_file, filter_ext=".txt"):
    with open(output_file, 'wt') as outfile:
        for dirpath, _, filenames in os.walk(root_dir):
            for file in filenames:
                if file.endswith(filter_ext):
                    file_path = os.path.join(dirpath, file)
                    with open(file_path, 'rt') as infile:
                        outfile.write(infile.read())
                        outfile.write("\n")


root_directory = r"C:\Users\Rahul\Desktop\Assignments"
output_filename = "combined_output.txt"

dump_filtered_files_to_single_file(root_directory, output_filename)
print(f"All text files are combined into {output_filename}.")
