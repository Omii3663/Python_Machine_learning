def count_frequency_check(lst, check_value):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency.get(check_value, 0)

def main():
    print("How many numbers do you want to Enter?")
    No = int(input())
    lst = []
    for _ in range(No):
        lst.append(int(input("Enter a number: ")))
    check_value = int(input("Enter a number to check its frequency: "))
    freq = count_frequency_check(lst, check_value)
    print(f"Frequency of {check_value} is: {freq}")

if __name__ == "__main__":
    main()