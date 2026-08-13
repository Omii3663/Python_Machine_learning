import pandas as pd

def StudentPerformance(DataPath):
    Border = "-"*40
    #Read CSV
    df = pd.read_csv(DataPath)

    print(Border)
    print(df.shape[0])

    print(Border)
    X = df['FinalResult']
    PassCount = 0
    FailCount = 0
    for i in X:
        if (i==1):
            PassCount += 1
        elif(i==0):
            FailCount +=1

    print("Students Passed : ",PassCount)
    print("Students Fail :",FailCount)
    print(Border)
    
            

def main():
    StudentPerformance("student_performance_ml.csv")

if __name__ == "__main__":
    main()