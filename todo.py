tasks = []
def remove_task():
    view_tasks()
    index_to_be_removed = int(input('Give an index of task to be removed: '))
    if index_to_be_removed in range(1, len(tasks)+1):
        tasks.pop(index_to_be_removed - 1)
        print(f"Task {index_to_be_removed} succesfully removed")
    else:
        print('Nothing was removed')




# Lisää Todo
def add_task():
    task = input("Input task: ")
    tasks.append(task)
    print("Task added successfully!")

# Katso Todot
def view_tasks(): 
    print("-----TASKS-----")
    for i in range(len(tasks)):
        print(f"{i + 1}: {tasks[i]}")
        

