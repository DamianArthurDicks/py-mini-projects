import random

Return_Value = ""
Password_Length = int(input("Enter a number between 10 and 100: ")) 
Character_List = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                  "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4",
                  "5", "6", "7", "8", "9", "0", "!", "@", "#", "$",
                  "%", "^", "&", "*", "(", ")", "_", "-", "+", "=",
                  "{", "}", "[", "]", "|", ":", ";", "<", ">", ",",
                  ".", "?", "/", "~"]

 
if Password_Length < 10:
    print("Password Length to Short")
elif Password_Length > 100:
    print("Password Length to Long")
else:
    print("Password Length is perfect")

for x in range(Password_Length):
    Return_Value += random.choice(Character_List)

print("Generated Password:", Return_Value)
            