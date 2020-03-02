import os
import shutil

print("nowDir:",os.getcwd())
saveroot = os.getcwd()
os.chdir('..')
print("changeDir:",os.getcwd())
roots = os.getcwd()
for files in os.listdir():
    if os.path.isfile(files):
        print("copyfile:",files)
        shutil.copy(os.path.join(roots,files),os.path.join(saveroot,files))
