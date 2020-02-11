'''
# environment variable, control os related resources such as directory and file etc
import os
print(os.environ)
print(os.environ['PATH'])

# change current directory
# os.chdir("C:\WINDOWS")

# get current directory
print(os.getcwd())

# execute system command from python
print(os.system("dir"))

# get return value from system command
f = os.popen("dir")  # it return type of file
print(type(f))

print(f.read()) # how to read above file object

# os.mkdir : create directory
# os.rmdir: delete directory
# os.unlink: delete file
# os.rename(src, dst): rename file
# shutil: copy file
'''