import function
from function import *
import shutil

def check():
    function.check_json_file()
    menu()

def menu():
    terminal_width = int(shutil.get_terminal_size().columns) # 获取终端宽度
    #---project_moon_archive_manage---
    print('-' * int(terminal_width / 2 - 27 / 2),'Project Moon Archive Manage', '-' * int(terminal_width - (terminal_width / 2 - 27 / 2) - 29)) # 打印标题
    print('Menu')
    print(" 1.Save archive","\n","2.Delete archive","\n","3.Search archive","\n","4.Change archive","\n","5.edit archive","\n","6.Exit") # 打印菜单
    maintype = input("Please enter the number of the function you want to use: ")
    if maintype == '1':
        save_archive()

def save_archive():
    gametype = input("Please enter the game name: ")
    isdefult = input("Do you want to use the default path? In the foulder where the software is located? (y/n): ")
    options = ['lobotomycorp', 'libraryofruina']
    gametype = function.fuzzy_search(gametype,options)
    compress_type = input("Please enter the compress type: ")
    archive_name = input("Please enter the archive name: ")
    print('gametype:',gametype,' compress_type:',compress_type,' archive_name:',archive_name,' isdefult:',isdefult)
    #根据参数进行存档
    if gametype == "lobotomycorp":
        if isdefult == 'y':
            if compress_type == 'zip':
                path = os.getcwd() + '/' + archive_name + '.zip'
                function.compress_lobotomyCorp(path,'zip')
            elif compress_type == '7z':
                path = os.getcwd() + '/' + archive_name + '.7z'
                function.compress_lobotomyCorp(path,'7z')
            else:
                print("Invalid compress type.")
        else:
            path = input("Please enter the path of the compress file: ")
            if compress_type == 'zip':
                function.compress_lobotomyCorp(path,'zip')
            elif compress_type == '7z':
                function.compress_lobotomyCorp(path,'7z')
            else:
                print("Invalid compress type.")
    
    elif gametype == 'libraryofruina':
        if isdefult == 'y':
            if compress_type == 'zip':
                path = os.getcwd() + '/' + archive_name + '.zip'
                function.compress_libraryOfRuina(path,'zip')
            elif compress_type == '7z':
                path = os.getcwd() + '/' + archive_name + '.7z'
                function.compress_libraryOfRuina(path,'7z')
            else:
                print("Invalid compress type.")
        else:
            path = input("Please enter the path of the comrpess file: ")
            if compress_type == 'zip':
                function.compress_libraryOfRuina(path,'zip')
            elif compress_type == '7z':
                function.compress_libraryOfRuina(path,'7z')
            else:
                print("Invalid compress type.")

    try:
        with open('config.json', 'r', encoding='utf-8') as old:
            data = json.load(old)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    new_data = {
                'gametype' : gametype,
                'compress_type' : compress_type,
                'path' : path,
            }
    data.append(new_data)

    with open('config.json', 'w', encoding='utf-8') as new:
        json.dump(data, new, ensure_ascii=False, indent=4) 

if __name__ == '__main__':
    check()