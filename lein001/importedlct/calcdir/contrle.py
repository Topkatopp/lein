import sys
import os
from colorama import *
import random

randimport = False


def write1(*args):
    writecheckcmplt2 = 0
    writecheckcmplt = 0
    writecheck = args.count('(')
    if writecheck > 1:
        system = Fore.RED + f"""write1("{args}")
    ^^^^
    founded error in write1("{args}")
    invalid syntax error""" + Fore.RESET
        print(system)
        writecheckcmplt = 1
    writecheck2 = args.count(')')

    if writecheck2 > 1:
        system = Fore.RED + f"""write1("{args}")
    ^^^^
    founded error in write1("{args}")
    invalid syntax error""" + Fore.RESET
        print(system)
        writecheckcmplt2 = 1
    if writecheckcmplt2 != 1:
        print(*args)
    elif writecheckcmplt != 1:
        print(*args)

def imp(arg, other=False, command="*"):
    global randimport
    if arg == "random":
        f = open(r"C:\lein001\module\random.py", "r")
        randomline = f.read()
        f.close()
        with open(r"module\random.py", "w") as f:
            f.write(randomline)
        try:
            import module.random as mr
        except SyntaxError:
            pass
        randimport = True
    else:
        if other == False:
            print(Fore.RED + f"""imp({arg}, other={other})
    {"^" * len(arg)}
founded error in imp({arg}, other={other})
error not founded module {arg}
""" + Fore.RESET)
        elif other == True:
            if command == "*":
                try:
                    globals().update(__import__(f"module.{arg}", fromlist=["*"]).__dict__)
                except:
                    print(Fore.RED + f"""imp({arg}, other={other})
    {"^" * len(arg)}
founded error in imp({arg}, other={other})
error not founded module {arg}""" + Fore.RESET)
            else:
                try:
                    globals().update(__import__(f"module.{arg}", fromlist=[f"{command}"]).__dict__)
                except:
                    print(Fore.RED + f"""imp({arg}, other={other}, command={command})
    {"^" * len(arg)}
founded error in imp({arg}, other={other}, command={command})
error not founded module {arg}""" + Fore.RESET)
        else:
            print(Fore.RED + f"""imp({arg}, other={other})
    {" " * len(arg)}        {"^" * len(other)}
founded error in imp({arg}, other={other})
error {other} takes only 2 arguments 'True' and 'False' but gives '{other}'
""" + Fore.RESET)






def write2(*args, type="str", error=True):
    writecheckcmplt2 = 0
    writecheckcmplt = 0
    writecheck = args.count('(')
    if writecheck > 1:
        system = Fore.RED + f"""write1("{args}")
    ^^^^
    founded error in write1("{args}")
    invalid syntax error""" + Fore.RESET
        print(system)
        writecheckcmplt = 1
    writecheck2 = args.count(')')

    if writecheck2 > 1:
        system = Fore.RED + f"""write1("{args}")
    ^^^^
    founded error in write1("{args}")
    invalid syntax error""" + Fore.RESET
        print(system)
        writecheckcmplt2 = 1
    if type == "int":
        if writecheckcmplt2 != 1:
            print(*args, end="")
            try:
                wirte2int = int(input())
            except:
                if error:
                    print(Fore.RED + f"""write2("{args}")
            ^^^^^^^^^^^^^^^^^^
            founded error in write2("{args}")
            str symbol can't be int symbol""" + Fore.RESET)
                    wirte2int = 0.0
            return wirte2int
        elif writecheckcmplt != 1:
            print(*args, end="")
            try:
                wirte2int = int(input())
            except:
                if error:
                    print(Fore.RED + f"""write2("{args}")
            ^^^^^^^^^^^^^^^^^^
            founded error in write2("{args}")
            str symbol can't be int symbol""" + Fore.RESET)
                    wirte2int = 0.0
            return wirte2int
    elif type == "float":
        if writecheckcmplt2 != 1:
            print(*args, end="")
            try:
                wirte2int = float(input())
            except:
                if error:
                    print(Fore.RED + f"""write2("{args}")
^^^^^^^^^^^^^^^^^^
founded error in write2("{args}")
str symbol can't be float symbol""" + Fore.RESET)
                    wirte2int = 0.0
            return wirte2int
        elif writecheckcmplt != 1:
            print(*args, end="")
            try:
                wirte2int = float(input())
            except:
                if error:
                    print(Fore.RED + f"""write2("{args}")
^^^^^^^^^^^^^^^^^^
founded error in write2("{args}")
str symbol can't be float symbol""" + Fore.RESET)
                    wirte2int = 0.0

            return wirte2int
    else:
        if writecheckcmplt2 != 1:
            print(*args, end="")
            wirte2int = input()
            return wirte2int
        elif writecheckcmplt != 1:
            print(*args, end="")
            wirte2int = input()
            return wirte2int


def rand(n, b):
    if randimport:
        import module.random as mr
        result = mr.randomrun(n, b)
        return result
    else:
        print(Fore.RED + f"""rand({n}, {b})
^^^^
founded error in
rand({n}, {b})
error no module named rand""" + Fore.RESET)


def calc(arg):
    arg = str(arg)
    try:
        arg = eval(arg)
    except ZeroDivisionError:
        print(Fore.RED + f"""calc("{arg}")
      {"^" * len(arg)}
founded error in calc("{arg}")
type of error is ERROR DIVISION BY ZERO""" + Fore.RESET)
        arg = ".inf"
    except:
        print(Fore.RED + f"""calc("{arg}")
      {"^" * len(arg)}
founded error in calc("{arg}")
type of error is INVALID ARGUMENT ERROR""" + Fore.RESET)
        arg = "None"
    return arg

