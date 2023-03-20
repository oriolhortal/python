import sys

def check_num(num):
    if num == 0:
        print ("I\'m zero")
    elif num % 2 == 0:
        print ("I\'m even")
    else:
        print ("I\'m odd")

if len(sys.argv) > 2:
    print ("More than one argument provided")
elif len(sys.argv) == 1:
    print ("")
else:
    try:
        sys.argv[1].isnumeric()
        num = int(sys.argv[1])
        check_num(num)
    except:
        print ("Argument is not an integer")
