isinterupterror = 0

import keyboard
import os
import time
import sys

curpath = os.getcwd().split("\\")

module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, module_path)

import commands.charge.charge as charge


def cls():
    os.system("cls")


try:
    boot = os.listdir("boot\\")
except:
    os.chdir("..")
    boot = os.listdir("boot\\")

for i in range(20):
    if keyboard.is_pressed("F2"):
        cls()
        os.system("python bios\\bios.py")
        break
    elif keyboard.is_pressed("F12"):
        cls()
        while True:
            try:
                cls()
                print(boot)
                crboot = int(input("which your boot file is if the first write (1)\n"))
                crboot = crboot - 1
                break
            except:
                continue
        try:
            with open("startfile/bootsave/crboot.txt", "w") as f:
                f.write(boot[crboot])
                f.flush()
                cls()
                charge.reboot()
        except FileNotFoundError:
            with open("startfile/bootsave/crboot.txt", "w", encoding="utf-8") as f:
                f.write("")
                f.flush()
                cls()
                charge.reboot()
        charge.reboot()
    else:
        pass
    time.sleep(0.1)

with open("startfile\\bootsave\\crboot.txt", "r") as f:
    runboot = f.read()

if runboot == "":
    input("""\a\nsystem cannot find boot file
press enter to restart
when restarted press F12 to change boot file""")
    charge.reboot()
try:
    os.system("python " + "boot\\" + runboot)
except KeyboardInterrupt:
    while True:
        try:
            cls()
            os.system("python " + "boot\\" + runboot)
        except KeyboardInterrupt:
            continue

except Exception as fe:
    cls()
    os.system("python " + "boot\\" + runboot)
input("END BOOT FILE")
cls()
charge.reboot()
