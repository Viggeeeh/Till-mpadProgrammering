import csv

class Product:

    def __init__(self, file_name):
        self.file_name = file_name
    
    def add_item(self):
        id = 0
        for count in products:
            id += 1

        name = input("Name of the product: ")
        desc = input("Description of the product: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        add_to_dictionary(id, name, desc, price, quantity)
    
    def remove_item(self):
        id = int(input("Which product do you want to remove? (by id): "))
        products.pop(id)

    def check_inventory(self):
        for product in products:
            print(f"Product: ({product['id']}) {product['name']} \t {product['desc']} \t {product['price']}")

    def import_items(self):
        with open(self.file_name, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                id = int(row["id"])
                name = row["name"]
                desc = row["desc"]
                price = float(row["price"])
                quantity = int(row["quantity"])
            
                add_to_dictionary(id, name, desc, price, quantity)

    def save_items(self):
        with open(self.file_name, "w") as file:
            fieldnames = products[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
    
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
    

products = []
product = Product("./db_products.csv")
product.import_items()
product.check_inventory()
product.add_item()
product.check_inventory()
product.remove_item()
product.check_inventory()
product.save_items()


       
    #TODO: Skapa check_inventory (visa produkter)
    #TODO: Skapa add_item-metod för produkter
    #TODO: Skapa remove-metod för produkter
    #TODO: Skapa sparfunktion
    #TODO: (Frivillig) Skapa en metod som visar mest sålda produkt