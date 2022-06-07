def get_max_value(some_value) :
    """Find the max value in a range of values.
    Pass in a complex data type, function will loop through and print out the highest value"""

    max_value = some_value[0]
    length = len(some_value)

    for i in range(1, length) :
        if some_value[i] > max_value :
            max_value = some_value[i]
    
    print("Max value is:", max_value)


a_list = [1, 2, 3, 4, 1, 6, 60, 3, 5, 7]

get_max_value(a_list)