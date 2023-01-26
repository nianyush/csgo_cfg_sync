from os import listdir, system
from os.path import exists
from shutil import copytree, rmtree
import json
import sys
import winreg

if __name__ == '__main__':
    f = open("config.json")
    config = json.load(f)
    f.close()
    if config['use_winreg']:
        try:
            hkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\WOW6432Node\Valve\Steam")
        except:
            hkey = None
            print(sys.exc_info())
        
        try:
            steam_path = winreg.QueryValueEx(hkey, "InstallPath")
        except:
            steam_path = None
            print(sys.exc_info())
        path = steam_path[0] + "\\userdata"
    else:
        path = config["path"]
    print("steam userdata path is " + path)


    dirs = [f for f in listdir(path)]
    dirs.remove(config['mainAccount'])
    for dir in dirs:
        src = path + "\\" + config['mainAccount']+'\\730'
        dst = path + "\\" + dir +'\\730'
        if exists(dst):
            rmtree(dst)
        copytree(src, dst)
    k=input("press any key to exit") 
    
