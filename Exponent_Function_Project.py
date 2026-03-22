def Raise_to_Power(Base_Num, Pow_Num):
    Result = 1
    for index in range(Pow_Num):
        Result = Result * Base_Num
    return Result


print(Raise_to_Power(3, 3))