import function
from function import *
import shutil
import time
import threading

def is_function_exit():
    while True:
        with keyboard.Listener(on_press=function.is_exit_function) as listener:
            listener.join()

def check():
    function.check_json_file()
    menu()

def menu():
    terminal_width = int(shutil.get_terminal_size().columns) # 获取终端宽度
    #---project_moon_archive_manage---
    while True:
        os.system('cls')
        print('-' * int(terminal_width / 2 - 27 / 2),'Project Moon Archive Manage', '-' * int(terminal_width - (terminal_width / 2 - 27 / 2) - 29)) # 打印标题
        print('Menu')
        print(" 1.Save archive","\n","2.Delete archive","\n","3.Search archive","\n","4.Change archive","\n","5.edit archive","\n","6.Exit") # 打印菜单
        maintype = input("Please enter the number of the function you want to use: ")
        if maintype == '1':
            save_archive()

def save_archive():
    #获取存档信息
    def get_input():
        while True:
            temp = 0
            gametype = input("Please enter the game name: ")
            options = ['lobotomycorp', 'libraryofruina']
            gametype = function.fuzzy_search(gametype, options)
            archive_name = input("Please enter the archive name: ")
            is_archive_correct = function.check_archive_name(archive_name)
            if is_archive_correct == False:
                while is_archive_correct == False:
                    archive_name = input("Error! Please enter the archive name again: ")
                    is_archive_correct = function.check_archive_name(archive_name)
            compress_type = input("Please enter the compress type: ")
            while compress_type not in ['7z', 'zip']:
                compress_type = input("Error! Please enter the compress type (7z or zip): ")
            try:
                with open('config.json', 'r', encoding='utf-8') as file:
                    data_check = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                data_check = []  # 如果文件不存在或不是有效的JSON，初始化为空列表
            isdefult = input("Do you want to use the default path? In the folder where the software is located? (y/n): ")
            if isdefult == 'y':
                path = os.path.join(os.getcwd(), str(archive_name) + '.zip')
            else:
                path = input("Please enter the path of the compress file: ")
                path = os.path.normpath(path)
                if path[len(path) - 1] == '/' or ord(path[len(path) - 1]) == 92:
                    path = path + str(archive_name) + '.' + str(compress_type)
                else:
                    path = path + '/' + str(archive_name) + '.' + str(compress_type)
            for item in data_check:
                print('item=',item,' item[path]=',item['path'],' path=',path)
                if item['path'] == path:
                    print("Error! Path already exists.")
                    temp = 1
                    break
            if temp == 1:
                continue
            print("Please check the information. Gametype:", gametype, " Archive name:", archive_name, " Compress type:", compress_type, " Save file path:", path)
            is_finish = input("Is it right? (y/n)")
            if is_finish.lower() == 'y':
                return gametype, archive_name, compress_type, path
            else:
                os.system('cls')
                continue

    gametype,archive_name,compress_type,path = get_input()

    #根据参数进行存档
    if gametype == "lobotomycorp":
        if compress_type == 'zip':
            #path = os.getcwd() + '\\' + archive_name + '.zip'
            function.compress_lobotomyCorp(path,'zip')
        elif compress_type == '7z':
            #path = os.getcwd() + '\\' + archive_name + '.7z'
            function.compress_lobotomyCorp(path,'7z')
    
    elif gametype == 'libraryofruina':
        if compress_type == 'zip':
            #path = os.getcwd() + '\\' + archive_name + '.zip'
            function.compress_libraryOfRuina(path,'zip')
        elif compress_type == '7z':
            #path = os.getcwd() + '\\' + archive_name + '.7z'
            function.compress_libraryOfRuina(path,'7z')

    #将存档信息写入json文件
    function.write_data_to_json(gametype,compress_type,path)

    for i in range(3):
        # if function.is_exit == True:
        #     return None
        print(i,"seconds to exit this function.(return to main menu) If you don't want to exit,please press space key.")
        time.sleep(1)

if __name__ == '__main__':
    check()