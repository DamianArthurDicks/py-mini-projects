Employee_File = open("employees.txt", "a") #use "w" to write a new file of employees  
                                           #use "a" to append to existing file
Employee_File.write("\nJerry - Human Resources")

Employee_File.close()