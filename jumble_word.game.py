import random
def choose():
    words=['rainbow','computer','science','player','board','swing','love','dove','soap','kill']
    pick = random.choice(words)
    return pick

    # function for shuffling the characters of the choosen words
def jumble(word):
    random_word = random.sample(word, len(word) )
    jumbled = ''.join(random_word)
    return jumbled
# func for showing final score
def thank(p1n,p2n,p1,p2):
    print(p1n, 'your score is: ' , p1)
    print(p2n, 'your score is: ' , p2)
    # func call check_win
    check_win(p1n, p2n, p1 ,p2)
    print("Thanks for playing")



# func for declaring winner
def check_win(player1 , player2, p1score ,p2score):
    if p1score > p2score:
        print("winner is: " , player1)
    elif p2score > p1score:
        print("winner is: " , player2)
    else:
        print("GAME IS TIE !!!!")
    # func for playing game
def play():
    p1name= input("Enter name: ")
    p2name= input("Enter name: ")
    # variable for counting score
    pp1 = 0
    pp2 = 0
    # variable for counting turn
    turn = 0
    while True:
        # choose()  func calling
        picked_word = choose()
        # jumbled() func calling
        qn = jumble(picked_word)
        print("Jumbled word is: ", qn)
        # checking turn is odd or even
        if turn % 2 == 0:
            print(p1name, 'Your Turn')
            ans = input("Guess word: ")
            if ans == picked_word:
                pp1 += 1
                print('Your score is ', pp1)
                turn += 1
            else:
                print("BETTER LUCK NEXT TIME ")
                print(p2name, 'Your Turn')
                ans = input("Guess word: ")
                if ans == picked_word:
                    pp2 += 1
                    print('Your score is ', pp2)
                else:
                    print("BETTER LUCK NEXT TIME & corect word is : " , picked_word)
                c = int(input("Press 1 To continue & 0 To quit"))
                if c == 0:
                    thank(p1name, p2name, pp1, pp2)
                    break
        else:
            print(p2name, 'Your Turn')
            ans = input("Guess word: ")
            if ans == picked_word:
                pp2 += 1
                print('Your score is ', pp2)
                turn += 1
            else:
                print("BETTER LUCK NEXT TIME ")
                print(p1name, 'Your Turn')
                ans = input("Guess word: ")
                if ans == picked_word:
                    pp1 += 1
                    print('Your score is ', pp1)
                else:
                    print("BETTER LUCK NEXT TIME & corect word is : " , picked_word)
                    c = int(input("Press 1 To continue & 0 To quit"))
                    if c == 0:
                        thank(p1name, p2name, pp1, pp2)
                        break
                c = int(input("Press 1 To continue & 0 To quit "))
                if c == 0:
                        thank(p1name, p2name, pp1, pp2)
                        break
# Driver code
if __name__ == '__main__':
    play()







