#STAR
from collections import Counter
from datetime import datetime, timedelta
import random
from datetime import datetime, timedelta





#soroosh Talebi

def is_discounted(expiration_date): 
    today = datetime.today().date() 
    difference = expiration_date - today 
    if difference <= timedelta(days=7): 
        return True 
    return False 

mahsoulat = ["kode mahsoul khod ra vared konid0", "0 shir", "1 mast", "2 dogh", "3 kareh", "4 chips", "5 pofak", "6 keranchi", 
             "7 chipof", "8 biscouit", "9 shirkakou", "10 bastani", "11 kaick", "12 saladsezar"] 
ghimat = [0, 15000, 20000, 25000, 10000, 5000, 2000, 8000, 9000, 10000, 12000, 15000, 11000, 327000] 
kodekala = ["0", "Codekala1", "Codekala2", "Codekala2", "Codekala4", "Codekala15", "Codekala6", "Codekala7", "Codekala8", 
            "Codekala9", "Codekala10", "Codekala11", "Codekala12", "codekala13"] 
tarikhTolid = ["", "2023-8-28", "2023-8-28", "2023-8-28", "2023-8-28", "2023-8-28", "2023-8-28", "2023-8-28", 
               "2023-8-28", "2023-8-28", "2023-8-28", "2023-8-28", "2023-8-28", "2023-8-28"] 
tarikhEngeza = ["", "2023-9-17", "2023-9-17", "2023-9-17", "2023-9-18", "2023-9-18", "2023-9-19", "2023-9-24", 
                "2023-9-19", "2023-9-19", "2023-9-20", "2023-9-20", "2023-9-21", "2023-8-30"] 
info = [(m, g, k, datetime.strptime(td, "%Y-%m-%d"), datetime.strptime(ed, "%Y-%m-%d")) for m, g, k, td, ed in 
        zip(mahsoulat, ghimat, kodekala, tarikhTolid, tarikhEngeza) if td != "" and ed != "__"] 
sabad = [] 

# Get user information
esm = input("Enter your name: ")
phonenumber = input("Enter your phone number: ")
adrees = input("Enter your address: ")
#soroosh
while True: 
    print("Enter the product code to buy:\nEnter 'end' to finish:\nEnter 'off' to see discounted products") 
    print(mahsoulat)
    k = input("    ") 
     
    if k == "off": 
        discounted_products = [] 
        for item in info: 
            name, price, code, tolid_date, engeza_date = item 
            if is_discounted(engeza_date.date()): 
                discounted_products.append(item) 
                print(f"{name} is currently discounted for {price * 0.9}") 
 
        if not discounted_products: 
            print("There are no discounted products at the moment") 
 
    elif k == "end": 
        sum_ghimat = sum([item[1] for item in sabad]) 
        sum_mahsoulat = len(sabad) 
        print("Total price:", sum_ghimat) 
        print("Number of items:", sum_mahsoulat) 
        print("Production date:") 
        for item in sabad: 
            print(item[3].strftime("%Y-%m-%d")) 
        print("Expiration date:") 
        for item in sabad: 
            print(item[4].strftime("%Y-%m-%d")) 
        break 
 
    else: 
        k = int(k) 
        name, price, code, tolid_date, engeza_date = info[k] 
        if is_discounted(engeza_date.date()): 
            print(f"{name} is currently discounted") 
            price *= 0.9 
            print(f"Price of {name} with discount: {price}") 
        else: 
            sabad.append(info[k]) 
            print(f"{name} is not discounted")


#Reyhane ardestani
if sabad:
    top_product = Counter([item[0] for item in sabad]).most_common(1)[0]  
    print("Most purchased item:", top_product[0])
else:
    print("No items were purchased.")


#Reyhane ardestani

# Write output to file
with open("output.txt", "a") as f: 
    print("Total price:", sum_ghimat, file=f) 
    print("Address:", adrees, file=f) 
    print("Name:", esm, file=f) 
    print("Phone number:", phonenumber, file=f) 
    if sabad:
        print("Most purchased item:", top_product[0], file=f)
    else:
        print("No items were purchased.", file=f)
        


 











#Reyhane ardestani

def add_item(code, name, price, quantity):


    mahsoulat[code] = {'name': name, 'price': price, 'quantity': quantity}


def remove_item(code):
    del mahsoulat[code]


def update_quantity(code, quantity):
    mahsoulat[code]['quantity'] = quantity
orders = []

#Reyhane ardestani

def place_order(customer_name, item_code, quantity, order_date, delivery_date, price, amount_paid):
    order = {'customer_name': customer_name, 'item_code': item_code,
    'quantity': quantity, 'order_date': order_date,
    'delivery_date': delivery_date, 'price': price,
    'amount_paid': amount_paid}
    orders.append(order)


def list_orders():
    for order in orders:
        print(order)


def remove_order(order):
    orders.remove(order)


def update_order_status(order, status):


    order['status'] = status
stores = []


def add_store(name, address):
    store = {
    'name': name, 'address': address,
    'orders_delivered': 0, 'orders_requested': 0,
    'debt': 0}
    stores.append(store)


def remove_store(store): stores.remove(store)


def update_store_info(store, orders_delivered, orders_requested, debt):


    store['orders_delivered'] = orders_delivered ,store['orders_requested'] = orders_requested
    store['debt'] = debt

#Reyhane ardestani

sum_ghimat = sum([item[1] for item in sabad])
sum_mahsoulat = len(sabad)
print("ghimat:", sum_ghimat)
print("tedad mahsoulat", sum_mahsoulat)
print(mahsoulat)





#random
#soroosh talebi
random_number = random.randint(1, 1000)



with open("output.txt", "r") as f: 
    previous_data = f.readlines() 
 
# Extract product information from order history file 
products = [] 
for line in previous_data: 
    if "Expiration date:" in line: 
        product_info = line.split(" - ") 
        product_name = product_info[0].strip() 
        products.append(product_name) 
 
# Analyze sales 
#reyhane ardestani
if products: 
    top_product = Counter(products).most_common(1)[0] 
    print("Most purchased item:", top_product[0]) 
else: 
    print("No items were purchased.")




#soroosh talebi

with open("output.txt", "a") as f:
    print("GHIMAT KOL:", sum_ghimat, file=f,)
    print("adress  :   ",adrees, file=f)
    print("name  :   ",esm, file=f)
    print("phonenumber  :   ",phonenumber, file=f)
    print(" mahboub tarin kala khridari shode ", top_product[0],file=f)




    for item in sabad:

        if is_discounted(item[4].date()):
            print(f"{item[0]} - TARIKH ENGEZA: {item[4].strftime('%Y-%m-%d')} - GHIMAT BA TAKHFIF: {item[1] * 0.9}", file=f)
        else:
            print(f"{item[0]} - TARIKH ENGEZA: {item[4].strftime('%Y-%m-%d')} - GHIMAT: {item[1]}", file=f)
    
    print("_______________________________________________________________________________________________________________", file=f)
    print("code sefaresh",random_number, file=f)  
    print("________________________________________________________________________________________________________________",file=f)
# باز کردن فایل سابقه سفارشات



#soroosh talebi
with open("output.txt", "r") as f:
    previous_data = f.readlines()

# استخراج اطلاعات محصولات از فایل سابقه سفارشات
products = []
for line in previous_data:
    if "TARIKH ENGEZA" in line:
        product_info = line.split(" - ")
        product_name = product_info[0].strip()
        products.append(product_name)

# تحلیل فروش
top_product = Counter(products).most_common(1)[0]

# نمایش محصول برتر خریداری شده
j=print(" mahboub tarin kala khridari shode ", top_product[0])

#reyhane ardestani 

if sum_ghimat>=20000000:
    print("bedehi shoma bish az saghf  mojaz ast , saghf kharid to 2000000 ast \n ba Tashakor")
else:
    print("merci az kharid")



