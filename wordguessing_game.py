import random
# lib help to choose random word from list
name = input("ENTER NAME: ")
print("Good luck ", name)
words = ['rainbow','computer','sheep','goat','car','water','board','sleep','singing','dancing','mathematics','sea']
print(words)
word = random.choice(words)
print("Guess Charcter : ")

guesses = ''
# any no of turns can be used
turns = 5

while turns > 0:
    # counts the no. of time user fails
    failed = 0
    # all character from the input word taking one at a time
    for char in word:
        # comparing the character with the character in guesses
        if char in guesses:
            print(char)
        else:
            print("-")
            # for every failure 1 will be incremented in the failure
            failed += 1
    if failed == 0:
        # user will win the game if failure is 0
        # you win will be printed
        print("U WIN")
        print("The Word is:  " , word)
        break
    # if user hv ip wrong alphabet it will ask user to enter another alph
    guess = input("guess a character: ")
    #  every ip charcter store in guesses
    guesses += guess

    # check ip with charcter in word
    if guess not in word:

        turns -= 1
        # if character not match the word wrong will be printed
        print("WRONG")
        print("U have", +turns,'more guesses')

        if turns == 0:
            print("YOU LOOSE")
