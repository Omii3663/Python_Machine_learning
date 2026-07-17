import threading

# Function to check prime number
def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


# Thread function to display prime numbers
def prime_numbers(numbers):
    print("Thread Name :", threading.current_thread().name)
    print("Thread ID :", threading.get_ident())

    print("Prime Numbers:")
    for num in numbers:
        if is_prime(num):
            print(num, end=" ")
    print()


# Thread function to display non-prime numbers
def non_prime_numbers(numbers):
    print("Thread Name :", threading.current_thread().name)
    print("Thread ID :", threading.get_ident())

    print("Non-Prime Numbers:")
    for num in numbers:
        if not is_prime(num):
            print(num, end=" ")
    print()


def main():
    numbers = list(map(int, input("Enter numbers: ").split()))

    t1 = threading.Thread(target=prime_numbers, args=(numbers,), name="Prime")
    t2 = threading.Thread(target=non_prime_numbers, args=(numbers,), name="NonPrime")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Execution Completed")


if __name__ == "__main__":
    main()