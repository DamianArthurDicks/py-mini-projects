Hangman_Letters = ["M", "O", "N", "K", "E", "Y"]
Guess = []
Guess_Count = 0
Guess_Limit = 12
Out_of_Guesses = False

while Guess != Hangman_Letters and not (Out_of_Guesses):
    if Guess_Count < Guess_Limit:
        Guess.append(input("Guess a letter: ").upper())
        Guess_Count += 1
        print("Guess Again")
    else:
        Out_of_Guesses = True
if Out_of_Guesses:
    print("you lose")
if Guess == Hangman_Letters:
    print("You Guessed Correct, You Win")     
    

    