import os
import shutil
from colorama import *


def delete_directory(path):
    # Iterate over all the files and subdirectories
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            file_path = os.path.join(root, name)
            os.remove(file_path)  # Delete individual file
        for name in dirs:
            dir_path = os.path.join(root, name)
            os.rmdir(dir_path)  # Delete individual subdirectory

    # Delete the root directory
    shutil.rmtree(path)


start = True
while start:
    system = input(">> ")
    try:
        print(eval(system))
    except ZeroDivisionError:
        print(Fore.RED + """">> 1/0"
    ^^^
division by zero error
line 1""" + Fore.RESET)
    except KeyboardInterrupt:
        pass
    except EOFError:
        pass
    except:
        pass
    if "echo" in system:
        system = system.replace("echo ", "", 1)
        print(system)
    elif 'write1("' in system:
        # check1
        writecheck = system.count('(')
        if writecheck > 1:
            system = Fore.RED + f"""{system}
^^^^
founded error in {system}
line 1
invalid syntax error""" + Fore.RESET
            print(system)
            continue
        writecheck2 = system.count(')')
        # check2
        if writecheck2 > 1:
            system = Fore.RED + f"""{system}
^^^^
founded error in {system}
line 1
invalid syntax error""" + Fore.RESET
            print(system)
            continue
        # end chek
        system = system.replace('write1("', "", 1)
        system = system.replace('")', "", 1)
        print(system)
    elif "write2" in system:
        writecheck = system.count('(')
        if writecheck > 1:
            system = Fore.RED + f"""{system}
^^^^
founded error in {system}
line 1
invalid syntax error""" + Fore.RESET
            print(system)
            continue
        writecheck2 = system.count(')')

        if writecheck2 > 1:
            system = Fore.RED + f"""{system}
^^^^
founded error in {system}
line 1
invalid syntax error""" + Fore.RESET
            print(system)
            continue
        system = system.replace("write2", "", 1)
        system = system.replace("(", "", 1)
        system = system.replace(")", "", 1)
        system = system.replace('"', "")
        input(system)
    elif system.startswith("reimport") == True:
        system = system.replace("reimport ", "", 1)
        try:
            orf = open(fr"..\savele\{system}saved.le", "r")
        except:
            print("file not found")
            continue
        linesaved = orf.read()
        orf.close()
        sfw = open(fr"..\importlct\{system}.le", "w")
        sfw.write(linesaved)
        sfw.close()
        delete_directory(f'..\\importedlct\\{system}dir')
        print(Fore.GREEN + "succesfly reimported" + Fore.RESET)
    elif system.startswith("import") == True:
        system = system.replace("import ", "", 1)
        try:
            f = open(fr"..\importlct\{system}.le", "r")
            testline = f.read()
        except:
            print("file not found")
            continue
        f.close()
        os.mkdir(fr"..\importedlct\{system}dir")
        os.mkdir(fr"..\importedlct\{system}dir\module")
        if 'imp("random")' in testline or "imp('random')" in testline:
            with open('..\\module\\random.py', "r") as f:
                randomcode = f.read()
            with open(fr'..\importedlct\{system}dir\module\random.py', "w") as fd:
                fd.write(randomcode)
                
        lines = testline.splitlines()
        for i, line in enumerate(lines):
            if "imp(" in line:
                lines[i] += "\nfrom contrle import *"
        code = "\n".join(lines)

        wsf = open(fr"..\savele\{system}saved.le", "w")
        wsf.write(testline)
        wsf.close()
        wf = open(fr"..\importedlct\{system}dir\{system}.py", "w")
        wf.write(f"from contrle import *\n{code}")
        wf.close()
        cntrls = open(fr"..\contrlesave\contrle.txt", "r")
        scntrline = cntrls.read()
        cntrls.close()
        cntrcr = open(fr"..\importedlct\{system}dir\contrle.py", "w")
        cntrcr.write(scntrline)
        cntrcr.close()
        with open(fr"..\importedlct\{system}dir\module\__init__.py", "w") as cremod:
            cremod.write("")
        os.system(fr'del ..\importlct\{system}.le')
        print("succesfly imported DON'T DELETE contrle.py THAT IS CRITICAL FILE")
