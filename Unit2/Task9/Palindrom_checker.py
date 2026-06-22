num = int(input("Enter a number: "))
dup = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if dup == reverse:
    print(dup   , "is a Palindrome Number")
else:
    print(dup, "is not a Palindrome Number")