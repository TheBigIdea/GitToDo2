

def remove_task(tasks):
    result = tasks.copy()
    while True:
        for index, task in enumerate(result):
            print(index, task)
        break
    index_to_be_removed = int(input('anna poistettavan tehtävän numero: '))
    if index_to_be_removed in range(len(result)):
        result.pop(index_to_be_removed)
    else:
        print('mitään ei poistettu')
    return result


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
        

