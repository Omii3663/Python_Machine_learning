from multiprocessing import Pool
import os

def odd_sum(n):

    total = 0

    for i in range(1, n + 1, 2):
        total = total + i

    print("Process ID:", os.getpid())
    print("Input Number:", n)
    print("Sum of Odd Numbers:", total)
    print()

    return total


def main():

    numbers = [1000000, 2000000, 3000000, 4000000]

    p = Pool()

    p.map(odd_sum, numbers)

    p.close()
    p.join()


if __name__ == "__main__":
    main()