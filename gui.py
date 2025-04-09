import tkinter as tk
from tkinter import messagebox
from inventory import load_data, add_item

# ----- Function ----- #

def view_inventory_gui():
    data = load_data()

    inventory_list.delete(0, tk.END)  # clear listbox

    if not data:
        inventory_list.insert(tk.END, "Inventory is empty.")
    else:
        for item in data:
            line = f"{item['name']} - Qty: {item['quantity']} - Price: P{item['price']}"
            inventory_list.insert(tk.END, line)

def open_add_item_window():
    def submit():
        name = name_entry.get()
        try:
            quantity = int(quantity_entry.get())
            price = float(price_entry.get())
            add_item(name, quantity, price)
            messagebox.showinfo("Success", f"{name} added to inventory.")
            add_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid quantity and price")

    add_window = tk.Toplevel(root)
    add_window.title("Add New Item")

    tk.label(add_window, text="Item Name:").pack()
    name_entry = tk.Entry(add_window)
    name_entry.pack()

    tk.Label(add_window, text="Quantity:").pack()
    quantity_entry = tk.Entry(add_window)
    quantity_entry.pack()

    tk.Label(add_window, text="Price:").pack()
    price_entry = tk.Entry(add_window)
    price_entry.pack()

    tk.Button(add_window, text="Add Item", command=submit).pack(pady=5)

# ----- GUI Setup ----- #

root = tk.Tk()
root.title("Inventory System")


# ----- Frame ----- #

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

# ----- View Button ----- #

view_btn = tk.Button(frame, text="View Inventory", command=view_inventory_gui)
view_btn.pack(pady=5)

# ----- Inventory List Display ----- #

inventory_list = tk.Listbox(frame, width=50, height=10)
inventory_list.pack(pady=10)

# ----- Add Item Button ----- #

add_button = tk.Button(frame, text="Add Item", command=open_add_item_window)
add_button.pack(pady=5)

# ----- Start GUI loop ----- #
root.mainloop()
