import sys
import string

def maths(num1, num2):
    a = num1
    b = num2
    print ("Sum:", (a + b))
    print ("Difference:", (a - b))
    print ("Product:", (a * b))
    if b == 0:
        print ("Quotient: ERROR (division by zero)")
        print ("Remainder: ERROR (modulo by zero)")
    else:    
        print ("Quotient:", (a / b))
        print ("Remainder:", (a % b))

if len (sys.argv) == 1:
    print ("Usage: python operations.py <num1> <num2>\nExample: python operations.py 10 3")
elif len (sys.argv) == 2:
    print ("Error: Only one argument provided")
    sys.exit()
elif len (sys.argv) > 3:
    print ("Error: More than 2 argumens provied")
    sys.exit()
else:
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        maths(num1, num2)
    except ValueError:
        print ("Only integers")
        sys.exit()
