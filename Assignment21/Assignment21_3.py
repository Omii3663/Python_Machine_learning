import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter

    for i in range(1000):
        lock.acquire()

        counter = counter + 1

        lock.release()

    print(threading.current_thread().name, "Completed")


def main():

    t1 = threading.Thread(target=increment, name="Thread1")
    t2 = threading.Thread(target=increment, name="Thread2")
    t3 = threading.Thread(target=increment, name="Thread3")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Final Counter Value :", counter)


if __name__ == "__main__":
    main()