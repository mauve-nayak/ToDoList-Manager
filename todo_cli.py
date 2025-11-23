f1 = 'todo_list.txt'
tasks = []
def load_tasks():
    global tasks
    try:
        with open(f1,'r') as file:
            tasks = []
            for line in file.readlines():
                tasks.append(line.strip())
    except FileNotFoundError:
        tasks = []
def save_tasks():
    with open(f1,'w') as file:
        for task in tasks:
            file.write(task + '\n')
def add_task():
    description = input("Enter the task description: ")
    new_task = f"[ ] {description}"
    tasks.append(new_task)
    save_tasks()
    print(f"\n✅ Task added: '{description}'")

def view_tasks():
    if not tasks:
        print("\nYour to-do list is empty! 🚀")
        return
    print("\n--- 📝 Current To-Do List ---")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")
    print("----------------------------")

def mark_done():
    index = input("Enter the number of the task to mark as done: ")
    try:
        task_index = int(index) - 1
    except ValueError:
        print("\n❌ Invalid input. Please enter a valid number.")
        return
    if 0 <= task_index < len(tasks):
        if tasks[task_index].startswith('[ ]'):
            tasks[task_index] = tasks[task_index].replace('[ ]', '[x]', 1)
            save_tasks()
            print(f"\n🎉 Task {index} marked as done.")
        else:
            print(f"\nℹ️ Task {index} is already done!")
    else:
        print(f"\n❌ Error: No task found with index {index}.")
def delete_task():
    view_tasks()    
    if not tasks:
        return
    index = input("Enter the number of the task to delete: ")
    try:
        task_index = int(index) - 1
    except ValueError:
        print("\n❌ Invalid input. Please enter a valid number.")
        return

    if 0 <= task_index < len(tasks):
        deleted_task = tasks.pop(task_index)
        save_tasks()
        print(f"\n🗑️ Task deleted: {deleted_task}")
    else:
        print(f"\n❌ Error: No task found with number {index}.")
def main():
    load_tasks()
    while True:
        print("\n===================================")
        print("  PYTHON SIMPLE TO-DO LIST")
        print("===================================")
        print("1. Add a New Task")
        print("2. View All Tasks")
        print("3. Mark Task as Done")
        print("4. Delete a Task")
        print("5. Exit Application")
        choice = input("\nEnter your choice (1-5): ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            view_tasks()
            mark_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("\nGoodbye! Your to-do list has been saved. 👋")
            break
        else:
            print("\n🛑 Invalid choice. Please enter a number between 1 and 5.")
if __name__ == "__main__":

    main()

