class Node:
    def search_list(self, target, lyst):
        global iterations
        position = 0

        while position < len(lyst):
            iterations = + 1
            if target == lyst[position]:
                return position
            position += 1
        return -1


def main():
    lyst = [34, 12, 45, 12, 43, 64]
    node = Node()
    input_result = int(input("Enter Target"))
    result = node.search_list(input_result, lyst)
    if result == -1:
        print("Target found at")
    else:
        print("Target not found")


main()
