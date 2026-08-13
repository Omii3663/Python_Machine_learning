import pandas as pd

def StudentPerformance(DataPath):
    Border = "-"*40
    #Read CSV
    df = pd.read_csv(DataPath)

    StudyHours = df['StudyHours']
    sum = 0
    count = 0
    
    for i in StudyHours:
        sum += i
        count += 1

    Avg = sum/count

    print("Average StudyHours :", Avg)
    print(Border)

    Attendance = df['Attendance']
    sum1 = 0
    count1 = 0

    for i in StudyHours:
        sum1 += i
        count1 += 1
    
    Avg1 = sum1/count1

    print("Average Attendance :", Avg1)
    print(Border)
    
    PreviousScore = df['PreviousScore']
    print(f"Maxmium PreviousScore is :{max(PreviousScore)}")
    print(Border)

    SleepHours = df['SleepHours']
    print(f"Minimum SleepHours are :{min(SleepHours)}")
    print(Border)

def main():
    StudentPerformance("student_performance_ml.csv")

if __name__ == "__main__":
    main()