import os
from colorama import *


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
            orf = open(fr"C:\lein001\savele\{system}saved.le", "r")
        except:
            print("file not found")
            continue
        linesaved = orf.read()
        orf.close()
        sfw = open(fr"C:\lein001\importlct\{system}.le", "w")
        sfw.write(linesaved)
        sfw.close()
        os.system(fr"del C:\lein001\importedlct\{system}dir\{system}.py")
        os.system(fr"del C:\lein001\importedlct\{system}dir\contrle.py")
        os.system(fr"del C:\lein001\savele\{system}saved.le")
        os.system(fr"del C:\lein001\importedlct\{system}dir\__pycache__\contrle.cpython-311.pyc")
        try:
            os.system(fr"del C:\lein001\importedlct\{system}dir\module\__pycache__\random.cpython-311.pyc")
        except:
            pass
        try:
            os.system(fr"del C:\lein001\importedlct\{system}dir\module\random.py")
        except:
            pass
        os.system(fr"del C:\lein001\importedlct\{system}dir\module\__pycache__\__init__.cpython-311.pyc")
        os.system(fr"del C:\lein001\importedlct\{system}dir\module\__init__.py")
        os.system(fr"rmdir del C:\lein001\importedlct\{system}dir\module\__pycache__")
        os.system(fr"rmdir C:\lein001\importedlct\{system}dir\module")
        os.system(fr"rmdir C:\lein001\importedlct\{system}dir\__pycache__")
        os.system(fr"rmdir C:\lein001\importedlct\{system}dir")
        print("succesfly reimported")
    elif system.startswith("import") == True:
        system = system.replace("import ", "", 1)
        try:
            f = open(fr"C:\lein001\importlct\{system}.le", "r")
            testline = f.read()
        except:
            print("file not found")
            continue
        f.close()
        lines = testline.splitlines()
        for i, line in enumerate(lines):
            if "imp(" in line:
                lines[i] += "\nfrom contrle import *"
        code = "\n".join(lines)

        os.mkdir(fr"C:\lein001\importedlct\{system}dir")
        os.mkdir(fr"..\importedlct\{system}dir\module")
        wsf = open(fr"C:\lein001\savele\{system}saved.le", "w")
        wsf.write(testline)
        wsf.close()
        wf = open(fr"C:\lein001\importedlct\{system}dir\{system}.py", "w")
        wf.write(f"from contrle import *\n{code}")
        wf.close()
        cntrls = open(fr"C:\lein001\contrlesave\contrle.txt", "r")
        scntrline = cntrls.read()
        cntrls.close()
        cntrcr = open(fr"C:\lein001\importedlct\{system}dir\contrle.py", "w")
        cntrcr.write(scntrline)
        cntrcr.close()
        with open(fr"C:\lein001\importedlct\{system}dir\module\__init__.py", "w") as cremod:
            cremod.write("")
        os.system(fr'del C:\lein001\importlct\{system}.le')
        print("succesfly imported DON'T DELETE contrle.py THAT IS CRITICAL FILE")
