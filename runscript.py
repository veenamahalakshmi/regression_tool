from flask import session

import zipfile,fnmatch,os

import colorama
from colorama import Fore
colorama.init(autoreset=True)

import os, shutil, re, glob
from os.path import isfile, join
from os import walk

from pyth import pvalue

# def create_dir(rootpath):
#     os.chdir("E:")
#     cwd=os.getcwd()
#     print(cwd)
#     name=session['uname']
#     rootpath=cwd+session['uname']
#     print "The current working director is" +cwd
#     if(os.path.exists(rootpath)):
#          shutil.rmtree(rootpath,True)
#     os.mkdir(rootpath)
#     print"created new directory" + rootpath
#     return








def running_script(rootPath):
    cwd=os.getcwd()
    print(cwd)
    uname=session['uname']
    rootPath=cwd + uname
    pvalue = 10



    pattern = '*.zip'
    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, pattern):
            #print(os.path.join(root, filename))
            zipfile.ZipFile(os.path.join(root, filename)).extractall(os.path.join(root, os.path.splitext(filename)[0]))


        os.chdir(rootPath)
        for file in glob.glob(pattern):
            temp = file.rsplit(".", 1)[0]
            #print (">>>", temp)
            f = open((file.rsplit(".", 1)[0]) + "_ANA.txt", "w")


            f.close()
    pvalue=30

    ##here folder output
    mypath =r'c:\\test'
    newpath = os.path.expanduser(mypath)
    # filenam = "1.txt"

    f = []
    path = ''
    path1 = []

    for (dirpath, dirnames, filenames) in walk(mypath):
        if isfile(join(mypath, dirpath)):
            path1.extend(join(mypath, dirpath))
        if os.path.isdir(join(mypath, dirpath)):
            for f in filenames:
                path1.append(str(join(mypath, dirpath, f)))
    print(path1)
    pvalue=40
    # newf = open(os.path.join(newpath, filenam ), "w+")



    myarray = {"ERROR", "error"}
    for element in myarray:
        elementstring = ''.join(element)


    for f in path1:
        openfile = open(os.path.join(path, f), "r")
        t1 = re.match(".*(TC(\d)+.*)\\\\.*", f)
        if t1 is not None:
            l1 = t1.group(0).split('\\')
            of = open(l1[3] + "_ANA.txt", "a+")
            of.write("*****************************************************************************************************************************************************" + "\n")
            F = f.upper()
            of.write(F + "\n")
            for line in openfile:
                if elementstring in line:
                    of.write(line)
            of.write("\n\n\n")
            of.close()
        else:
            print ("regex not matched")
            print(Fore.GREEN + "**********" + "Script Completed" + "**********" + "\n")
            print(Fore.GREEN + "**********" + "Summary File Generated" + "**********")

    # newf.close()
    openfile.close()
    print ("Completed Runscript...")
    pvalue=50
    return True
#running_script("C:\\test")
