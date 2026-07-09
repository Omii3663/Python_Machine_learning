from functools import reduce
def Even(No):
    if No % 2 == 0:
        return No
    
def Square(No):
    return No * No

def Add(No1,No2):
    return No1 + No2

def main():
    print("How many Numbers Do you want to Enter :")
    No = int(input())
    lst = []
    for i in range(No):
        lst.append(int(input("Enter Number :")))

    FData = list(filter(Even,lst))
    print("List After Filter :", FData)

    MData = list(map(Square,FData))
    print("List After Map :", MData)

    RData = reduce(Add,MData)
    print("List After Reduce :", RData)

if __name__ == "__main__":
    main()