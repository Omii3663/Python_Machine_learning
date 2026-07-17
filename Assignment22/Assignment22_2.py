from multiprocessing import Pool
import os

def factorial(n):

    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    print("Process ID :", os.getpid())
    print("Input Number :", n)
    print("Factorial :", fact)
    print()

    return fact


def main():

    numbers = [10, 15, 20, 25]

    p = Pool()

    p.map(factorial, numbers)

    p.close()
    p.join()


if __name__ == "__main__":
    main()