import function as f
from function import *
import shutil

def run_cmd():
    terminal_width = int(shutil.get_terminal_size().columns) # 获取终端宽度
    #---project_moon_archive_manage---
    print('-' * int(terminal_width / 2 - 27 / 2),'Project Moon Archive Manage', '-' * int(terminal_width - (terminal_width / 2 - 27 / 2) - 29)) # 打印标题
    print('Menu')
    print(" 1.Save archive","\n","2.Delete archive","\n","3.Search archive","\n","4.Change archive","\n","5.edit archive","\n","6.Exit") # 打印菜单
    maintype = input("Please enter the number of the function you want to use: ")
    if maintype == '1': # 保存存档
        #获取保存参数
        gametype = input("Please enter the game name: ")
        isdefult = input("Do you want to use the default path? In the foulder where the software is located? (y/n): ")
        options = ['lobotomycorp', 'libraryofruina']
        gametype = f.fuzzy_search(gametype,options)
        compress_type = input("Please enter the compress type: ")
        print(gametype)
        #根据参数进行存档
        if gametype == "lobotomycorp":
            if isdefult == 'y':
                if compress_type == 'zip':
                    f.compress_lobotomyCorp(True,None,'zip')
                elif compress_type == '7z':
                    f.compress_lobotomyCorp(True,None,'7z')
                else:
                    print("Invalid compress type.")
            else:
                path = input("Please enter the path of the zip file: ")
                if compress_type == 'zip':
                    f.compress_lobotomyCorp(True,None,'zip')
                elif compress_type == '7z':
                    f.compress_lobotomyCorp(True,None,'7z')
                else:
                    print("Invalid compress type.")
        
        elif gametype == 'libraryofruina':
            if isdefult == 'y':
                if compress_type == 'zip':
                    f.compress_libraryOfRuina(True,None,'zip')
                elif compress_type == '7z':
                    f.compress_libraryOfRuina(True,None,'7z')
                else:
                    print("Invalid compress type.")
            else:
                path = input("Please enter the path of the zip file: ")
                if compress_type == 'zip':
                    f.compress_libraryOfRuina(True,None,'zip')
                elif compress_type == '7z':
                    f.compress_libraryOfRuina(True,None,'7z')
                else:
                    print("Invalid compress type.")

        else:
            print("Invalid game name.")
    

if __name__ == '__main__':
    run_cmd()