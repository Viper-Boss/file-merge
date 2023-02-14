import os
import shutil

# 设置源文件夹路径
src_folder =r"C:\Users\86166\Desktop\二级合同成果 - 副本\openAI\test"

# 遍历源文件夹下的所有文件
for filename in os.listdir(src_folder):
    # 获取文件的完整路径
    file_path = os.path.join(src_folder, filename)
    # 如果当前的 file_path 是文件
    if os.path.isfile(file_path):
        # 获取文件的前10个字符
        prefix = filename[:10]
        # 遍历源文件夹下的所有文件夹
        for foldername in os.listdir(src_folder):
            # 获取文件夹的完整路径
            folder_path = os.path.join(src_folder, foldername)
            # 如果当前的 folder_path 是文件夹
            if os.path.isdir(folder_path):
                # 获取文件夹的前10个字符
                folder_prefix = foldername[:10]
                # 如果文件的前10个字符和文件夹的前10个字符相同
                if prefix == folder_prefix:
                    # 移动文件到文件夹中
                    shutil.move(file_path, os.path.join(folder_path, filename))
                    break