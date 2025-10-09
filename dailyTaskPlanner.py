userName = input("What’s your name? ").capitalize()
numberOfTasks = int(input("How many tasks today? "))

taskName =  []
taskPriority = []
taskTime = []

for i in range(numberOfTasks):
    taskName.append(input(f"Enter task name {i+1}: "))
    taskPriority.append(input("Enter priority (High/Medium/Low): "))
    taskTime.append(float(input("Enter time in minutes: ")))

totalTime = 0
eachTaskPercentage = []
for i in range(len(taskTime)):
    totalTime += taskTime[i]

for i in range(len(taskTime)):
    percentage = (taskTime[i]/totalTime) * 100
    eachTaskPercentage.append(percentage)

if totalTime > 480:
    statusMessage = "The Day is Packed(8 hours)"
elif totalTime < 120:
    statusMessage = "The Day is Light(2 hours)"
else:
    statusMessage = "The Day is Balanced(4-6 hours)"

print(f"Daily Planner for {userName}")

for i in range(len(taskName)):
    print(f"- Task: {taskName[i]}, Priority: {taskPriority[i]}, Time: {taskTime[i]:.2f} minutes ({eachTaskPercentage[i]:.2f}% of total)")

print(f"Total time planned: {totalTime:.2f} minutes")
print(f"Status: {statusMessage}")











