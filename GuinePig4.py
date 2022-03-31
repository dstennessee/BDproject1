from pymongo import MongoClient

client = MongoClient()								# connect to the server.
db = client.test									# returns an object pointing to the DB named "test".
collection = db.waiter


def update():
    while(True):
        
        try:
        
            order = int(input('Order Number:'))
            if(order == 0):
                break
            tableNum = int(input('Table Number:'))
            if(tableNum == 0):
                break
            entree = input('Entree:')
            if(entree == ""):
                break
            enPrice = float(input('Entree Price:'))
            if(enPrice == 99):
                break
            bevrage = input('Bevrage:')
            if(bevrage == ""):
                break
            bevPrice = float(input('Bevrage Price:'))
            if(bevPrice == 99):
                break

            result = collection.update_one( 
                { "order_number" : order },

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
