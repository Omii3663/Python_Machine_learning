from multiprocessing import Pool
import time

def power_sum(n):

    total = 0

    for i in range(1, n + 1):
        total = total + (i ** 5)

    return total


def main():

    numbers = [
        1000000,
        2000000,
        3000000,
        4000000
    ]

    start = time.time()

    p = Pool()

    result = p.map(power_sum, numbers)

    p.close()
    p.join()

    end = time.time()

    print("Results:")
    print(result)

    print("Execution Time :", end - start, "seconds")


if __name__ == "__main__":
    main()