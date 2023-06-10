import os
import sys

module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, module_path)

import commands.charge.charge as charge
from commands.cmd.text.text import *
from commands.filesys.filesys import *

os.chdir(os.getcwd() + "\\0)")

curdir = "C:\\"

while True:
    a = input(curdir + ">> ")
    if a == "e":
        charge.reboot()
        os.chdir(os.getcwd())
    elif a == "cls":
        cls()

    elif a.startswith("mkdir ") == True:
        a = a.replace("mkdir ", "", 1)
        if "\\" in a:
            print(Fore.RED + "error you can't use like a mkdir n\\n you can use only mkdir n" + Fore.RESET)
        else:
            print(Fore.RED + makedir(a) + Fore.RESET)

    elif a.startswith("cd ") == True:
        a = a.replace("cd ", "", 1)

        if curdir == "C:\\" and a == "..":
            print(Fore.RED + "cannot go out from C:\\" + Fore.RESET)
        elif "\\" in a:
            print(Fore.RED + "error you can't use like a cd n\\n you can use only cd n" + Fore.RESET)
        elif a.startswith("...") == True:
            print(Fore.RED + "error cannot join to the directry: " + a + Fore.RESET)
        elif a == ".":
            print(Fore.RED + "error cannot join to the directry: " + a + Fore.RESET)
        else:
            result = cdir(a)
            if result == "":
                if curdir == "C:\\":
                    curdir = curdir + a
                elif a == "..":
                    curdir = curdir.split("\\")
                    curdir.pop()
                    curdir = "\\".join(curdir)
                else:
                    curdir = curdir + "\\" + a
            else:
                print(Fore.RED + result + Fore.RESET)

    elif a.startswith("rmdir ") == True:
        a = a.replace("rmdir ", "", 1)
        if "\\" in a:
            print(Fore.RED + "error you can't use like a rmdir n\\n you can use only rmdir n" + Fore.RESET)
        else:
            print(Fore.RED + removedir(a) + Fore.RESET)

    elif a == "dir":
        print(directorylist())

    elif a.startswith("mkfile ") == True:
        a = a.replace("mkfile ", "", 1)
        a = a.replace("\\n", "\n")
        if a == "-n":
            pass
        else:
            a = a.split(" ")
            try:
                name, *other = a
                oldtext = other
                other = " ".join(other)
                mkfile(name, other)
                print(oldtext)
            except:
                name = a[0]
                mkfile(name, "")

    elif a.startswith("read ") == True:
        a = a.replace("read ", "", 1)
        print(readfile(a))

    elif a.startswith("python ") == True:
        os.system(a)


    elif a == "":
        continue

    elif a.startswith(" ") == True:
        continue

    else:
        print(Fore.RED + "unknow command: " + a + Fore.RESET)
