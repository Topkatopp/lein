import os
from commands.filesys.helptofilesys.text import *

def makedir(path):
        try:
                os.mkdir(path)
                return ""
        except:
                return "error cannot make dir: " + path
def cdir(path):
        try:
                os.chdir(path)
                return ""
        except:
                return "error cannot join to the directory: " + path

def removedir(path):
        try:
                os.rmdir(path)
                return ""
        except:
                return "error cannot delete directory: " + path

def directorylist():
        result = ''
        directory_path = os.getcwd()
        files = os.listdir(directory_path)
        for file in files:
                file_path = os.path.join(directory_path, file)
                if os.path.isfile(file_path):
                        if file.endswith('.cs'):
                                result += f'{file} <C# file>\n'
                        elif file.endswith('.py'):
                                result += f'{file} <python file>\n'
                        else:
                                result += f'{file} <{file[file.find("."):]} file>\n'
                elif os.path.isdir(file_path):
                        result += f'{file} <directory>\n'
        return result


def mkfile(name, what):
        with open(name, "w") as f:
                f.write(what)

def rmfile(name):
        try:
                os.remove(name)
                return ""
        except:
                return "error the file: " + name + " is not real file"

def readfile(name):
        try:
                with open(name, "r") as f:
                        result = f.read()
                return Fore.BLUE + result + Fore.RESET
        except:
                return Fore.RED + "error the file: " + name + " is not real file" + Fore.RESET
