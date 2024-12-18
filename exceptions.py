import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("error: invalid input, try again")
    
    x = int(input("x: "))
    y = int(input("y: "))



try:
    result = x / y
except ZeroDivisionError:
    print("error: cannot divide by 0.")
    sys.exit(1)



print(f" {x} / {y} = {result}")