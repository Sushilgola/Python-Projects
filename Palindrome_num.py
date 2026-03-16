# Find Palindrome Number

num = int(input("Enter A Number: "))
temp = num
add_num = 0

while num > 0:
    mod_num = num % 10
    add_num *= 10
    add_num += mod_num
    num //= 10

if temp == add_num:
    print(f"{temp} is Palindrome Number!")
else:
    print(f"{temp} Number is Not Palindrome Number!")