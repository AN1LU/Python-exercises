def todo_list():
    """
    This function returns a list of tasks to be completed.
    Each task is represented as a dictionary with 'task' and 'status'.
    """
    tasks = [
        {"task": "Buy groceries", "status": "pending"},
        {"task": "Clean the house", "status": "completed"},
        {"task": "Finish project report", "status": "pending"},
        {"task": "Call mom", "status": "completed"},
    ]
    return tasks

def add_task(task, status="pending"):
    """
    This function adds a new task to the todo list.
    
    :param task: The task description
    :param status: The status of the task (default is 'pending')
    :return: A dictionary representing the new task
    """
    task = input("Enter the task name: ")
    status = input("Enter the task status (pending/completed): ")
    return {"task": task, "status": status}

def remove_task(task_list, task):
    """
    This function removes a task from the todo list.
    
    :param task_list: The current list of tasks
    :param task: The task to be removed
    :return: The updated list of tasks
    """
    return [t for t in task_list if t["task"] != task]

def update_task(task_list, task, new_status):
    """
    This function updates the status of a task in the todo list.
    
    :param task_list: The current list of tasks
    :param task: The task to be updated
    :param new_status: The new status for the task
    :return: The updated list of tasks
    """
    for t in task_list:
        if t["task"] == task:
            t["status"] = new_status
            break
    return task_list

def display_tasks(task_list):
    """
    This function displays all tasks in the todo list.
    
    :param task_list: The current list of tasks
    """
    for t in task_list:
        print(f"Task: {t['task']}, Status: {t['status']}")

def main():
    """
    Main function to run the todo list application.
    """
    tasks = todo_list()
    display_tasks(tasks)
    
    while True:
        action = input("Choose an action: add, remove, update, display, exit: ").strip().lower()
        if action == "add":
            new_task = add_task("", "")
            tasks.append(new_task)
        elif action == "remove":
            task_to_remove = input("Enter the task to remove: ")
            tasks = remove_task(tasks, task_to_remove)
        elif action == "update":
            task_to_update = input("Enter the task to update: ")
            new_status = input("Enter the new status (pending/completed): ")
            tasks = update_task(tasks, task_to_update, new_status)
        elif action == "display":
            display_tasks(tasks)
        elif action == "exit":
            break
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()  