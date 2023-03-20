import sys

combined_strings = ' '.join(sys.argv[1:])
reversed_string = combined_strings[::-1]
converted_string = reversed_string.swapcase()
print(converted_string)
