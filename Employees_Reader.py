Employee_File = open("Employees.txt", "r") #use "r" to read file
for Employee in Employee_File.readlines():  #.readlines to read all lines in file
    print(Employee) 
Employee_File.close()