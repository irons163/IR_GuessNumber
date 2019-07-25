import random

answer = random.randint(1, 10)

while True:
    guess = int(input("Please input a guess number(1-10):"))
    if answer < guess:
        print("Too large.")
    elif answer > guess:
        print("Too small5.")
    else:
        print("You Win.")
        break
