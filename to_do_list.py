# Step 1: Basic Setup

tasks = []  # yahan pe sare tasks store honge

while True:
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "4":
        print("Exiting To-Do List. Goodbye!")
        break
    elif choice == "1":
        task = input("Enter Your Task: ")
        tasks.append(task)
    elif choice == "2":
        if not tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
    elif choice == "3":
        for i , task in enumerate(tasks , start=1):
            print(f"{i}. {task}")
        task_num = int(input("Enter task number to delete the task: "))
        if 1 <= task_num <= len(tasks):
            tasks.pop(task_num - 1)
            print("Task deleted successfully")
        else:
            print("Invalid Task Number")
    

