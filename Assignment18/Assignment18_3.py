def ListMinimum(lst):
    min_val = lst[0]
    for i in lst:
        if i < min_val:
            min_val = i
    return min_val

def main():
    print("How many numbers do you want to Enter?")
    No = int(input())
    lst = []
    for _ in range(No):
        lst.append(int(input("Enter a number: ")))
    Ret = ListMinimum(lst)
    print(f"Minimum of Numbers is : {Ret}")

if __name__ == "__main__":
    main()