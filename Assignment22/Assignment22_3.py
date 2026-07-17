from multiprocessing import Pool

def is_prime(num):

    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def prime_count(n):

    count = 0

    for i in range(2, n + 1):
        if is_prime(i):
            count = count + 1

    return count


def main():

    numbers = [10000, 20000, 30000, 40000]

    p = Pool()

    result = p.map(prime_count, numbers)

    p.close()
    p.join()

    for i in range(len(numbers)):
        print("Prime count between 1 and", numbers[i], "=", result[i])


if __name__ == "__main__":
    main()
    