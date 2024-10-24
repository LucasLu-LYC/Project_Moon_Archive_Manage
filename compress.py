import os
import zipfile
from py7zr import SevenZipFile
def compress_to_zip(source_path, output_path):
    if not os.path.exists(source_path):
        return "源路径不存在。"
    try:
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(source_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, start=source_path))
        return f"文件已成功压缩为ZIP格式：{output_path}"
    except Exception as e:
        return f"压缩ZIP时出错：{e}"

def compress_to_7z(source_path, output_path):
    if not os.path.exists(source_path):
        return "源路径不存在。"
    try:
        with SevenZipFile(output_path, 'w') as zipf:
            for root, dirs, files in os.walk(source_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, arcname=os.path.relpath(file_path, start=source_path))
        return f"文件已成功压缩为7z格式：{output_path}"
    except:
        return 1

# 使用示例
source_path = "C:/Users/" + os.getlogin() + "/AppData/LocalLow/Project_Moon"
print("源路径：" + source_path)
zip_output_path = os.getcwd() + '\text.zip'
print("ZIP输出路径：" + zip_output_path)
print(compress_to_zip(source_path, zip_output_path))

sevenz_output_path = os.getcwd() + '\text.7z'
print("7z输出路径：" + sevenz_output_path)
print(compress_to_7z(source_path, sevenz_output_path))
