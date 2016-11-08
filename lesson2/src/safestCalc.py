print("Welcome to our calculator!")
print("Please input a number.")

input1 = int(input())

print("Please input another number.")

input2 = int(input())

print("Please input an operation. Choices can be 'plus' 'minus' 'divide' multiply'")

operator = str(input())

isInvalidInputs = True


if(operator == 'plus'):
    output = input1 + input2
    isInvalidInputs = False
elif(operator == 'minus'):
    output = input1 - input2
    isInvalidInputs = False
elif(operator == 'divide'):
    if(input2 == 0):
        print("Error: your second input is zero. Cannot divide by zero!")
    else:
        output = input1 / input2
        isInvalidInputs = False
elif(operator == 'multiply'):
    output = input1 * input2
    isInvalidInputs = False
else:
    print("Error: " + operator + " is not a valid operator.")

if(isInvalidInputs == False):
    print(str(input1) + " " + operator + " " + str(input2) + " equals " + str(output))
