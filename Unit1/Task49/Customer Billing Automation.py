customer_name = input("Enter Customer Name: ")
product_amount = float(input("Enter Product Amount: "))
quantity = int(input("Enter Quantity: "))

total_amount = product_amount * quantity

print("\n----- Invoice -----")
print("Customer Name =", customer_name)
print("Product Amount =", product_amount)
print("Quantity =", quantity)
print("Total Amount =", total_amount)