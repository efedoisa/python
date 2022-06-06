num = input("Enter a positive integer number: ")
while not num.isdigit():
    print("Do not enter floats, strings or negative numbers!")
    num = input("Please enter a positive integer number: ")

sum = 0
digit = len(num)

num2 = int(num)
while num2>0:
    order = num2 % 10
    sum+= order ** digit
    num2//=10
    
if sum == int(num):   
    print(f"{num} is an armstrong number.")   
else:       
    print(f"{num} is NOT an armstrong number!")