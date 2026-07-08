def ListAddition(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

def main():
    print("How many numbers do you want to add?")
    No = int(input())
    lst = []
    for _ in range(No):
        lst.append(int(input("Enter a number: ")))
    Ret = ListAddition(lst)
    print(f"Addition of Numbers is : {Ret}")

if __name__ == "__main__":
    main()