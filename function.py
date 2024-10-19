import os
import zipfile

def zip_folder(folder_path, output_zip):
    # 创建一个ZipFile对象，并设置模式为写入
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # 遍历文件夹
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # 创建文件的完整路径
                file_path = os.path.join(root, file)
                # 将文件添加到zip文件中
                # 使用os.path.relpath获取文件相对于文件夹的相对路径
                zipf.write(file_path, os.path.relpath(file_path, os.path.dirname(folder_path)))

def fuzzy_search(name, options):
    name = name.lower()  # 将输入转换为小写以忽略大小写
    max_similarity = -1
    best_match = None

    for option in options:
        option = option.lower()  # 将选项转换为小写
        similarity = 0
        min_len = min(len(name), len(option))  # 取两者长度的最小值

        # 遍历每个字符并比较
        for i in range(min_len):
            if name[i] == option[i]:
                similarity += 1

        # 计算相似度比例
        similarity_ratio = similarity / min_len

        # 更新最相似的匹配
        if similarity_ratio > max_similarity:
            max_similarity = similarity_ratio
            best_match = option

    # 输出结果
    if best_match:
        print(f"Best match: {best_match} with similarity {max_similarity:.2f}")
        return best_match
    else:
        print("Error!")
        return None

def zip_lobotomyCorp_cmd():
    folder_path = r"C:\Users\luyuc\AppData\LocalLow\Project_Moon"
    print("Enter the output zip file path.If you to use defulse path,please enter 0")
    isdefule = input()
    if isdefule == '0':
        print("defult")
        output_zip = r"C:\Users\luyuc\Desktop\Project_Moon.zip"
    else:
        print("undefult")
        output_zip = os.path.normpath(os.path.abspath(input()))
    zip_folder(folder_path, output_zip)
    print("Done!")

def zip_libraryOfRuina_cmd():
    folder_path = r"C:\Users\luyuc\AppData\LocalLow\Project Moon"
    print("Enter the output zip file path.If you to use defulse path,please enter 0")
    isdefule = input()
    if isdefule == '0':
        print("defult")
        output_zip = r"C:\Users\luyuc\Desktop\Project Moon.zip"
    else:
        print("undefult")
        output_zip = os.path.normpath(os.path.abspath(input()))
    zip_folder(folder_path, output_zip)
    print("Done!")
    

if __name__ == '__main__':
    print("Choose a game")
    gametype = input()
    gametype = gametype.lower()
    if gametype == 'lobotomycorp':
        zip_lobotomyCorp_cmd()
    elif gametype == 'libraryofruina' or gametype == 'library of ruina':
        zip_libraryOfRuina_cmd()
    else:
        print("fuzzy search")
        options = ['lobotomycorp', 'libraryofruina', 'library of ruina']
        choose_game = fuzzy_search(gametype, options)
        print(choose_game)