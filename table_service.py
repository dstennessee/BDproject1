from pymongo import MongoClient
import json            

client = MongoClient()								# connect to the server.
db = client.test	# returns an object pointing to the DB named "test".
collection = db.waiter
from GuinePig4 import update  #import the function created in GuinePig.py

with open('DocOrders.json') as file:
    file_data = json.load(file)
      

print("WELCOME")


def menu():        # main menu function
    print("1. Load Orders")
    print("2. Take Order")
    print("3. Show Menu")
    print("4. Review Orders")
    print("5. Cancle Order")
    print("6. Substute Order")
    print("0. Exit")

    
    
    try:
        option = int(input("what Can I Do For You?: ")) #if input here not an integer print exception
        return option
    except:
        print("I'm Sorry what was That?")
        return(-1)


def insert():   #for the insert function
 while(True):
   
        
    try:

        order = int(input('Order Number:')) # input set to integer, braek at 0
        if(order == 0):
            break
        tableNum = int(input('Table Number:'))# input set to integer, braek at 0
        if(tableNum == 0):
            break
        entree = input('Entree:') # input set to all  characters, braek at empty entry
        if(entree == ""):
            break
        enPrice = float(input('Entree Price:')) # input set float , braek at 99
        if(enPrice == 99):
            break
        bevrage = input('Bevrage:')  #input set to all  characters, braek at empty entry
        if(bevrage == ""):
            break
        bevPrice = float(input('Bevrage Price:')) # input set float , braek at 99
        if(bevPrice == 99):
            break

        result = collection.insert_one( #incert user input into document
                {
                "order_number" : order , 
                "table_number": tableNum, 
                "entree" : entree,
                "entree_price" : enPrice, 
                "bevrage" : bevrage, 
                "bevrage_price": bevPrice
            })
        
        print(result)
        break

    except: 
        print("I'm Sorry what was That?") 

        
def main():     #main function for cli menu


    while(True):
        optionSelected = menu()
        if(optionSelected == 0):
            break

        if(optionSelected == 1):    # Option 1 to Take an order
            print("What Can I Get You?...")
      
            if isinstance(file_data, list):
                collection.insert_many(file_data)  
            else:
                collection.insert_one(file_data)

        elif(optionSelected ==2):
            print("What Can I Get You?...")
            insert()
        elif(optionSelected == 3):    # Option 2 to Show the Resturant Menu
            print("Here is our menu...")
            print("""#######################################################################
Today's Special...............................4.99
(Ask Server for details) 

Ribeye Stake .................................6.99
(Served with mashed patatos)

Salmon Fillet.................................5.99
(Served with seasond rice)

Baked Chicken Brest...........................5.99
(Served with vegetables)

Cobb Salad....................................4.99

Bevrages

Iced Tea......................................1.99

Soda..........................................1.99

Beer..........................................5.99

###################################################################""")
        elif(optionSelected ==4):       # Option 3 to Review orders
            print("Here is What Was Orderd..")
            output = list(collection.find()) #to perform .find() operator

            for i in output: #for loop to display documents as a dictionary
                print("order_number:", i['order_number'])
                print("table_number:", i['table_number'])
                print("entree:", i['entree'])
                print("entree_price:",i['entree_price'])
                print("bevrage:", i['bevrage'])
                print("bevrage_price:", i['bevrage_price'])
                print()
            
        elif(optionSelected ==5):   # Cancle Orders
            while(True):
                try:
                    val= int(input("Cange your mind? Which order was This?"))
                    if(val == 0):
                        break     #the loop will search for document baed on user input and delete the document
                    result = collection.delete_one({"order_number": val})
                    print(result)   #set to search based on "order_number"
                    if(val >=1):
                        print("No Problem. Your order has been cancled")
                        break
                except:
                    print("It dosent look like you orderd this")
        elif(optionSelected ==6):
            print("What would you like to change?..")
            
            update() #calls to imported funtion
        
        else:
            print("I'm sorry what was that?...")

if __name__ == "__main__":
    main()
    

    
db = client.test
db = client["test"]

coll = db.waiter
coll = db["waiter"]

