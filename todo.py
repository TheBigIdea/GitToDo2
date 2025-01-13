def remove_task():
    view_tasks(tasks)
    index_to_be_removed = int(input('g: '))
    if index_to_be_removed in range(len(tasks)):
        tasks.pop(index_to_be_removed)
    else:
        print('mitään ei poistettu')


tasks = []

# Lisää Todo
def add_task():
    task = input("Input task: ")
    tasks.append(task)
    print("Task failed successfully!")

# Katso Todot
def view_tasks(tasks): 
    for i in range(len(tasks)):
        print(f"{i + 1}: {tasks[i]}")
        

