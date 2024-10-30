import os
import zipfile
from py7zr import SevenZipFile
def compress_to_zip(source_path, output_path):
    if not os.path.exists(source_path):
        return 1
    try:
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(source_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, start=source_path))
        return 0
    except:
        return 2

def compress_to_7z(source_path, output_path):
    # 检查文件夹路径是否存在
    if not os.path.isdir(source_path):
        return 1
    
    try:
        with SevenZipFile(output_path, 'w') as archive:
            # 遍历文件夹，添加所有文件到压缩文件中
            for root, dirs, files in os.walk(source_path):
                for file in files:
                    # 构造文件的完整路径
                    file_path = os.path.join(root, file)
                    # 构造文件在压缩包中的相对路径
                    archive.write(file_path, arcname=os.path.relpath(file_path, start=source_path))
        print(output_path)
        return 0
    except:
        return 2

# 使用示例
# source_path = "C:/Users/" + os.getlogin() + "/AppData/LocalLow/Project_Moon"
# print("源路径：" + source_path)
# zip_output_path = os.getcwd() + '\text.zip'
# print("ZIP输出路径：" + zip_output_path)
# print(compress_to_zip(source_path, zip_output_path))

# sevenz_output_path = os.getcwd() + '\text.7z'
# print("7z输出路径：" + sevenz_output_path)
# print(compress_to_7z(source_path, sevenz_output_path))
