import os
import shutil

def shorting_algorithm():
    directory = input("Give the directory you want to search.")
    name = input("Give the name of you files you want to move.")
    newdir = input("Give the new directory.")
    xlist = os.listdir(directory)
    
    
    for files in xlist:
        if name in files:
            shutil.move(directory + '\\' + files,newdir)
                 
                 
shorting_algorithm()
