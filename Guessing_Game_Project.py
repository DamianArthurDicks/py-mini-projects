Secret_Word = "crocodile"     #logical operators are "and, or, not"
Guess = ""     #"and" is used if both conditions are true
Guess_Count = 0   #"or" is used if 1 one of the conditions are true
Guess_Limit = 3   #"not" reverses a condition if it is True = False
Out_of_Guesses = False

while Guess != Secret_Word and not (Out_of_Guesses):   #before going thru the while loop
    if Guess_Count < Guess_Limit:                     #this checks if we still have any guesses left
        Guess = input("Enter guess: ")   #if there are it asks for more input from user
        Guess_Count += 1               
    else:
        Out_of_Guesses = True   #if there aren't any guesses left it
                                #it prints out of guesses you lose and stops the while loop
if Out_of_Guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("YOU WIN!")
