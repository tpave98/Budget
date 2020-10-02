# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 12:01:05 2020

@author: Thomas
"""

# budgeting tool
import csv

class Transaction:
    def __init__(self,date,description,comments,checkNumber,amount,balance,category,subcategory):
        self.date = date
        self.description = description
        self.comments = comments
        self.checkNumber = checkNumber
        self.amount = amount
        self.balance = balance
        self.category = category
        self.subcategory = subcategory
        
####################################### FUNCTION DEFS ###########################################################
        
# SELECTING START AND END OF PART OF STRING TO PRINT: takes in string and outputs corrected string based on start and end characters
def selective_str(myString):
    if (myString.find('>') > 0): # only runs if the start character is found in the string
        myString = myString[(myString.find('>')+1):] # sets the string back ingto 
        myString = myString[:myString.find('<')]
    return myString

# TAKES INPUT OF STRING AND STARTING AND ENDING CHARS AND OUTPUTS THE STRING AS A BETWEEN THE FIRST INSTANCE OF startCh and first instance of the endCh
def selective_str2(myString,startCh,endCh):
    if (myString.find(startCh) > 0): # only runs if the start character is found in the string
        myString = myString[(myString.find(startCh)+1):] # sets the string back ingto 
        myString = myString[:myString.find(endCh)]
    return myString

# CONVERTS FORMAT OF NUMBERS SO THEY MAY BE CONVERTED TO FLOATS FOR CALCULATIONS
def format_for_float_conv(myString):
    myString = myString.replace(",","")
    myString = myString.replace("(","-")
    myString = myString.replace(")","")
    myString = myString.replace("$","")
#    if myString[0] == "(":
#        myString = "-" + selective_str2(myString,"$",")")
#    else:
#        myString = myString[1:]
    return myString
        
        
# READING CSV ENTRIES INTO OBJECT LIST: Takes in file name and stores variables in class and objs in a list
def read_LMCU_CSV_2_Obj_List(CSVFILE):
    objList = []
    with open(CSVFILE, "r") as csvFile:
        csvRead = csv.reader(csvFile)
        next(csvRead)
        for row in csvRead:
            objList.append(Transaction(row[0],selective_str(row[1]),row[2],row[3],float(format_for_float_conv(row[4])),float(format_for_float_conv(row[5])),"",""))
    csvFile.close
    return objList

# PRINTING CSV ENTRIES LOADED INTO OBJECT LIST:
def print_Obj_List(objList):
    for obj in objList:
        print("{:^15} | {:^50} | {:^10} | {:^12} | {:^12} | {:^15}".format(obj.date,obj.description,obj.comments,obj.checkNumber,obj.amount,obj.balance))
                
def assign_category(objList):
    for obj in objList:
        while obj.category == "":
            print("\n\n{:^15} | {:^50} | {:^10} | {:^12} | {:^12} | {:^15}".format(obj.date,obj.description,obj.comments,obj.checkNumber,obj.amount,obj.balance))
            catAssign = input("What category should this be assigned to?\nN: NEEDS\nW: WANTS\nS: SAVINGS\n")
            if catAssign == "N" or catAssign == "n":
                obj.category = "NEEDS"
            elif catAssign == "W" or catAssign == "w":
                obj.category = "WANTS"
            elif catAssign == "S" or catAssign == "s":
                obj.category = "SAVINGS"
            else:
                obj.category = ""
            while obj.subcategory == "":
                print("{:^15} | {:^8} | {:^12} | {:^50} | {:^12} | {:^15}".format(obj.date,obj.category,obj.subcategory,obj.description,obj.amount,obj.balance))
                obj.subcategory = input("What subcategory should this be assigned to?")
                print("{:^15} | {:^8} | {:^12} | {:^50} | {:^12} | {:^15}".format(obj.date,obj.category,obj.subcategory,obj.description,obj.amount,obj.balance))

def assignMainCat(objList):
    for obj in objList:
        if obj.subcategory != "":
            if obj.subcategory in ["Rent","Internet Bill","Electric Bill","Gas Bill","Water Bill","Car Insurance","Renters Insurance","Groceries","Gas (for car)","Haircut"]:
                obj.category = "Monthly Bills (Needs)"
            elif obj.subcategory in ["Resturants","Entertainment","Whatevers not planned","Projects","Gifting","Electronics/Games","Clothes","Tools","Subscriptions","Gym Membership","Other"]:
                obj.category = "Everyday Expenses (Wants)"
            elif obj.subcategory in ["Rainy Day Fund","Car Replacement","Roth Contribution","Car Expenses","Health Spending"]:
                obj.category = "Savings"
            
            
# SORTS THE MAIN CATEGORIES INTO LISTS FOR EASIER OPERATION 
def sort_category(objList):
    NEEDS = []
    WANTS = []
    SAVINGS = []
    for obj in objList:
        if obj.category == "NEEDS":
            NEEDS.append(obj)
        elif obj.category == "WANTS":
            WANTS.append(obj)
        elif obj.category == "SAVINGS":
            SAVINGS.append(obj)
        else:
            print("\n{:^15} | {:^8} | {:^12} | {:^50} | {:^12} | {:^15}".format(obj.date,obj.category,obj.subcategory,obj.description,obj.amount,obj.balance))
            catAssign = input("What category should this be assigned to?\nN: NEEDS\nW: WANTS\nS: SAVINGS\n")
            if catAssign == "N" or catAssign == "n":
                obj.category = "NEEDS"
            elif catAssign == "W" or catAssign == "w":
                obj.category = "WANTS"
            elif catAssign == "S" or catAssign == "s":
                obj.category = "SAVINGS"
    
    return NEEDS,WANTS,SAVINGS
            
def display_category():
    print("\n\n")
    for obj in NEEDS:
        print("{:^15} | {:^8} | {:^12} | {:^50} | {:^12} | {:^15}".format(obj.date,obj.category,obj.subcategory,obj.description,obj.amount,obj.balance))
    print("\n\n")
    for obj in WANTS:
        print("{:^15} | {:^8} | {:^12} | {:^50} | {:^12} | {:^15}".format(obj.date,obj.category,obj.subcategory,obj.description,obj.amount,obj.balance))
    print("\n\n")
    for obj in SAVINGS:
        print("{:^15} | {:^8} | {:^12} | {:^50} | {:^12} | {:^15}".format(obj.date,obj.category,obj.subcategory,obj.description,obj.amount,obj.balance))

# WRITING CATEGORIZED LIST TO THE SAVE FILE        
def write_2_new_CSV(objList):
    CSVFILE = "./CategroizedCSV.csv"
    with open(CSVFILE, "w",newline = '') as csvFile:
        csvWrite = csv.writer(csvFile,dialect = "excel")
        for obj in objList:
            csvWrite.writerow([obj.date,obj.description,obj.amount,obj.balance,obj.category,obj.subcategory])
    csvFile.close

# Load the most recently saved statement with categorizations included
def load_stored_CSV_2_Obj_List(CSVFILE): 
    objList = []
    with open(CSVFILE, "r") as csvFile:
        csvRead = csv.reader(csvFile)
        for row in csvRead: #fix so that Transaction doesnt have check # and comment parameters to reduce size?
            objList.append(Transaction(row[0],selective_str(row[1]),row[2],row[3],float(format_for_float_conv(row[4])),float(format_for_float_conv(row[5])),"",""))
    csvFile.close
    return objList

def load_Categories(txtFile):
    categoryList = []
    textFile = open(txtFile, "r")
    for row in textFile:
        categoryList.append(row.replace("\n",""))
    textFile.close
    return categoryList
        
####################################### END FUNCTION DEFS ###########################################################



####################################### MAIN PROGRAM ################################################################


myFile = "./export_20200914.csv"     
transactionList = read_LMCU_CSV_2_Obj_List(myFile)
print_Obj_List(transactionList) # Reads the csv and prints the values in a table after they are stored in a object list
assign_category(transactionList)

NEEDS,WANTS,SAVINGS = sort_category(transactionList)
display_category()
write_2_new_CSV(transactionList)
