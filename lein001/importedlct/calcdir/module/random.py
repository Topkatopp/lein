from colorama import *
import random


def randomrun(n, b):
    error2 = 1
    error1 = 1
    try:
        check = n.isalpha()
    except:
        check = False
        check2 = False
        pass
    if check:
        error1 = 1
    try:
        check2 = b.isalpha()
    except:
        check = False
        check2 = False
        pass
    if check2:
        error2 = 1
    iscompl = 0
    try:
        n.isdigit()
    except:
        error = 0
        error1 = 0
        error2 = 0
        iscompl = 1
    if error1 == 1:
        iscompl = 0
        print(Fore.RED + f"""rand("{n}", {b})
     ^^^ invalid syntax error 
rand takes only int character""" + Fore.RESET)
    try:
        b.isdigit()
    except:
        error1 = 0
        error = 0
        iscpompl = 1
    if error2 == 1:
        iscompl = 0
        print(Fore.RED + f"""rand({n}, "{b}")
        ^^^ invalid syntax error 
rand takes only int character""" + Fore.RESET)
    if iscompl != 0:
        try:
            outputrand = random.randint(n, b)

        except:
            print(Fore.RED + "unknown error" + Fore.RESET)
            outputrand = "None"
        return outputrand
