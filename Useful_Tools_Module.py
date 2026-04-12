import random   #imports "random" library

Feet_in_Mile = 5280
Meters_in_Kilometer = 1000
Beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Star"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1: ]

def roll_dice(num):
    return random.randint(1, num)