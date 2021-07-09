def sequential_search(target, lyst):
    position = 0
    global iterations
    iterations = 0

    while position < len(lyst):
        if lyst[position] == target:
            return position
        position += 1
        iterations += 1


def main():
    lyst = [15, 334, 53, 2, 32, 31, 567, 7, 867, 556, 546, 5, 6]

    result = sequential_search(31, lyst)
    if result != -1:
        print("Target found at index : %s" % result)
    else:
        print("Target not Found!")


main()
