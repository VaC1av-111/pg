def fibonacci (maximum):
    result = [1]
    value = 1
    while value <= maximum:
        result.append(value)
        value = result[-1] + result[-2]
    return result

if __name__ == "__main__":
    import sys
    maximum = int(sys.argv[1])
    print(fibonacci(maximum))