print("=" * 30)
print("  Welcome To Your Task Manager")
print("=" * 30)
def task_manager():
    tasks = []
    while (True):
        print("Menu")
        print("1. Add Task")
        print("2. View Task")
        print("3. Delete Task")
        print("4. Exit")

        try:
            choose = int(input("choose: "))
        except ValueError:
            print("Please enter a number!")
            continue

        if (choose == 1):
            print("enter task")
            task = input("task: ")
            tasks.append(task)
        elif (choose == 2):
            if tasks:
                print("\n==TO DO LIST==")
                for i in range(len(tasks)):
                    print(f"{i+1}. {tasks[i]}")
            else:
                print("The list is empty")
        elif (choose == 3):
            if tasks:
                print("which task do u want to remove from the list")
                for i in range(len(tasks)):
                    print(f"{i+1}. {tasks[i]}")
                try:
                    j = int(input("Task Number: "))
                except ValueError:
                    print("Invalid input. Enter a valid number.")
                    continue
                # if tasks[j]:
                if j >= 1 and j <= len(tasks):
                    removed_task= tasks.pop(j-1)
                    print(f"Removing task: {removed_task}...")
                    print("Task removed successfully ✔")
                else:
                    print("Invalid task number")
            else:
                print("No tasks to delete")
        elif (choose == 4):
            break
        else:
            print("invalid choose")


task_manager()
