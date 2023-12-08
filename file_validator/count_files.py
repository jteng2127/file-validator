import os

def count_files(directory, recursive=True):
    total_files = 0
    if recursive:
        for root, dirs, files in os.walk(directory):
            total_files += len(files)
    else:
        total_files = len(os.listdir(directory))
    return total_files
