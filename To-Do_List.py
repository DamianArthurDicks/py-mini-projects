Uncompleted_Tasks = [
    "Eat Breakfast",
    "Start Work",
    "Eat Lunch",
    "Finish Work",
    "Come home and relax",
    "Go to Sleep",                
                    ]
Completed_Tasks = []
Activities = ""

for Activities in range(5):
    Tasks = Uncompleted_Tasks.pop(0)
    Completed_Tasks.append(Tasks)
print(Completed_Tasks)
           



