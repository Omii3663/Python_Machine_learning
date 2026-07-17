import threading

def extract_even(numbers):
    even_nums = [n for n in numbers if n % 2 == 0]
    print(f"EvenList Thread - Even Numbers: {even_nums}")
    print(f"EvenList Thread - Sum: {sum(even_nums)}\n")

def extract_odd(numbers):
    odd_nums = [n for n in numbers if n % 2 != 0]
    print(f"OddList Thread - Odd Numbers: {odd_nums}")
    print(f"OddList Thread - Sum: {sum(odd_nums)}\n")

def main():
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Create threads
    even_list_thread = threading.Thread(target=extract_even, args=(input_list,))
    odd_list_thread = threading.Thread(target=extract_odd, args=(input_list,))
    
    # Start threads concurrently
    even_list_thread.start()
    odd_list_thread.start()
    
    # Wait for both threads to finish
    even_list_thread.join()
    odd_list_thread.join()
    
    print("Execution completed.")

if __name__ == "__main__":
    main()