import todo

print('Welcome to simple task manager!\n')

print('Please read below instrustions carefully. \n')
print('Press 1 to add task to the list.')
print('Press 2 to view tasks.')
print('Press 3 to remove task from the list.')
print('Press 4 to exit from the program.')

def main(num):
    match num:
        case 1:
            todo.add_task()
        case 2:
            todo.view_tasks(todo.tasks)
        case 3:
            todo.remove_task()
        case 4:
            print('Good bye!')
        case _:
            print('Out of range instructions. Goodbye!')

main(int(input('Please enter your choice: ')))