def move(my_list, direction):

    # Finds the index of the one in the list
    index_of_one = my_list.index(1)

    # Move the one to the left or to the right
    if direction == 'right':
        if index_of_one != len(my_list) - 1:
            my_list[index_of_one] = 0
            my_list[index_of_one + 1] = 1

    elif direction == 'left':
        if index_of_one != 0:
            my_list[index_of_one] = 0
            my_list[index_of_one - 1] = 1

    return my_list
