import os

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):  
            print(f"{i}. {task}")

def add_task(tasks, new_task):
    tasks.append(new_task)  
    print("Task added successfully.")

def update_task(tasks, index, updated_task):
    if 1 <= index <= len(tasks):
        tasks[index - 1] = updated_task  
        print("Task updated successfully.")
    else:
        print("Invalid task index.") 

def delete_task(tasks, index):
    if 1 <= index <= len(tasks):  
        deleted_task = tasks.pop(index - 1)  
        print(f"Task '{deleted_task}' deleted successfully.")
    else:
        print("Invalid task index.")

def save_task_to_file(file_path, tasks):
    with open(file_path, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

def load_task_from_file(file_path):
    tasks = []  
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            tasks = file.read().splitlines()
    return tasks

def main():
    file_path = "Todo_list.txt"
    tasks = load_task_from_file(file_path)
    while True:
        print("\n===== To-Do List =====")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Save & Exit")
        choice = input("Enter your choice (1-5): ") 
        if choice == "1":
            show_tasks(tasks)  
        elif choice == "2":
            new_task = input("Enter the task to add: ")
            add_task(tasks, new_task)
        elif choice == "3":
            index = int(input("Enter the task index to update: "))
            updated_task = input("Enter the updated task: ") 
            update_task(tasks, index, updated_task)
        elif choice == "4":
            index = int(input("Enter the task index to delete: "))
            delete_task(tasks, index)
        elif choice == "5":
            save_task_to_file(file_path, tasks)
            print("Tasks saved. Exiting...")
            break
        else: 
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
