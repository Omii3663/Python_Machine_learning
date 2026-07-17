import threading

# Global variables to store results
sum_result = 0
product_result = 1

# Function to calculate sum
def calculate_sum(numbers):
    global sum_result

    sum_result = 0
    for i in numbers:
        sum_result = sum_result + i

    print("Thread Name :", threading.current_thread().name)
    print("Thread ID :", threading.get_ident())
    print("Sum =", sum_result)
    print()


# Function to calculate product
def calculate_product(numbers):
    global product_result

    product_result = 1
    for i in numbers:
        product_result = product_result * i

    print("Thread Name :", threading.current_thread().name)
    print("Thread ID :", threading.get_ident())
    print("Product =", product_result)
    print()


def main():

    numbers = list(map(int, input("Enter list elements: ").split()))

    # Create threads
    t1 = threading.Thread(target=calculate_sum, args=(numbers,), name="Thread1")
    t2 = threading.Thread(target=calculate_product, args=(numbers,), name="Thread2")

    # Start threads
    t1.start()
    t2.start()

    # Wait for threads to finish
    t1.join()
    t2.join()

    # Display results in main thread
    print("Results returned to Main Thread")
    print("Sum of Elements =", sum_result)
    print("Product of Elements =", product_result)


if __name__ == "__main__":
    main()