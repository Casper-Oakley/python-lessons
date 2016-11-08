print("Welcome to our calculator!")
print("Please input a number.")

input1 = int(input())

print("Please input another number.")

input2 = int(input())

print("Please input an operation. Choices can be 'plus' 'minus' 'divide' multiply'")

operator = str(input())

if(operator == 'plus'):
    output = input1 + input2
elif(operator == 'minus'):
    output = input1 - input2
elif(operator == 'divide'):
    output = input1 / input2
elif(operator == 'multiply'):
    output = input1 * input2

print(str(input1) + " " + operator + " " + str(input2) + " equals " + str(output))

