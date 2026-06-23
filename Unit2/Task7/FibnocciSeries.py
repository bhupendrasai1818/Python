terms = int(input("Enter the number of terms: "))   
if terms <= 0: 
    print("Enter a positive integer.")
else: 
    a, b = 0, 1
    print("Fibonacci Sequence:") 
    for i in range(terms): 
        print(a, end=" ") 
        next_term = a + b 
        a = b 
        b = next_term