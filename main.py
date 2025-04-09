from inventory import (add_item, view_inventory,
                        update_item, delete_item, 
                        search_item, check_low_stock,
                        export_inventory_to_csv, show_inventory_value)


def show_menu():
    print("\n--- Inventory System Menu ---")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Search Item")
    print("6. Check Low Stock")
    print("7. Export Inventory to CSV")
    print("8. Show Total Inventory Value")
    print("9. Exit")


while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == '1':
        view_inventory()

    elif choice == '2':
        name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        add_item(name, quantity, price)
        print("Item added!")

    elif choice == '3':
        view_inventory()
        try:
            item_no = int(input("Enter item number to update: ")) - 1
            new_quantity = int(input("Enter new quantity: "))
            new_price = float(input("Enter new price: "))
            update_item(item_no, new_quantity, new_price)
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    elif choice == '4':
        view_inventory()
        try:
            item_no = int(input("Enter item number to delete: ")) - 1
            delete_item(item_no)
        except ValueError:
            print("Invalid input. Please enter a number. ")

    elif choice == '5':
        keyword = input("Enter Keyword to search: ")
        search_item(keyword)

    elif choice == '6':
        check_low_stock()

    elif choice == '7':
        export_inventory_to_csv()

    elif choice == '8':
        show_inventory_value()

    elif choice == '9':
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
