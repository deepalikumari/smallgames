import random
import math
# taking inputs
lower = int(input("Enter Lower bound: "))
upper= int(input("Enter Upper bound: "))
# generating random no. betwwen upper and lower bound
x = random.randint(lower,upper)
print("\n\tYou have only", round(math.log(upper - lower + 1, 2)), "chance to guess the integer!\n")
# initialling the no of guesses
count=0
# for calculation of minimum no. of guesses depends upon the range
while count < math.log(upper - lower + 1, 2):
    count += 1
    # taking guessing n. as input
    guess = int(input("Guess a No.: "))
    # condition testing
    if x == guess:
        print("Congratulation you did it in ", count," try")
        # once guessed loop will break
        break
    elif x>guess:
        print("You guessed too small !!!")
    elif x<guess:
        print("You guessed too high !!!")
        # if guessing is more than the required guesses shows this output
if count >= math.log(upper-lower + 1, 2):
    print("THE NO> IS %d" %x)
    print("Better Luck Next Time!")