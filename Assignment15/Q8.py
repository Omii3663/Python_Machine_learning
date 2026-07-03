# def Divisible(No):
#     if No % 3 == 0 and No % 5 == 0:
#         return No
    
divisible = lambda no : no if (no%3==0 and no%5==0) else None

def main():
    lst = [10,12,52,35,45,55,82,15,30]

    FData = list(filter(divisible,lst))
    print("Divisble by 3 and 5",FData)

if __name__ == "__main__":
    main()