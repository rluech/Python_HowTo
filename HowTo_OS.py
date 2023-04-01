# https://docs.python.org/3.9/library/os.path.html#os.path.split

import os  # python built-in module, see pathlib as alternative.

# working directory
path = os.getcwd()                       # current working directory 'cwd'
os.chdir("C:\\Users\\rluec\\Documents")  # change cwd
os.chdir(path)                           # ... and back

# create
os.listdir()
os.listdir("C:\\")
os.mkdir("test")
os.listdir("test")
os.rename("test", "test-2")
os.listdir("test")  # error: cannot find path
os.listdir("test-2")
os.remove("test-2")  # PermissionError: Schreibgeschützt auf Windows

# partitioning
os.path.basename(path)  # last part
os.path.dirname(path)   # path without last part
os.path.split(path)     # tuple(dirname(), basename())
os.path.splitdrive(path)
path.split('\\')        # string split into all parts
os.path.join('C:','\\','Users','rluec','Desktop')

# info
os.path.exists(path)
os.path.isfile(path)
os.path.isdir(path)
os.path.getmtime(path)  # last modification time in seconds since epohe
os.path.getctime(path)  # ctime, see documentation
os.path.getsize(path)   # file size

# safety
os.path.normcase("C:/Users\\rluec/PycharmProjects")  # normalize path
os.path.realpath(path)  # canonical path eliminating any symbolic links

for roots, dirs, files in os.walk(path):
    print(roots, dirs, files)

# path of this script (works not interactively):
# os.path.dirname(os.path.realpath(__file__))  
