def division(a,b):
    try:
        answer = int(a) / int(b)
    except ArithmeticError:
        if(int(b) == 0):
            print("Cannot divide by zero")
        else:
            print("ERROR!")
    else:
        print("{0} / {1} = ".format(x,y) + str(answer))

print("---- This program divides to numbers ----")
x = input("Enter number 1: ")
y = input("Enter number 2: ")
division(x,y)
