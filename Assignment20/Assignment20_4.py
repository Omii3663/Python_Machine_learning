import threading

# Function to count lowercase letters
def count_small(text):
    count = 0
    for ch in text:
        if ch.islower():
            count += 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Lowercase Characters :", count)
    print()


# Function to count uppercase letters
def count_capital(text):
    count = 0
    for ch in text:
        if ch.isupper():
            count += 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Uppercase Characters :", count)
    print()


# Function to count digits
def count_digits(text):
    count = 0
    for ch in text:
        if ch.isdigit():
            count += 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Digits :", count)
    print()


def main():
    text = input("Enter a string: ")

    # Create threads
    small = threading.Thread(target=count_small, args=(text,), name="Small")
    capital = threading.Thread(target=count_capital, args=(text,), name="Capital")
    digits = threading.Thread(target=count_digits, args=(text,), name="Digits")

    # Start threads
    small.start()
    capital.start()
    digits.start()

    # Wait for threads to finish
    small.join()
    capital.join()
    digits.join()

    print("Execution Completed.")


if __name__ == "__main__":
    main()