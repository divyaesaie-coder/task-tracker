# Task Manager using File Handling

tasks = []

# Read existing tasks from file
try:
    file = open("tasks.txt", "r")

    for line in file:
        tasks.append(line.strip())

    file.close()

except FileNotFoundError:
    pass

# Get date
date = input("Enter date: ")

print(f"Tasks for {date}")

# Add tasks
while True:

    task = input("Enter task including time (or type 'exit'): ")

    if task.lower() == "exit":
        break

    tasks.append(task)

# Save tasks to file
file = open("tasks.txt", "w")

for task in tasks:
    file.write(task + "\n")

file.close()

print("Tasks saved successfully!")

# Display all tasks
print("Saved Tasks:")
for task in tasks:
    print("-", task)
