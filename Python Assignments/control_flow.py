# Task 4

def value_checker(x):
    if(x == 0):
        print("{0} is zero".format(x))
    elif(x < 0):
        print("{0} is a negative number".format(x))
    else:
        print("{0} is a positive number".format(x))

number = int(input("Please enter a whole number to find whether it is positive, negative or zero: "))
value_checker(number)