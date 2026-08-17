import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

import matplotlib.pyplot as plt
import numpy as np

from sklearn.tree import plot_tree


from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report,
)

Border = "-"*40

def Student_Perf(DataPath):
    ##########################################
    # Step1 : Load the Data Set
    ##########################################

    print(Border)
    print("Step1 : Load the DataSet")
    print(Border)

    df = pd.read_csv(DataPath)

    print("Dataset Loaded Succefully")

    print("Initial enteries form dataset :")
    print(df.head())

    ##########################################
    # Step2 : Data Analysis (EDA) & Droping SleepHours
    ##########################################

    print(Border)
    print("Step2 : Data Analysis (EDA)")
    print(Border)

    print("Shape of Data Set",df.shape)

    df.columns = df.columns.str.strip()
    df = df.drop(columns= ['SleepHours'],errors = 'ignore')

    print("Columns Names Are :", list(df.columns))

    print("Missing Value per Columns Are :")
    print(df.isnull().sum())

    print("Class distribution Pass or Fail")

    print("Satatical report of Dataset :")
    print(df.describe())

    #####################################################
    # Step3 : Decide independent & dependent variables 
    # only with 2 colums StudyHours & Attendance
    ####################################################

    print(Border)
    print("Step3 : Decide independent & dependent variables")
    print(Border)

    # X : Independent Variable (features)
    # Y : Dependent Variable (lables)

    feature_col = [             #Independent Variables
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
               ]

    df["PerformanceIndex"] = (
    (df["StudyHours"] * 2) +
    df["Attendance"]
    )

    feature_col1 = [
        "StudyHours",
        "Attendance",
        "PerformanceIndex"
    ]



    X = df[feature_col]
    Y = df["FinalResult"]       # Depedent Variable
    Z = df[feature_col1]


    print("X Shape :",X.shape)
    print("Y Shape :",Y.shape)
    print("Z Shape :",Z.shape)

    #####################################################
    # Step4 : visualization of dataset
    ####################################################

    print(Border)
    print("Step4 : visualization of dataset")
    print(Border)

    
    plt.figure(figsize=(6, 4))

    df["FinalResult"].value_counts().plot(
        kind="bar",
        edgecolor="black"
    )

    plt.title("Student Pass / Fail Distribution")
    plt.xlabel("Final Result")
    plt.ylabel("Number of Students")

    plt.xticks(rotation=0)

    
    plt.show()

    #####################################################
    # Step5 : Split dataset for Traning & testing
    ####################################################

    print(Border)
    print("Step5 : Split dataset for Traning & testing")
    print(Border)

    Z_train, Z_test, Y_train, Y_test = train_test_split(Z, Y, train_size=0.8, random_state=42)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.8, random_state=42)

    print("Data set splitting Activity Done ")

    print("X :", X.shape)  
    print("Y :", Y.shape) 
    print("Z :", Z.shape) 

    print("X_train :",X_train.shape) 
    print("X_test :",X_test.shape) 

    print("Y_train :",Y_train.shape) 
    print("Y_test :",Y_test.shape)  

    print("Z_train :",Z_train.shape) 
    print("Z_test :",Z_test.shape) 

    #####################################################
    # Step6 : Bulid the model
    ####################################################

    print(Border)
    print("Step6 : Bulid the model")
    print(Border)

    model = DecisionTreeClassifier(max_depth=None)

    model2 = DecisionTreeClassifier(max_depth=5)

    print("Model gets Created succesfully")

    #####################################################
    # Step7 : Train the model &  use model.feature_importance_
    ####################################################

    print(Border)
    print("Step7 : Train the model")
    print(Border)

    model.fit(X_train,Y_train)

    model2.fit(Z_train,Y_train)

    print(" Both Model tranaied sucssfully")

    print(model.feature_importances_)

    #####################################################
    # Step8 : Test the model
    ####################################################

    print(Border)
    print("Step8 : Test the model")
    print(Border)

    Y_pred = model.predict(X_test)
    Y_pred2 = model2.predict(Z_test)

    print("Model testing done")

    print("Expected Answer:")
    print(Y_test)

    print("Predicted answer  from Model1:")
    print(Y_pred)

    print("Predicted answer  from Model1:")
    print(Y_pred2)

    #####################################################
    # Step9 : Evaluate the model performance
    ####################################################

    print(Border)
    print("Step9 : Evaluate the model performance")
    print(Border)

    print(Border)
    accuracy = accuracy_score(Y_test,Y_pred)
    print("accuracy of model is :", accuracy*100)
    print(Border)

    accuracy2 = accuracy_score(Y_test,Y_pred2)
    print("accuracy of model is :", accuracy2*100)

    if (accuracy > accuracy2):
        print("First Model is Better")
    elif (accuracy2>accuracy):
        print("Second Model is Better")
    else:
        print("Both Model Has Same Accuracy")

    print("Confustion matrix")
    cm = confusion_matrix(Y_test,Y_pred)
    print(cm)

    disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Fail", "Pass"]
    )
    
    disp.plot()
    plt.show()

    print("Classification Report")
    print(classification_report(Y_test,Y_pred))


    print(Border)
    Test_check = pd.DataFrame([
    [7, 85, (7 * 2) + 85],
    [2, 65, (2 * 2) + 65],
    [5, 70, (5 * 2) + 70],
    [6, 80, (6 * 2) + 80],
    [1, 60, (1 * 2) + 60]
    ],
    columns=["StudyHours", "Attendance","PerformanceIndex"]
    )

    Result = model2.predict(Test_check)

    for i in range(len(Result)):
        if Result[i] == 1:
            print(f"Student No {i + 1} is Pass")
        elif Result[i] == 0:
            print(f"Student No {i + 1} is Fail")

    print(Border)
    for actual, predicted in zip(Y_test, Y_pred):
        print(f"Actual: {actual}, Predicted: {predicted}")


    print(Border)

    plot_tree(
    model,
    feature_names=feature_col,
    class_names=["Fail", "Pass"],
    filled=True
    )

    plt.title("Decision Tree - Student Performance")
    plt.show()

    print(Border)
    plot_tree(
    model2,
    feature_names=feature_col1,
    class_names=["Fail", "Pass"],
    filled=True
    )

    plt.title("Decision Tree Model 2")
    plt.show()

    print(Border)

    print("Testing Accuracy :",accuracy * 100, "%")
    Y_train_pred = model.predict(X_train)
    training_Acc = accuracy_score(Y_train, Y_train_pred)
    print("Training Accuracy :", training_Acc * 100, "%")

def main():
    Student_Perf("student_performance_ml.csv")

   

if __name__ == "__main__":
    main()