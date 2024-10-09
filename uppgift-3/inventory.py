import csv
from msvcrt import getwch

class Product:

    def __init__(self, file_name):
        self.file_name = file_name
    
    def add_item(self):
        max_id_product = max(products, key=lambda id: id["id"])
        max_id = max_id_product["id"]
        new_id = max_id + 1
        print("New ID: ", new_id)
        

        name = input("Name of the product: ")
        desc = input("Description of the product: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        add_to_dictionary(new_id, name, desc, price, quantity)
    
    def remove_item(self, product_list):
        id = int(input("Vilken produkt vill du ta bort? (id): "))
        for product in products:
            if product["id"] == id:
                product_list.remove(product) 
                print(f"Produkten {id} har tagits bort.")
    
    def edit_item(self, products):
        id = int(input("Vilken produkt vill du ändra? (id): "))
        name = input("Namn på produkten: ")
        desc = input("Beskrivning på produkten: ")
        price = float(input("Pris på produkten: "))
        quantity = int(input("Antal produkter: "))
        for product in products:
            if product["id"] == id:
                product["name"] = name
                product["desc"] = desc
                product["price"] = price
                product["quantity"] = quantity

    def check_inventory(self):
        for product in products:
            print(f"Product: ({product['id']}) {product['name']} \t {product['desc']} \t {product['price']} \t {product['quantity']}")

    def import_items(self):
        with open(self.file_name, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                id = int(row["id"])
                name = str(row["name"])
                desc = str(row["desc"])
                price = float(row["price"])
                quantity = int(row["quantity"])
            
                add_to_dictionary(id, name, desc, price, quantity)

    def save_items(self):
        with open(self.file_name, "w", newline="") as file:
            fieldnames = ["id", "name", "desc", "price", "quantity"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            
            for row in products:
                writer.writerow(row)  


def add_to_dictionary(id, name, desc, price, quantity):
    products.append(
        {
            "id": id,
            "name": name,
            "desc": desc,
            "price": price,
            "quantity": quantity
        }
    )

def actions(product, product_list):
    print("L = Lägga till, T = Ta bort, Ä = Ändra, Q = Avsluta")
    key_pressed = getwch().upper()
    match key_pressed:
        case "L":
            product.add_item()
        case "T":
            product.remove_item(product_list)
        case "Ä":
            product.edit_item(product_list)
        case "Q":
            product.save_items()
            quit()
    
    product.check_inventory()
    

products = []
product = Product("./db_products.csv")
product.import_items()
product.check_inventory()

while True:
    actions(product, products)