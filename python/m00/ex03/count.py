import sys
import string

def text_analyzer(text:str = None):
    '''\nThis function counts the number ofupper characters, lower characters, punctuation and spaces in a given text.'''
    x = 0 #upper_letter
    y = 0 #lower_letter
    z = 0 #punctuation_mark
    w = 0 #spaces
    d = 0 #numeros

    if text == None:
        text = input("What is the text to analyze?\n")

    if not isinstance(text, str):
       raise AssertionError ("Argument is not a string")

    for char in text:
        if (char.isupper()):
            x += 1
        elif (char.islower()):
            y += 1
        elif (char.isspace()):
            w += 1
        elif (char in string.digits):
            d += 1
        elif (char in string.punctuation):
            z += 1

    print ("The text contains", (x + y + z + w + d), "character(s)")
    print ("-", + x, "upper letter(s)")
    print ("-", + y, "lower letter(s)")
    print ("-", + z, "punctuation mark(s)")
    print ("-", + w, "space(s)")

if __name__ == "__main__":
    if len (sys.argv) == 2:
        text = sys.argv[1]
        text_analyzer(text)
    else:
        print ("Input just one string")
        sys.exit(1)
