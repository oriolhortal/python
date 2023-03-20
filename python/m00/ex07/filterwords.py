import sys
import string

if len(sys.argv) != 3:
    print("Error: el programa debe ser llamado con dos argumentos: una cadena y un número entero.")
    sys.exit()

try:
    n = int(sys.argv[2])
except ValueError:
    print("Error: el segundo argumento debe ser un número entero.")
    sys.exit()

s = sys.argv[1]
words = [word.strip(string.punctuation) for word in s.split() if len(word.strip(string.punctuation)) > n]
print(words)
