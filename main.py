from todo import *

print('Welcome to Simple To Do List manager!\n')

def main():
    while True:
        try:
            choice = int(input('Please enter your choice (1: Add, 2: View, 3: Remove, 4: Exit): '))
            match choice:
                case 1:
                    add_task()
                case 2:
                    view_tasks(tasks)
                case 3:
                    remove_task()
                case 4:
                    print("Goodbye!")
                    break
                case _:
                    print('Out of range instructions. Please try again.')
        except ValueError:
            print("Please enter a valid number.")

main()

