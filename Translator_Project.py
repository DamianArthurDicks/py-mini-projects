def translate(phrase):    #we have if statements inside of a for loop inside of a function
    translation = ""      #that can translate both lower and upper case vowels into g/G
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a Phrase: ")))
        
