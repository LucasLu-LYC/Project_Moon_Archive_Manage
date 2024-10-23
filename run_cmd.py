import function as f
from function import *
import shutil

def run_cmd():
    terminal_width = int(shutil.get_terminal_size().columns) # 获取终端宽度
    #---project_moon_archive_manage---
    print('-' * int(terminal_width / 2 - 27 / 2),'Project Moon Archive Manage', '-' * int(terminal_width - (terminal_width / 2 - 27 / 2) - 29)) # 打印标题
    print('Menu')
    print(" 1.Save archive","\n","2.Delete archive","\n","3.Search archive","\n","4.Change archive","\n","5.edit archive","\n","6.Exit")
    maintype = input("Please enter the number of the function you want to use: ")
    if maintype == '1':
        gametype = input("Please enter the game name: ")
        isdefult = input("Do you want to use the default path? In the foulder where the software is located? (y/n): ")
        options = ['lobotomycorp', 'libraryofruina']
        gametype = f.fuzzy_search(gametype,options)
        print(gametype)
        if gametype == "lobotomycorp":
            if isdefult == 'y':
                f.zip_lobotomyCorp(True,None)
            else:
                path = input("Please enter the path of the zip file: ")
                f.zip_lobotomyCorp(False,path)
        elif gametype == 'libraryofruina':
            if isdefult == 'y':
                f.zip_libraryOfRuina(True,None)
            else:
                path = input("Please enter the path of the zip file: ")
                f.zip_libraryOfRuina(False,path)
    

if __name__ == '__main__':
    run_cmd()