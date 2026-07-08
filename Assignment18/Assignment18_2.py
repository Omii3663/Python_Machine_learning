def ListMaximum(lst):
    max_val = lst[0]
    for i in lst:
        if i > max_val:
            max_val = i
    return max_val

def main():
    print("How many numbers do you want to Enter?")
    No = int(input())
    lst = []
    for _ in range(No):
        lst.append(int(input("Enter a number: ")))
    Ret = ListMaximum(lst)
    print(f"Maximum of Numbers is : {Ret}")

if __name__ == "__main__":
    main()