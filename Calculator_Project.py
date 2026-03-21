"""def cube(num):
    return num*num*num

result = cube(5)
print(result)"""

"""is_drive_far = False
is_radio_working = False

if is_drive_far or is_radio_working:
    print("the drive is far")
    print("the radio is working")
else:
    print("the drive is not far")
    print("the radio isn't working")"""

"""is_drive_far = False
is_radio_working = False

if is_drive_far and is_radio_working:
    print("the drive is far")
    print("the radio is working")
elif is_drive_far and not(is_radio_working):
    print("drive is far and radio isn't working")
elif not(is_drive_far) and is_radio_working:
    print("drive isn't far and radio is working")
else:
    print("the drive is not far")
    print("the radio isn't working")"""

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    

print(max_num(5, 6, 7))