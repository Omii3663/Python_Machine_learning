from threading import Thread

def sum(No1,No2):
    return No1 + No2

def EvenFactor(No):
    factors = []
    total = 0
    for i in range(1, No + 1):
        if  No % i == 0 and i % 2 == 0:
            factors.append(i)
    
    for i in factors:
        total += i

    return total

    
def OddFactors(No):
    factors = []
    total = 0
    for i in range(1,No+1):
        if No % i == 0 and i % 2 != 0:
            factors.append(i)
    
    for i in factors:
        total += i

    return total
    
def main():
    print("Enter Number :")
    No = int(input())

    t1 = Thread(target=EvenFactor, args=(No,))
    t1.start()

    t2 = Thread(target=OddFactors,args=(No,))
    t2.start()

    t1.join()
    t2.join()

    print(f"The Sum of Even Factors : {t1}")
    print(f"The Sum of Odd Factors : {t2}")

    print("Exit from main Thread")

if __name__ == "__main__":
    main()

    