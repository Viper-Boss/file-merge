import os
import shutil

# 要处理的文件的目录
src_dir = r"C:\Users\用户名\Desktop\test"

# 获取要处理的文件的列表
files = os.listdir(src_dir)

for filename in files:
    # 获取文件名的前4个字符前缀
    prefix = filename[:4]
    # 获取文件名的第5个字符到第14个字符的10位数字
    num = filename[4:14]
    # 获取文件的完整路径
    file_path = os.path.join(src_dir, filename)

    # 遍历文件夹列表
    for dirname in os.listdir(src_dir):
        # 判断是否是文件夹
        if os.path.isdir(os.path.join(src_dir, dirname)):
            # 获取文件夹的前10个字符
            folder_num = dirname[:10]
            # 判断文件夹前10个字符与文件名的10位数字是否相同
            if folder_num == num:
                # 将文件移动到该文件夹
                shutil.move(file_path, os.path.join(src_dir, dirname, filename))
                break
