def remove_task():
    view_tasks(tasks)
    index_to_be_removed = int(input('Give an index of task to be removed: '))
    if index_to_be_removed in range(1, len(tasks)+1):
        tasks.pop(index_to_be_removed - 1)
    else:
        print('Nothing was removed')


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
        

