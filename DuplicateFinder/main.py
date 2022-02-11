import os
import shutil

duplicatepath = ""


def finder():
    directory = input("Give the directory: ")
    xlist = os.listdir(directory)
    foldercreator(directory)
    for files in xlist:
        if "Copy" in files:
            mover(directory, files)
        else:
            for counter in range(10):
                buffer = "(" + str(counter) + ")"
                if buffer in files:
                    mover(directory, files)


def foldercreator(directory):
    xlist = os.listdir(directory)
    global duplicatepath
    duplicatepath = os.path.join(directory, "duplicate")
    if "duplicate" not in xlist:
        os.mkdir(duplicatepath)


def mover(directory, file):
    xlist = os.listdir(duplicatepath)
    if file not in xlist:
        shutil.move(directory + "\\" + file, duplicatepath)


finder()
