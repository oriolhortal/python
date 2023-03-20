import sys
import random

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game. ( ' included)\nGood luck!")

numero = random.randint(1,99)
intentos = 0

while True:
    respuesta = input ("\nWhat's your guess between 1 and 99?\n")

    if respuesta.lower() == "exit":
        print ("Goodbye!")
        sys.exit()

    try:
        NumRespuesta = int(respuesta)
        intentos += 1
    except ValueError:
        print ("Only numbers accepted")
        continue

    if NumRespuesta < numero:
        print ("Too low!")
    elif NumRespuesta > numero:
        print ("Too high!")
    else:
        if numero == 42:
            print ("The answer to the ultimate question of life, the universe and everything is 42.")
            if intentos == 1:
                print ("Congratulations! You got it on your first try!")
            else:
                print ("You won in", +intentos, "attempts!")
        else:
            if intentos == 1:
                print ("Congratulations! You got it on your first try!")
            else:
                print ("Congratulations, you've got it!")
                print ("You won in", +intentos, "attempts!")
        break
