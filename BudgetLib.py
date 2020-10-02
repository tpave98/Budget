# Function Lib for Tracking

#1 Fucntion to intake values:
    #take in float
    #take in category (Needs/Wants/Savings) and sub category (Rent,Income for x,etc)

class Entry:
    def _init_(self,cost,category,subcategory):
        self.cost = 0
        self.category = category
        self.subcategory = subcategory

def newEntry():
    entryCount +=1
    Cost = input("What is the cost?")
    Category = input("What category is this in?")
    Subcategory = input("What is the subcategory?")
    print("Entry #",entryCount,"\nCost: ",Cost,"\nCategory: ",Category,"\nSubcategory: ",Subcategory)
    entryConfirm = input("Is the above entry correct?")
    if (entryConfirm == "y" or entryConfirm == "Y"):
        EntryList.append( Entry(entryCount,Cost,Category,Subcategory) )


def displayEntries(list1):
    print("\n\nEntry #","  |  ","Cost","  |  ","Category","  |  ", "Subcategory")
        for obj in list1:   
            print(obj.num,"  |  ",obj.cost,"  |  ",obj.category,"  |  ",obj.subcategory)
        
