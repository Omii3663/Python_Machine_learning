import pandas as pd
import matplotlib.pyplot as plt

def StudentPerformance(DataPath):
    Border = "-"*40
    #Read CSV
    df = pd.read_csv(DataPath)

    print(Border)

    #plt.scatter(df.index,df["StudyHours"],color="blue",marker="o", label="Study Hours")
    #plt.scatter(df.index,df["PreviousScore"],color="red",marker="X", label="Study Hours")

    StudyHours = df['StudyHours']
    PreviousScore = df['PreviousScore']

    plt.scatter(
        StudyHours,
        PreviousScore,
        s = 100,
        marker="o",
        alpha=0.8,
        linewidths=1,
        edgecolors="black",
        label = "StudyHours vs PreviousScore"
    )

    plt.title("Scatter plot")
    plt.xlabel("StudyHours")
    plt.ylabel("PreviousScor")

    plt.grid(True)

    plt.legend()
    plt.show()




def main():
    StudentPerformance("student_performance_ml.csv")

if __name__ == "__main__":
    main()