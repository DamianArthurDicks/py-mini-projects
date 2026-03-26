Hangman_Letters = ["M", "O", "N", "K", "E", "Y"]
Guess = []
Guess_Count = 0
Guess_Limit = 12
Out_of_Guesses = False

while Guess != Hangman_Letters and not (Out_of_Guesses):   #while that loops until out of guesses
    if Guess_Count < Guess_Limit:
        Guess.append(input("Guess a letter: ").upper())   #if letter is guessed in lower case it is coverted in to uppercase
        Guess_Count += 1       #every guess counted is added to the guess list                
        print("Guess Again")   #guess count adds guess number until it has reached its guess limit
    else:
        Out_of_Guesses = True
if Out_of_Guesses:
    print("you lose")
if Guess == Hangman_Letters:
    print("You Guessed Correct, You Win")     
    

    