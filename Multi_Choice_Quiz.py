from Multi_Choice_Question_Class import Question

Question_Prompts = [   #These are multiple choice questions put in an array/list
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What colour are bananas?\n(a) Teal\n(b) Magneta\n(c) Yellow\n\n",
    "What colour are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
                    ]

Questions = [  #These are the answers for each questions put in an array/list
    Question(Question_Prompts[0], "a"),
    Question(Question_Prompts[1], "c"),
    Question(Question_Prompts[2], "b")
            ]

def Run_Test(Questions):  #This for loop inside a function tracks the score of questions answered
    Score = 0             #and checks if the answers are correct
    for Question in Questions:
        Answer = input(Question.Prompt)
        if Answer == Question.Answer:
            Score += 1
    print("You Got " + str(Score) + "/" + str(len(Questions)) + " Correct")

Run_Test(Questions)