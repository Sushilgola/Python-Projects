import random

chance = 0
rand_num = random.randint(1, 100)

print("You have 10 chance to find the Number! ")
while chance != 10:
    chance += 1
    guess_num = int(input("Guess the number: "))

    if rand_num == guess_num:
        print("Congratulation You Got Number! ", guess_num)
        break
    elif rand_num > guess_num:
        print("Try Bigger Number! ")
    elif rand_num < guess_num:
        print("Try Smaller Number! ")

if chance == 10:
    print("\nYou Lose the Game!")

