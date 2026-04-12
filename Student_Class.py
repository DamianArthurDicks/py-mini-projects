class Student:     #Class defines the object data type

    def __init__(self, name, major, gpa, is_on_probation):  #these parenthesis passes info to the object
        self.name = name     #this make sure that the object name == name that we passed in                               
        self.major = major   #this make sure that the object major == major that we passed in
        self.gpa = gpa       #this make sure that the object gpa == gpa that we passed in
        self.is_on_probation = is_on_probation  #same for is on probation

    def on_honor_roll(self):   #this is a class function that checks if the student is on honor roll
        if  self.gpa >= 3.5:
            return True
        else:
            return False