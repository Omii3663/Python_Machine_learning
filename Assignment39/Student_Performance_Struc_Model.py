import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
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
    # Step2 : Data Analysis (EDA)
    ##########################################

    print(Border)
    print("Step2 : Data Analysis (EDA)")
    print(Border)

    print("Shape of Data Set",df.shape)

    print("Columns Names Are :", list(df.columns))

    print("Missing Value per Columns Are :")
    print(df.isnull().sum())

    print("Class distribution Pass or Fail")

    print("Satatical report of Dataset :")
    print(df.describe())

    #####################################################
    # Step3 : Decide independent & dependent variables
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
    "SleepHours"
               ]

    X = df[feature_col]
    Y = df["FinalResult"]       # Depedent Variable

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=42)

    print("X Shape :",X.shape)
    print("Y Shape :",Y.shape)

    #####################################################
    # Step4 : visualization of dataset
    ####################################################

    print(Border)
    print("Step4 : visualization of dataset")
    print(Border)

    plt.hist(
        Y,                      #Countinous Data
        bins=5,                     #number of groups
        edgecolor = 'black',        #Border color   
        alpha = 0.8,            #Transperancy
        rwidth=0.9,             #relative

    )


    plt.title("Final Result")
    plt.xlabel("Pass and fail")
    plt.ylabel("")

    plt.grid(False)

    plt.legend()
    plt.show()

    
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

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.8, random_state=42)

    print("Data set splitting Activity Done ")

    print("X :", X.shape)  
    print("Y :", Y.shape) 

    print("X_train :",X_train.shape) 
    print("X_test :",X_test.shape) 

    print("Y_train :",Y_train.shape) 
    print("Y_test :",Y_test.shape)  

    #####################################################
    # Step6 : Bulid the model
    ####################################################

    print(Border)
    print("Step6 : Bulid the model")
    print(Border)

    model = DecisionTreeClassifier(max_depth=5)

    print("Model gets Created succesfully")

    #####################################################
    # Step7 : Train the model
    ####################################################

    print(Border)
    print("Step7 : Train the model")
    print(Border)

    model.fit(X_train,Y_train)

    print("Model tranaied sucssfully")

    #####################################################
    # Step8 : Test the model
    ####################################################

    print(Border)
    print("Step8 : Test the model")
    print(Border)

    Y_pred = model.predict(X_test)

    print("Model testing done")

    print("Expected Answer :")
    print(Y_test)

    print("Predicted answer :")
    print(Y_pred)

    #####################################################
    # Step9 : Evaluate the model performance
    ####################################################

    print(Border)
    print("Step9 : Evaluate the model performance")
    print(Border)

    accuracy = accuracy_score(Y_test,Y_pred)
    print("accuracy of model is :", accuracy*100)

    print("Confustion matrix")
    cm = confusion_matrix(Y_test,Y_pred)
    print(cm)

    print("Classification Report")
    print(classification_report(Y_test,Y_pred))


def main():
    Student_Perf("student_performance_ml.csv")

if __name__ == "__main__":
    main()