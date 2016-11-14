
def askForInput( message ):
    print(message)
    inputString = input()
    return inputString

def writeToLog( input1, operator, input2, output, fileObject ):
    message = operator + ": " + str(input1) + ", " + str(input2) + " = " + str(output) + "\n"
    fileObject.write(message)



#We start by opening our log file
myLogFile = open("my_log.txt", "a")

print("Welcome to our calculator!")

#Here, we loop until the user specifies
#that they want to end the program
isRunning = True
while(isRunning):

    input1 = int(askForInput("Please input a number."))
    input2 = int(askForInput("Please input another number."))
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
        writeToLog(input1, operator, input2, output, myLogFile)

    question = askForInput("Do you want to make another calculation (type 'yes' or 'no')? ")

    if(question == 'yes'):
        isRunning = True
    else:
        isRunning = False

#Don't forget to close our file once we're done!
myLogFile.close()