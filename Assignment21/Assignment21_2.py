import threading

def maximum(numbers):
    max_num = numbers[0]

    for i in numbers:
        if i > max_num:
            max_num = i

    print("Thread Name :", threading.current_thread().name)
    print("Thread ID :", threading.get_ident())
    print("Maximum Number :", max_num)


def minimum(numbers):
    min_num = numbers[0]

    for i in numbers:
        if i < min_num:
            min_num = i

    print("Thread Name :", threading.current_thread().name)
    print("Thread ID :", threading.get_ident())
    print("Minimum Number :", min_num)


def main():
    numbers = list(map(int, input("Enter numbers: ").split()))

    t1 = threading.Thread(target=maximum, args=(numbers,), name="Thread1")
    t2 = threading.Thread(target=minimum, args=(numbers,), name="Thread2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Execution Completed")


if __name__ == "__main__":
    main()