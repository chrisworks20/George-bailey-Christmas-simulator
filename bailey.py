import random
import time

print("George Bailey Simulator 1.0")
print(" ")
times = int(input("How many Christmas's would you like to simulate? "))
choices = ["To live", "To not exist"]
print("You've picked ", times, "Christmas's to be ran.")
time.sleep(1)
results = []

for i in range(times):
    outcome = random.choice(choices)
    results.append(outcome)
    print(outcome)
else:
    print(" ")
    print("Simulation is complete")
    print(" ")
    time.sleep(1)
    print("Lets look at our data.")
    a1 = results.count("To live")
    a2 = results.count("To not exist")
    print(" ")
    print("George Bailey picked to live ", a1, "times")
    print("and")
    print("George Bailey picked to not exist", a2, "times")
    print(" ")

time.sleep(1)
if a1 > a2:
    print("George Bailey picked to live most often")
elif a2 > a1:
    print("Goerge Bailey picked to not exist most often")
else:
    print("Program done")
