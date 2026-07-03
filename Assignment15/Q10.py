Counter = lambda no: no%2==0

def main():
    lst = [10,20,54,42,34,27,33,66]
    print("List of Input:", lst)

    FData = len(list(filter(Counter, lst)))
    print("Count of even numbers is:", FData)

if __name__ == "__main__":
    main()
