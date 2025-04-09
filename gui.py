import tkinter as tk
from tkinter import messagebox
from inventory import load_data

def view_inventory_gui():
    data = load_data()

    inventory_list.delete(0, tk.END)  # clear listbox

    if not data:
        inventory_list.insert(tk.END, "Inventory is empty.")
    else:
        for item in data:
            line = f"{item['name']} - Qty: {item['quantity']} - Price: ${item['price']}"
            inventory_list.insert(tk.END, line)

# ----- GUI Setup -----
root = tk.Tk()
root.title("Inventory System")

# Frame
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

# View Button
view_btn = tk.Button(frame, text="View Inventory", command=view_inventory_gui)
view_btn.pack(pady=5)

# Inventory Display
inventory_list = tk.Listbox(frame, width=50, height=10)
inventory_list.pack(pady=10)

# Start GUI loop
root.mainloop()
