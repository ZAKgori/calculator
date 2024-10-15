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
total = 0
print('PLEASE CHOOSE THE OPERATION YOU WANT TO CARRY OUT: ')
operation = input('1. add\n2. subtract\n3. multiply\n4.divide\n')
print('PLEASE ENTER TWO NUMBERS BETWEEN 1 - INFINITY ')
num1 = input()
num2= input()
if operation == "1":
    sum = int(num1) + int(num2)
    print(f"{num1} + {num2} = {sum}")
elif operation == 2:
    print()
elif operation == 3:
    print()
elif operation == 4:
    print()
else:
    print ("INVALID INPUT")