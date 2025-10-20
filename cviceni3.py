def my_range(start, stop, step=1):

    result = []
    actual = start

    while actual < stop:
        result.append(actual)
        actual += step

    return result
    """""
    start = 1
    stop = 3

    while start < stop:
        print (my_range)
        start += 1

    print(list(my_range(1, 3)))
   """
def while_enumerate(iterable, start=100):
    
    result = []
    index = 0
    while index <len(iterable):
        result.append((start + index, iterable[index]))
        index += 1

    return result

def for_enumerate(iterable, start=0):

    result = []
    #index = start
    #for el in iterable:
    #    result.append((index, el))
    #    index += 1
    #    return result
    for index in range(len(iterable)):
        result.append((start + index, iterable[index]))

    return result




if __name__ == "__main__":

    text = "abcdef"
    print(list(enumerate(text, 10)))
    print(while_enumerate(text, 100))
    print(for_enumerate(text))


    # print(list(range(1, 5)))
    # print(my_range(1, 10, 2))
    