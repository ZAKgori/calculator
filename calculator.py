'''
give 4 options:
1. add
2. subtract
3. multiply
4.divide
ask the user for input
then ask for 2 numbers after the option that they created
based on what they chose do the operation on the 2 numbers
then print the result
'''
print('PLEASE CHOOSE THE OPERATION YOU WANT TO CARRY OUT: ')
operation = input('1. add\n2. subtract\n3. multiply\n4. divide\n')

print('PLEASE ENTER TWO NUMBERS BETWEEN 1 - INFINITY ')
num1 = input()
num2 = input()

if operation == "1":
    result = int(num1) + int(num2)
    print(f"{num1} + {num2} = {result}")
elif operation == "2":
    result = int(num1) - int(num2)
    print(f"{num1} - {num2} = {result}")
elif operation == "3":
    result = int(num1) * int(num2)
    print(f"{num1} * {num2} = {result}")
elif operation == "4":
    if int(num2) != 0:  # Adding check to avoid division by zero
        result = int(num1) / int(num2)
        print(f"{num1} / {num2} = {result}")
    else:
        print("Division by zero is not allowed.")
else:
    print("INVALID INPUT")
