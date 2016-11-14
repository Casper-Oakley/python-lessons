
def askForInput( message ):
    print(message)
    inputString = input()
    return inputString

print("Welcome to our calculator!")

isRunning = True
while(isRunning):

    input1 = askForInput("Please input a number.")
    input2 = askForInput("Please input another number.")
    operator = askForInput("Please input an operation. Choices can be 'plus' 'minus' 'divide' 'multiply'")

    isInvalidInputs = True

    while(isInvalidInputs):

        if(operator == 'plus'):
            output = input1 + input2
            isInvalidInputs = False
        elif(operator == 'minus'):
            output = input1 - input2
            isInvalidInputs = False
        elif(operator == 'divide'):
            if(input2 == 0):
                print("Error: your second input is zero. Cannot divide by zero!")
                print("Please enter your second input again.")
                input2 = int(input())
            else:
                output = input1 / input2
                isInvalidInputs = False
        elif(operator == 'multiply'):
            output = input1 * input2
            isInvalidInputs = False
        else:
            print("Error: " + operator + " is not a valid operator.")
            print("Please input an operation. Choices can be 'plus' 'minus' 'divide' multiply'")
            operator = str(input())

    if(isInvalidInputs == False):
        print(str(input1) + " " + operator + " " + str(input2) + " equals " + str(output))

    question = askForInput("Do you want to make another calculation (type 'yes' or 'no')? ")

    if(question == 'yes'):
        isRunning = True
    else:
        isRunning = False
