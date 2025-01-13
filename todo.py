def remove_task(tasks):
    result = tasks.copy()
    for index, task in enumerate(result):
        print(index, task)
    index_to_be_removed = int(input('anna poistettavan tehtävän numero: '))
    if index_to_be_removed in range(len(result)):
        result.pop(index_to_be_removed)
    else:
        print('mitään ei poistettu')
    return result