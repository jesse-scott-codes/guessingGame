# AUTHOR : JESSE SCOTT
# DATE CREATED : Oct. 27, 2022

import os
import time
import sys
import random

running = True

randomNumber = random.randint(1, 10)

def main():
    try:
        while running:
            os.system("cls")
            print("Guess a number between 1 and 10.")
            print()
            guessNum = input("Answer: ")

            if int(guessNum) == randomNumber:
                print()
                print("You guessed right!")
                time.sleep(3)
            else:
                print()
                print("you were wrong!")
                time.sleep(3)
    except KeyboardInterrupt:
        sys.exit()

main()