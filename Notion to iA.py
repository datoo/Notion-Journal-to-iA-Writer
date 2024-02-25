import os
import re
from datetime import datetime

def extract_and_rename_files(folder_path):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            
            if os.path.isfile(file_path):
                with open(file_path, 'r', errors='ignore') as file:
                    content = file.read()

                # 使用正则表达式提取"Date:"和"Tags"之间的内容
                match = re.search(r'\bDate:(.*?)(?=Tags:|$)', content, re.IGNORECASE | re.DOTALL)

                if match:
                    extracted_content = match.group(1).strip()

                    # 将提取的内容转换为日期格式
                    try:
                        date_obj = datetime.strptime(extracted_content, '%B %d, %Y')
                        new_format_date = date_obj.strftime('%Y-%m-%d')

                        # 构造新的文件名
                        new_filename = f"{new_format_date}.txt"
                        new_path = os.path.join(folder_path, new_filename)

                        # 输出提取的内容和新文件名
                        print(f"File: {filename}")
                        print(f"Extracted Content: {extracted_content}")
                        print(f"Renamed Content: {new_format_date}")
                        print(f"New Filename: {new_filename}\n")

                        # 在这里进行文件重命名
                        os.rename(file_path, new_path)
                    except ValueError:
                        print(f"Error: Unable to parse extracted content as date in file {filename}\n")

        print("Extraction and renaming completed.")
    except Exception as e:
        print(f"Error: {e}")

# 示例用法：
folder_path = 'change'
extract_and_rename_files(folder_path)

import os

def add_lines_to_files_in_folder(folder_path):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            
            if os.path.isfile(file_path):
                with open(file_path, 'a') as file:
                    # 在文件末尾添加空白行和新行
                    file.write('\n')
                    file.write('#Notion\n')
                    file.write('#日记\n')

                print(f"Lines added to file {filename}")
                
        print("Lines added to all files.")
    except Exception as e:
        print(f"Error: {e}")

# 示例用法：
add_lines_to_files_in_folder(folder_path)

import os

def replace_location_tags_in_files(folder_path):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                    content = file.read()

                # 替换 "Location: " 和 "Tags: " 为 "#"
                content = content.replace('Location: ', '#').replace('Tags: ', '#')

                # 将修改后的内容写回文件
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content)

                print(f"Replaced 'Location:' and 'Tags:' in file {filename}")
                
        print("Replacement completed in all files.")
    except Exception as e:
        print(f"Error: {e}")

# 示例用法：

replace_location_tags_in_files(folder_path)
