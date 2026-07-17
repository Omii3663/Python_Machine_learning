import threading

# Function for Thread1
def display_forward():
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)

    print("Numbers from 1 to 50:")
    for i in range(1, 51):
        print(i, end=" ")
    print("\n")


# Function for Thread2
def display_reverse():
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)

    print("Numbers from 50 to 1:")
    for i in range(50, 0, -1):
        print(i, end=" ")
    print()


def main():
    # Create threads
    thread1 = threading.Thread(target=display_forward, name="Thread1")
    thread2 = threading.Thread(target=display_reverse, name="Thread2")

    # Start Thread1
    thread1.start()

    # Wait until Thread1 completes
    thread1.join()

    # Start Thread2
    thread2.start()

    # Wait until Thread2 completes
    thread2.join()

    print("\nExecution Completed.")


if __name__ == "__main__":
    main()
    