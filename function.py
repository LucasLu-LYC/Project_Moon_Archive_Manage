import os
import subprocess
import psutil
import compress as c
import json
from pynput import keyboard

is_exit = False

def is_exit_function(key):
    global is_exit
    try:
        while True:
            if key == keyboard.Key.f12:
                is_exit = True
                return True
            else:
                is_exit = False
                return False
    except:
        is_exit = False
        return False


def write_data_to_json(gametype, compress_type, path):
    try:
        with open('config.json', 'r', encoding='utf-8') as old:
            data = json.load(old)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    if data:
        last_item = max(data, key=lambda x: x['item'])['item']
    else:
        last_item = 0
    new_data = {
                'item' : last_item + 1,
                'gametype' : gametype,
                'compress_type' : compress_type,
                'path' : path,
            }
    data.append(new_data)

    with open('config.json', 'w', encoding='utf-8') as new:
        json.dump(data, new, ensure_ascii=False, indent=4) 

def check_json_file(): 
    if os.path.exists('config.json'):
        pass
    else:
        with open('config.json', 'w') as f:
            pass

def track_process(process_name):
    print(f"Tracking {process_name} process...")
    try:
        # 启动进程
        process = subprocess.Popen(process_name, shell=True)
        print(f"{process_name} started.")
        
        # 等待进程结束
        process.wait()
        print(f"{process_name} closed.")
    except Exception as e:
        print(f"An error occurred: {e}")

def check_archive_name(name):
    error_chars = r'<>:"/\\|?*()[{}]'
    # 检查文件名中是否包含非法字符
    if any(char in name for char in error_chars):
        return False
    if len(name) > 255:
        return False
    if (name.startswith('.') or name.startswith(' ') or name.endswith(' ') or name.startswith('/') or name.startswith(':') or name.startswith(';')):
        return False
    return True

def fuzzy_search(name, options): # 实现模糊搜索
    name = name.lower()  # 将输入转换为小写以忽略大小写
    max_similarity = -1 # 最高相似度
    best_match = None # 最佳匹配
    for option in options:
        option = option.lower()  # 将选项转换为小写
        similarity = 0
        min_len = min(len(name), len(option))  # 取两者长度的最小值
        for i in range(min_len): # 遍历最小长度的字符
            if name[i] == option[i]:
                similarity += 1
        similarity_ratio = similarity / min_len # 计算相似度
        if similarity_ratio > max_similarity: #匹配更高的相似度
            max_similarity = similarity_ratio
            best_match = option
    if best_match: #返回结果
        return best_match
    else:
        return None

def compress_lobotomyCorp(output_zip,type): #压缩LobotomyCorp游戏存档
    folder_path = r"C:\Users\luyuc\AppData\LocalLow\Project_Moon" #确定压缩的文件夹
    if type == '7z':
        is_finish = c.compress_to_7z(folder_path, output_zip) #压缩文件为7z

    elif type == 'zip':
        is_finish = c.compress_to_zip(folder_path, output_zip) #压缩文件为zip

    return is_finish

def compress_libraryOfRuina(output_zip,type): #压缩Library of Ruina游戏存档
    folder_path = r"C:\Users\luyuc\AppData\LocalLow\Project Moon" #确定压缩的文件夹
    if type == '7z':
        is_finish = c.compress_to_7z(folder_path, output_zip) #压缩文件为7z
    elif type == 'zip':
        is_finish = c.compress_to_zip(folder_path, output_zip) #压缩文件为zip
    return is_finish

def is_game_running(): #判断游戏是否在运行
    try:
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            print(proc.info)
            if proc.info['name'] == 'LobotomyCorp.exe' or proc.info['name'] == 'lobotomycorp.exe':
                print("LobotomyCorp is running")
                is_lob_running = True
                return 'lob'
            elif proc.info['name'] == 'LibraryOfRuina.exe':
                print("LibraryOfRuina is running")
                is_lib_running = True
                return 'lib'
    except:
        print("Error")
        return False

def auto_archiving(stop): #自动压缩存档
    while stop == True:
        running_game = is_game_running()
        if running_game == 'lob':
            is_lob_run = True
            is_lob_save = True
        elif running_game == 'lib':
            is_lib_run = True
            is_lib_save = True
        if is_lob_run == False and is_lob_save == True:
            compress_lobotomyCorp()
            is_lob_save = False
        elif is_lib_run == False and is_lib_save == True:
            compress_libraryOfRuina()
            is_lib_save = False

