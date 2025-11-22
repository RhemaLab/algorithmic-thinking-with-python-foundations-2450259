#problem: Imagine there are  100 doors that are all initially closed. You make 100 passes by the doors
#On the first passs, you will visit every door in sequence and toggle its state, that is, if the door is closed, you open
# it; if it is open, you close it. For the second time(pass), you only will visit every second door (door 2,4,6,...) and toggle it.
# For the third time(pass), you will visit every third door (door3,6,9,...) and toggle it. Continue this pattern until you only visit the 100th door.
# At the end of the process, which doors are open and which doors are closed?



#How to represent the data
#Representing the state of the doors: False = Closed Door , True = Open Door
#I want to map the index to the door number  from 1 to 101  but will ignore index 0 instead of 0 to 100
#Shortcut of PyCharm on windows Ctrl+Shift+F10 - runs the current file.
doors = [False] * 101

print(doors)

for i in range(1, 101):
    doors[i] = not doors[i]

print(doors)

#Nested loop with outer and inner loops.For each outer loop, the inner loop executes:
for i in range(1, 6):
    for j in range(1, 4):
        print("i:", i, "j:", j)

#Step Parameter for the range function - the third parameter in range() is the step
for i in range(1, 11, 2):
    print(i)
