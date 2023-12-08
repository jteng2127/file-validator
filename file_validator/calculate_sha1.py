import hashlib
import os
from tqdm import tqdm
from .count_files import count_files

def calculate_file_sha1(file_path):
    sha1 = hashlib.sha1()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(65536)  # 讀取固定大小的資料塊以節省記憶體
            if not data:
                break
            sha1.update(data)
    return sha1.hexdigest()

def calculate_all_sha1_in_folder(folder_path, recursive=True):
    print(f'Calculating SHA1 for all files in {folder_path}...')
    sha1_dict = {}
    if recursive:
        file_count = count_files(folder_path)
    else:
        file_count = len(os.listdir(folder_path))
    with tqdm(total=file_count) as pbar:
        if recursive:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    sha1_dict[file_path] = calculate_file_sha1(file_path)
                    pbar.update(1)
        else:
            for file in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file)
                sha1_dict[file_path] = calculate_file_sha1(file_path)
                pbar.update(1)

    return sha1_dict
