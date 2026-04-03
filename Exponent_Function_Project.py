def Raise_to_Power(Base_Num, Pow_Num):   #Base_Num and Pow_Num are the 2 inputs
    Result = 1                      #we are storing the value in this variable "Result"
    for index in range(Pow_Num):    #here we are looping thru Pow_Num until it reaches number input
        Result = Result * Base_Num  #each time Pow_Num loops it multiplies its self by the Base_Num
    return Result


print(Raise_to_Power(2, 3))