from multiprocessing import Pool
import os

def odd_count(n):

    count = 0

    for i in range(1, n + 1, 2):
        count = count + 1

    print("Process ID:", os.getpid())
    print("Input Number:", n)
    print("Odd Number Count:", count)
    print()

    return count


def main():

    numbers = [1000000, 2000000, 3000000, 4000000]

    p = Pool()

    p.map(odd_count, numbers)

    p.close()
    p.join()


if __name__ == "__main__":
    main()