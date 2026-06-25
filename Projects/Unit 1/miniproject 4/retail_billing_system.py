import tkinter as tk

subtotal = 0

def add_item():
    global subtotal

    name = product.get()
    qty = int(quantity.get())
    price = float(price_entry.get())

    total = qty * price
    subtotal += total

    items.insert(tk.END, f"{name} - {qty} x {price} = ₹{total}")

    product.delete(0, tk.END)
    quantity.delete(0, tk.END)
    price_entry.delete(0, tk.END)

def generate_bill():
    discount = subtotal * 0.10 if subtotal > 5000 else 0
    gst = (subtotal - discount) * 0.18
    final = subtotal - discount + gst

    result.config(
        text=f"""
Subtotal : ₹{subtotal:.2f}
Discount : ₹{discount:.2f}
GST : ₹{gst:.2f}
Final Amount : ₹{final:.2f}
"""
    )

root = tk.Tk()
root.title("Retail Billing System")
root.geometry("500x500")

tk.Label(root, text="Retail Billing System",
         font=("Arial", 16, "bold")).pack()

tk.Label(root, text="Product Name").pack()
product = tk.Entry(root)
product.pack()

tk.Label(root, text="Quantity").pack()
quantity = tk.Entry(root)
quantity.pack()

tk.Label(root, text="Price").pack()
price_entry = tk.Entry(root)
price_entry.pack()

tk.Button(root, text="Add Item",
          command=add_item).pack(pady=10)

items = tk.Listbox(root, width=50)
items.pack()

tk.Button(root, text="Generate Bill",
          command=generate_bill).pack(pady=10)

result = tk.Label(root, text="")
result.pack()

root.mainloop()