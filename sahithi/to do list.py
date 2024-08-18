import os

FILE_NAME = 'to-do-list.sahi'

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

def add_task():
    task = input("Enter the task:")
    task.append({'task': task, 'done': False})
    print("Task added!")

def mark_task_done(tasks):
    display_tasks(tasks)
    try:
        task_id = int(input("Enter the task number to mark as done: ")) - 1
        if 0 <= task_id < len(tasks):
            tasks[task_id]['done'] = True 
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except valueError:
        print("Invalide input ! \n Please enter a number.")
def remove_task(tasks):
    display_tasks(tasks)
    try:
        task_id = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_id < len(tasks):
            tasks.pop(task_id)
            print("Task removed!")
        else:
            printf("Invalide task number.")
    except ValueError:
        print("Invalid input. \n Please enter a number.")
def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file)
def main():
    tasks = load_tasks()

    while True:
        print("\n****TO-DO LIST MENU****")
        print("1. ADD NEW TASK")
        print("2. MARK TASK")
        print("3. REMOVE TASK")
        print("4. SAVE TASK")

        choice = input("choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            mark_task_done(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            save_tasks(tasks)
            print("Tasks saved successfully! ")
            break
        else:
            print("Invalid choice, \n Please choose again.")
if __name__ == "__main__":
    main()