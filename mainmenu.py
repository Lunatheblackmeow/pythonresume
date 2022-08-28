import textwrap as tr
from educationget import educationsearch
from workexp import workingexperience
from certifications import certsearch
import os

educationlist=[]
workexperiencelist=[]
certlist=[]

def clearscreen():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "mac" or os.name == "posix":
        os.system("clear")

def readfromfileeducation():
    with open("Textfiles/education.txt","r") as file:
        raw_lines = file.readlines()

        prep_linesforeducation = []
        readylinesforeducation = []

        for i in raw_lines:
            prep_linesforeducation.append(i.replace('\n',''))

        for pos, line in enumerate(prep_linesforeducation):
            if line not in readylinesforeducation:
                readylinesforeducation.append(prep_linesforeducation[pos].split(','))

        for row in readylinesforeducation:
            if row not in educationlist:
                educationlist.append(educationsearch(row[0],row[1],row[2]))

def readfromfileworkexp():
    with open("Textfiles/workexp.txt","r") as file:
        raw_lines = file.readlines()

        prep_linesforwork = []
        readylinesforwork = []

        for i in raw_lines:
            prep_linesforwork.append(i.replace('\n',''))

        for pos, line in enumerate(prep_linesforwork):
            if line not in readylinesforwork:
                readylinesforwork.append(prep_linesforwork[pos].split(','))

        for row in readylinesforwork:
            if row not in workexperiencelist:
                workexperiencelist.append(workingexperience(row[0],row[1],row[2]))

def readfromfilecert():
    with open("Textfiles/certs.txt","r") as file:
        raw_lines = file.readlines()

        prep_linesforcert = []
        readylinesforcert = []

        for i in raw_lines:
            prep_linesforcert.append(i.replace('\n',''))

        for pos, line in enumerate(prep_linesforcert):
            if line not in readylinesforcert:
                readylinesforcert.append(prep_linesforcert[pos].split(','))

        for row in readylinesforcert:
            if row not in certlist:
                certlist.append(certsearch(row[0],row[1],row[2]))


def scrolling(list):
    while userchoice != "m":
        print("Enter 'N' for Next Item, 'P' for Previous Item or 'M' for Main Menu:")
        userchoice = input("Please enter N/P/M : ").lower()
        if userchoice == 'n':
            count += 1
            if count == len(list):
                count = 0
        if userchoice == 'p':
            count -= 1
            if count < 0:
                count = 0
        if userchoice == 'm':
            mainmenu()


def mainmenu():
    clearscreen()
    print("******** Main Menu ********")
    print("1. About Myself")
    print("2. Education")
    print("3. Work Experiences")
    print("4. Other Certiications")
    x=input("Please input your selction: ")
    if x == "2":
        print(educationlist[0])
        count = 0
        userchoice = ""    
        while userchoice != "m":
            educationfun(educationlist[count])
            print("Enter 'N' for Next Item, 'P' for Previous Item or 'M' for Main Menu:")
            userchoice = input("Please enter N/P/M : ").lower()
            if userchoice == 'n':
                count += 1
                if count == len(educationlist):
                    count = 0
            if userchoice == 'p':
                count -= 1
                if count < 0:
                    count = 0
            if userchoice == 'm':
                mainmenu()
    if x == "3":
        print(workexperiencelist[0])
        count = 0
        userchoice = ""    
        while userchoice != "m":
            workexpfun(workexperiencelist[count])
            print("Enter 'N' for Next Item, 'P' for Previous Item or 'M' for Main Menu:")
            userchoice = input("Please enter N/P/M : ").lower()
            if userchoice == 'n':
                count += 1
                if count == len(workexperiencelist):
                    count = 0
            if userchoice == 'p':
                count -= 1
                if count < 0:
                    count = 0
            if userchoice == 'm':
                mainmenu()
    if x == "4":
        print(certlist[0])
        count = 0
        userchoice = ""    
        while userchoice != "m":
            certfun(certlist[count])
            print("Enter 'N' for Next Item, 'P' for Previous Item or 'M' for Main Menu:")
            userchoice = input("Please enter N/P/M : ").lower()
            if userchoice == 'n':
                count += 1
                if count == len(certlist):
                    count = 0
            if userchoice == 'p':
                count -= 1
                if count < 0:
                    count = 0
            if userchoice == 'm':
                mainmenu()

def educationfun(educationget:educationsearch):
    clearscreen()
    for index, item in enumerate(educationlist):
        if item == educationget:
            get_index = index + 1
    get_len = len (educationlist)
    text_test = tr.fill(educationget.getcourse(), width=55, subsequent_indent="\t\t")
    print("{:=^70s}".format(" Item {} of {} ".format(get_index,get_len)))
    print("{:15s} : {:55}".format("Name of Course", educationget.getcourse()))
    print("{:15s} : {:55}".format("School", educationget.getschool()))
    print("{:15s} : {:55}".format("Graduation  Year", educationget.getyear()))
    print("{0:=^70s}".format(""))

def workexpfun(workexp:workingexperience):
    clearscreen()
    for index, item in enumerate(workexperiencelist):
        if item == workexp:
            get_index = index + 1
    get_len = len (workexperiencelist)
    text_test = tr.fill(workexp.getcompanyname(), width=55, subsequent_indent="\t\t")
    print("{:=^70s}".format(" Item {} of {} ".format(get_index,get_len)))
    print("{:15s} : {:55}".format("Name of Company", workexp.getcompanyname()))
    print("{:15s} : {:55}".format("Role", workexp.getrole()))
    print("{:15s} : {:55}".format("Duration", workexp.getduration()))
    print("{0:=^70s}".format(""))

def certfun(certifications:certsearch):
    clearscreen()
    for index, item in enumerate(certlist):
        if item == certifications:
            get_index = index + 1
    get_len = len (certlist)
    text_test = tr.fill(certifications.getcertname(), width=55, subsequent_indent="\t\t")
    print("{:=^70s}".format(" Item {} of {} ".format(get_index,get_len)))
    print("{:15s} : {:55}".format("Name of Certification", certifications.getcertname()))
    print("{:15s} : {:55}".format("Certification From", certifications.getcertschool()))
    print("{:15s} : {:55}".format("Date of Certification", certifications.getcertyear()))
    print("{0:=^70s}".format(""))

readfromfileeducation()
readfromfileworkexp()
readfromfilecert()
mainmenu()