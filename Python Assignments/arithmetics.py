# Task 3

#Takes user input of 2 numbers and returns the 

print("Please pick 2 whole numbers for basic arithmetics")
num1 = int(input("number 1: "))
num2 = int(input("number 2: "))

print("Addition: {0} + {1} = ".format(num1,num2) + str(num1 + num2))
print("Subtraction: {0} - {1} = ".format(num1,num2) + str(num1 - num2))
print("Multiplication: {0} * {1} = ".format(num1,num2) + str(num1 * num2))
print("Division: {0} / {1} = ".format(num1,num2) + str(num1 / num2))