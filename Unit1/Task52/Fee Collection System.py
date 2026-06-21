student_name = input("Enter Student Name: ")
total_fee = float(input("Enter Total Fee Amount: "))
fee_paid = float(input("Enter Fee Amount Paid: "))
pending_balance = total_fee - fee_paid
print("\n--- Fee Collection Report ---")
print("Student Name:", student_name)
print("Total Fee Amount:", total_fee)
print("Fee Paid:", fee_paid) 
print("Pending Balance:", pending_balance)