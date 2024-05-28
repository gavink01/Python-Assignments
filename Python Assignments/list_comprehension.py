#Task 12

squares = [(x ** 2) for x in range(1,11)]
print(squares)

evens = [x for x in squares if (x % 2 == 0)]
print(evens)