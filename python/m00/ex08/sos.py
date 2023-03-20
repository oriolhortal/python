import sys

MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': '/'
}


def encode_morse(message):
    encoded = ''
    for char in message:
        if char.upper() in MORSE_CODE:
            encoded += MORSE_CODE[char.upper()] + ' '
        else:
            encoded += char + ' '
    return encoded.strip()


if len(sys.argv) == 1:
    print("Uso: python morse.py 'mensaje'")
else:
    message = ' '.join(sys.argv[1:])
    print(encode_morse(message))