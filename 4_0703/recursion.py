import time 

#Iterative implementation.
def fac(n: int):
    res = 1
    for i in range(1, n + 1):
        res *= i 

    return res

# Recursion implementation. 
def rec_fac(n: int):
    if n == 1:
        return 1
    return n * fac(n - 1)

# Iterative.
def square(numbers):
    return [n**2 for n in numbers]

# Recursive. 
def rec_square(numbers):
    if not numbers:
        return []
    return [numbers[0]**2] + rec_square(numbers[1:])


def main():
    test_fac = 500
    test_list = [10000, 100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 1000000]

    #Measure the time for each function. 
    start = time.perf_counter()
    fac(test_fac)
    end = time.perf_counter()
    print(f"Iterative factorial time: {end - start:.6f} s")

    start = time.perf_counter()
    rec_fac(test_fac)
    end = time.perf_counter()
    print(f"Recursive factorial time: {end - start:.6f} s")

    start = time.perf_counter()
    square(test_list)
    end = time.perf_counter()
    print(f"Iterative square time: {end - start:.7f} s")

    start = time.perf_counter()
    rec_square(test_list)
    end = time.perf_counter()
    print(f"Recursive square time: {end - start:.6f} s")


if __name__ == '__main__':
    main()

