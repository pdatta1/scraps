def sequential_search(lyst, target):
    position = 0
    global iteration
    iteration = 0
    while position < len(lyst):
        iteration += 1
        if target == lyst[position]:
            return position
        position += 1
    return -1
