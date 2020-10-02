# budgeting tool
import csv
entryCount = 0
myFile = "./BudgetLog.csv"

class Entry:
    def __init__(self,num,cost,category,subcategory):
        self.num = num
        self.cost = cost
        self.category = category
        self.subcategory = subcategory
        #add date category and potentially other
EntryList = []
      
Operation = input("Select an option from the menu: \nA: New Entry \nB: View Entries \n(add more options later)\n")


# Must add load/store functionality from some file type, either csv or text, csv is probably better

# 

# Category total function: adds all of the costs in a category
def totalCategory(categoryName,myList):
    total = 0
    for obj in myList:
        if obj.category == categoryName:
            total += obj.cost
        else:
            continue
    return total   

# View function: Prints the data stored in the entry list
def viewEntries(myList):        
        print("\n\n{:^20} | {:^20} | {:^20} | {:^20}".format("Entry #","Cost","Category","Subcategory")) #","  |  ","Cost","  |  ","Category","  |  ", "Subcategory")
        print("______________________________________________________________________________________")
        file = open(myFile,"r")
        for line in file:          # update for csv use
            line = line.strip()
            print(line)
#        for obj in myList:   
#          print("{:^20} | ${:^19} | {:^20} | {:^20}".format(obj.num,obj.cost,obj.category,obj.subcategory))
            #print(obj.num,"  |  ",obj.cost,"  |  ",obj.category,"  |  ",obj.subcategory)
        file.close
 
# daily spending function
# remaining balance function
# plot data function


if (Operation == 'a' or Operation == 'A'):

# Basis for newEntry() function
    
    entryCount +=1 # updating entries for purpose of 
    Cost = input("What is the cost?") # could be consolidated to fewer prompts in , seperated entries
    Category = input("What category is this in?") 
    Subcategory = input("What is the subcategory?")
    print("Entry #",entryCount,"\nCost: ",Cost,"\nCategory: ",Category,"\nSubcategory: ",Subcategory)
    entryConfirm = input("Is the above entry correct?") # add error checking later for type inputs 
    if (entryConfirm == "y" or entryConfirm == "Y"):
        EntryList.append( Entry(entryCount,Cost,Category,Subcategory) ) # adds entry to list
        #file = open(myFile, "a")
        #for obj in EntryList:
        #    file.write("\n{:^20} | ${:^19} | {:^20} | {:^20}".format(obj.num,obj.cost,obj.category,obj.subcategory))
        #file.close()
        with open(myFile, "w") as csvFile:
            csvWrite = csv.writer(csvFile, delimiter=',')
            for obj in EntryList:
                templist = [obj.num,obj.cost,obj.category,obj.subcategory]
                csvWrite.writerow(templist)
        #viewEntries(EntryList)
        


        