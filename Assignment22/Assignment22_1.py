from multiprocessing import Pool

# Function to calculate sum of squares
def sum_of_squares(n):
    total = 0

    for i in range(1, n + 1):
        total = total + (i * i)

    return total


def main():
    numbers = [1000000, 2000000, 3000000, 4000000]

    p = Pool()

    result = p.map(sum_of_squares, numbers)

    p.close()
    p.join()

    print("Result:")
    print(result)


if __name__ == "__main__":
    main()