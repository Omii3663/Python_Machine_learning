import pandas as pd

def StudentPerformance(DataPath):
    Border = "-"*40
    #Read CSV
    df = pd.read_csv(DataPath)

    print(Border)

    Result = df['FinalResult'].value_counts(normalize=True)
    print(Result)
    print(Border)

    print("Percentage of Pass Student :" ,Result[1]*100)
    print(Border)

    print("Percentage of Fail Student :" ,Result[0]*100)
    print(Border)

def main():
    StudentPerformance("student_performance_ml.csv")

if __name__ == "__main__":
    main()