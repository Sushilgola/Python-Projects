# Find the Factorial Of A Number

num = int(input("Enter the Number: "))
fact_num = 1
for i in range(num,0,-1):
    fact_num *= i
print(f"{fact_num} is The Factorial of {num}")
