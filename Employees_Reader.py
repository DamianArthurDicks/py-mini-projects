Employee_File = open("Employees.txt", "r")
for Employee in Employee_File.readlines():
    print(Employee) 
Employee_File.close()