from threading import Thread
import time
def Even():
    for i in range(1,11):
        if i % 2 == 0:
            return i

def Odd():
    for i in range(1,11):
        if i % 2 != 0:
            return i

def main():
    start_time = time.perf_counter()
    t1 = Thread(target=Even)
    t2 = Thread(target=Odd)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.perf_counter()
    print(f"Time Required is : {end_time-start_time:.4f}")

if __name__ == "__main__":
    main()

    