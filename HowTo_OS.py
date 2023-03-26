
import os # built-in module

path = os.getcwd()
print(path)
os.chdir("C:\\Users\\rluec\\Documents")
print(os.getcwd())
os.chdir(path)
print(os.getcwd())
os.getcwd() == path

os.listdir()
os.listdir("C:\\")

os.mkdir("test")
os.listdir("test")

os.rename("test", "test-2")
os.listdir("test")  # error: cannot find path
os.listdir("test-2")

os.remove("test-2")  # error

path = os.path.join('C:','\\','Users','rluec','Desktop','NewDir')
print(path)
pathsplit = os.path.split(path) # only last?
print(pathsplit)

os.path.exists(path)
os.path.exists(pathsplit[0])

for roots, dirs, files in os.walk(path):
    print(roots, dirs, files)