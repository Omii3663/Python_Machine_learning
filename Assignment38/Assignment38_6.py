import pandas as pd
import matplotlib.pyplot as plt

def StudentPerformance(DataPath):
    Border = "-"*40
    #Read CSV
    df = pd.read_csv(DataPath)

    print(Border)

    StudyHours = df['StudyHours']


    plt.hist(
        StudyHours,
        bins=5,
        edgecolor="black",
        alpha = 0.8,
        rwidth = 0.9
    )

    plt.title("Study Hours")
    plt.xlabel("Hours")
    plt.ylabel("Frequece of Hours")

    plt.show()




def main():
    StudentPerformance("student_performance_ml.csv")

if __name__ == "__main__":
    main()