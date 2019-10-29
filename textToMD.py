#!/usr/bin/env python3
# -*- coding: utf8 -*-


import sys,os,re


os.system("clear")
#os.system("last -w > ./resources/last.txt")

if len(sys.argv) == 2:
    parameter = sys.argv[1].lower()




with open("README.md", "r") as f:
    lines = f.readlines()

# régulière qui extrait : le login
def numberLines():
    with open("README_edited.md", "w") as f:
        i = 1
        for line in lines:
            # Find the lines that have at least one "@" in it.
            myRE = re.match(r'#',line)
            if myRE:
                f.write(line)
            else:
                if re.search(r'git', line):
                    j = str(i)
                    # take the part before "@" as a username
                    numberLines = re.split(r'[ ]{2,}', line, maxsplit=2)
                    if len(numberLines) == 2:
                        felech = re.search(r'--------->',numberLines[1])
                        if felech:
                            f.write(j+". "+'`'+numberLines[0]+'`'+"\t\t"+numberLines[1])
                            print(j+". ",numberLines[0])
                            i +=1
                        else:
                            print("111111111111111111111111111111111111111111111111111111111111111")
                            f.write(j+". "+'`'+numberLines[0]+'`'+"\t\t ---------->"+numberLines[1])
                            print(j+". ",numberLines[0])
                            i +=1

                    else:
                        f.write(j+". "+'`'+numberLines[0][:-1]+'`'+"\n")
                        print(j+". ",numberLines[0][:-1])
                        i +=1

                else:
                    # to print in the same line, I used "line[:-1]", to remove "\n" at the EOL
                    print("----------------------------------------")


numberLines()