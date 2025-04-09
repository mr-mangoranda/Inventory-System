import json
import os
import csv


file_path = os.path.join(os.path.dirname(__file__), "database.json")

#------------------------------------------------------------------------------------------#

def load_data():
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def export_inventory_to_csv(filename='report.csv'):
    data = load_data()
    if not data:
        print("Inventory is empty. Nothing to export.")
        return
    
    with open(filename, mode='w', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Item Name," "Quantity", "Price"])

        for item in data:
            writer.writerow([item['name'], item['quantity'], item['price']])

    print(f"Inventory exported to {filename} successfully!")


#------------------------------------------------------------------------------------------#

def add_item(name, quantity, price):
    data = load_data()
    item = {
        "name": name,
        "quantity": quantity,
        "price": price
    }
    data.append(item)
    save_data(data)

def view_inventory():
    data = load_data()
    if not data:
        print("Inventory is empty.")
    else:
        print("\nCurrent Inventory:")
        for index, item in enumerate(data, 1):
            print(f"{index}. {item['name']} - Qty: {item['quantity']} - Price: P{item['price']}")

def update_item(index, new_quantity, new_price):
    data = load_data()
    if 0 <= index < len(data):
        data[index]["quantity"] = new_quantity
        data[index]["price"] = new_price
        save_data(data)
        print("Item updated successfully!")
    else:
        print("Invalid item number.")

def delete_item(index):
    data = load_data()
    if 0 <= index < len(data):
        deleted = data.pop(index)
        save_data(data)
        print(f"Deleted item: {deleted['name']}")
    else:
        print("Invalid item number.")

def search_item(keyword):
    data = load_data()
    found = []

    for item in data:
        if keyword.lower() in item['name'].lower():
            found.append(item)

    if not found:
        print(f"No items found matching {keyword}.")
    else:
        print(f"\nSearch result for {keyword}:")
        for index, item in enumerate(found,1):
            print(f"{index}. {item['name']} - Qty: {item['quantity']} - Price: P{item['price']}")       

def check_low_stock(threshold=5):
    data = load_data()
    low_stock_items = []

    for item in data:
        if item["quantity"] < threshold:
            low_stock_items.append(item)

    if not low_stock_items:
        print(f"All items are well-stocked (above {threshold})")

    else:
        print("\nLow Stock Alert! Item below {threshold} quantity:")
        for index, item in enumerate(low_stock_items, 1):
            print(f"{index}. {item['name']} - Qty: {item['quantity']}")

def show_inventory_value():
    data = load_data()
    if not data:
        print("Inventory is empty.")
        return
    
    total_value = 0
    print("\nInventory Value:")
    for item in data:
        item_value = item["quantity"] * item['price']
        total_value += item_value
        print(f'{item['name']}: {item['quantity']} x {item['price']} = P{item_value:.2f}')

    print(f"\nTotal Inventory Value:P{total_value:.2f}")
            