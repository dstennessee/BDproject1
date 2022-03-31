from pymongo import MongoClient                  #this was made as an import to run as a funtion in the main .py file

client = MongoClient()								# connect to the server.
db = client.test									# returns an object pointing to the DB named "test".
collection = db.waiter


def update():
    while(True):
        
        try:
        
            order = int(input('Order Number:')) # input set to integer, braek at 0
            if(order == 0):
                break
            tableNum = int(input('Table Number:')) # input set to integer, braek at 0
            if(tableNum == 0):
                break
            entree = input('Entree:') # input set to all  characters, braek at empty entry
            if(entree == ""):
                break
            enPrice = float(input('Entree Price:')) # input set float , braek at 99
            if(enPrice == 99):
                break
            bevrage = input('Bevrage:') # input set to all  characters, braek at empty entry
            if(bevrage == ""):
                break
            bevPrice = float(input('Bevrage Price:')) # input set float , braek at 99
            if(bevPrice == 99):
                break

            result = collection.update_one(     #result will run the .update function 
                { "order_number" : order },     #and will set incert values based on user input

                { "$set": {"table_number": tableNum, 
                    "entree" : entree,
                    "entree_price" : enPrice, 
                    "bevrage" : bevrage, 
                    "bevrage_price": bevPrice}
                })
            print(result)
            break
            
        except Exception as e: 
            print("I'm Sorry what was That?")
            print(e)

        

        

if __name__ == "__main__":
    update()
