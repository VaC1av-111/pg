def faktorial(n):
    
    if n == 0 or n == 1:
        return 1
    return n * faktorial(n - 1)

def faktorial2(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result



if __name__ == "__main__":
    print(faktorial(5))
    print(faktorial(0))
    print(faktorial(3))