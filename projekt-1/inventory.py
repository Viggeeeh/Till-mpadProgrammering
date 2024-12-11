# INVENTORY.PY: Här är hela programmet

# __author__  = "Viggo Öfors"
# __version__ = "1.0.0"
# __email__   = "viggo.ofors@elev.ga.ntig.se"

from msvcrt import getwch
from pynput import keyboard
from colors import Color
import csv
import os

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
        while True:
            try:
                price = float(input("Price: "))
                break
            except:
                print(f"{Color.RED}Error! {Color.DEFAULT}Price has to be a number. \n")
        while True:
            try:
                quantity = int(input("Quantity: "))
                break
            except:
                print(f"{Color.RED}Error! {Color.DEFAULT} Quantity has to be a number. \n")

        add_to_dictionary(new_id, name, desc, price, quantity)
    
    def remove_item(self, product_list, current_selected_index):
        product = product_list[current_selected_index]
        product_list.remove(product)
        print(f"Produkten {product['id']} har tagits bort.")
    
    def edit_item(self, products, current_selected_index):
        product = products[current_selected_index] 
        
        print(f"Redigerar produkt: {product['name']}")

        name = input("Namn på produkten: ")
        desc = input("Beskrivning på produkten: ")
        while True:
            try:
                price = float(input("Pris: "))
                break
            except ValueError:
                print(f"{Color.RED}Error! {Color.DEFAULT}Pris måste vara ett nummer. \n")
        while True:
            try:
                quantity = int(input("Antal: "))
                break
            except ValueError:
                print(f"{Color.RED}Error! {Color.DEFAULT}Antal måste vara ett nummer. \n")

        product["name"] = name
        product["desc"] = desc
        product["price"] = price
        product["quantity"] = quantity

        print(f"{Color.GREEN}Produkten har uppdaterats!{Color.DEFAULT}")

    def check_inventory(self, current_selected_index):
        os.system("cls")
        print("""
=========================================================================================================
| ID  | Name                   | Description                                    | Price      | Quantity |
=========================================================================================================""")
        # Loopar igenom produkterna
        for product in products:
            # Hanterar längden på produkterna så att de inte blir för långa
            product_name = product["name"][:20] + "..." if len(product["name"]) > 23 else product["name"]
            product_desc = product["desc"][:43] + "..." if len(product["desc"]) > 46 else product["desc"]
            
            # Om produkten är markerad, stryk över med gult
            if product["name"] == products[current_selected_index]["name"]:
                print(f"|{Color.BG_YELLOW} {str(product['id'])[:4]:4}| {product_name:23}| {product_desc:46} | {str(product['price'])[:10]:10} | {str(product['quantity'])[:8]:8} {Color.DEFAULT}|")
            else:
                print(f"| {str(product['id'])[:4]:4}| {product_name:23}| {product_desc:46} | {str(product['price'])[:10]:10} | {str(product['quantity'])[:8]:8} |")

        print("""=========================================================================================================
\nAlternativ: [L] Lägg till | [T] Ta bort | [Ä] Ändra | [Q] Avsluta""")

    def import_items(self):
        # Öppna filen och importera items
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

def on_press(key):
    global products
    global listener
    global current_selected_index
    global is_handling_input

    # Ser till så att ingen knapp går att klicka
    if is_handling_input:
        return

    try:
        if key.char.upper() == "L":
            product.add_item()
        if key.char.upper() == "Q":
            # Sluta lyssna på inputs
            listener.stop()
            product.save_items()
            quit()
    except AttributeError:
        if key == keyboard.Key.down:
            if current_selected_index < len(products) - 1:
                current_selected_index += 1
        elif key == keyboard.Key.up:
            if current_selected_index > 0:
                current_selected_index -= 1
        elif key == keyboard.Key.enter:
            is_handling_input = True
            handle_enter_key(current_selected_index, products)
            is_handling_input = False

    product.check_inventory(current_selected_index)


def handle_enter_key(current_selected_index, products):
    print("""=========================================================================================================
\nAlternativ: [T] Ta bort | [Ä] Ändra | [B] Gå tillbaka | [Q] Avsluta""")
    print(f"{products[current_selected_index]} is selected")
    while True:
        key_pressed = getwch().upper()

        if key_pressed == "T":
            product.remove_item(products, current_selected_index)
            break
        elif key_pressed == "Ä":
            product.edit_item(products, current_selected_index)
            break
        elif key_pressed == "B":
            break
        elif key_pressed == "Q":
            # Sluta lyssna på inputs
            listener.stop()
            product.save_items()
            quit()

        
products = []
current_selected_index = 0
is_handling_input = False

product = Product("./db_products.csv")
product.import_items()
product.check_inventory(current_selected_index)

# Läs in tangentbordet
listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()

    # actions(product, products)