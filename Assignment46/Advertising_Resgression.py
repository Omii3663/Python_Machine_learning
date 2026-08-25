import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error



Border = '-'*40
#----------------------------------------------------
# step 1 : Load Data
#----------------------------------------------------
# Funcation Name :  LoadData
# Description    :  Load the dataset from csv
# Input          :  csv file
# output         :  Data frame
# Author         :  Omkar Ramchandra Kolte
# Date           :  24/08/2026
#-----------------------------------------------------
def LoadData():

    df = pd.read_csv("Advertising.csv")
    print(df.head())
    print(Border)

    return df

#----------------------------------------------------
# step 2 : Clean Prepare and Manipulate Data
#----------------------------------------------------
# Funcation Name :  Preprocessing 
# Description    :  Clean Prepare and Manipulate Data (EDA)
# Input          :  Data frame
# output         :  Data frame
# Author         :  Omkar Ramchandra Kolte
# Date           :  24/08/2026
#-----------------------------------------------------

def Preprocessing(df):

    print("Null values in columns :")
    print(Border)
    print(df.isnull().sum())
    print(Border)

    df = df.drop('Unnamed: 0',axis=1)
    print(df.head())
    print(Border)


    print("Statistical Summary")
    print(Border)
    print(df.describe())
    print(Border)

    print("Co-relation : ")
    print(Border)
    print(df.corr())


    return df

#----------------------------------------------------
# step 3 : Train Model
#----------------------------------------------------
# Funcation Name :  TrainModel
# Description    :  Train Model spliting & Traing & testing
# Input          :  Data frame
# output         :  spliting & Trained model
# Author         :  Omkar Ramchandra Kolte
# Date           :  24/08/2026
#-----------------------------------------------------

def TrainModel(df):

    X = df[["TV","radio","newspaper"]]

    Y = df["sales"]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    model = LinearRegression()

    model = model.fit(X_train,Y_train)

    return model,X_train, X_test, Y_train, Y_test

#----------------------------------------------------
# step 4 : Test Model
#----------------------------------------------------
# Funcation Name :  TestModel
# Description    :  Model Testing
# Input          :  Trained Model
# output         :  Tested Model / Y_pred,
# Author         :  Omkar Ramchandra Kolte
# Date           :  24/08/2026
#-----------------------------------------------------

def TestModel(model,X_test,Y_test):

    Y_pred = model.predict(X_test)

    print(Border)
    print("Expected Answer :")
    print(Border)
    print(Y_test[:3])

    print(Border)
    print("Predicted Answer :")
    print(Border)
    print(Y_pred[:3])

    return Y_pred

#----------------------------------------------------
# step 5 : Evaluate Model
#----------------------------------------------------
# Funcation Name :  EvaluateModel
# Description    :  Evaluate Model How model is performing
# Input          :  Model
# output         :  Display Evaluation 
# Author         :  Omkar Ramchandra Kolte
# Date           :  24/08/2026
#-----------------------------------------------------

def EvaluateModel(model,Y_test,Y_pred):

    MSE = mean_squared_error(Y_test,Y_pred)

    RMSE = np.sqrt(MSE)

    R2 = r2_score(Y_test,Y_pred)

    print(Border)
    print("Mean Squared Error :")
    print(Border)
    print(MSE)

    print(Border)
    print("Square_Root of MSE :")
    print(RMSE)

    print(Border)
    print("R2 :")
    print(R2)

    print(Border)
    print("Coifficent : ")

    print("TV Coifficent :",model.coef_[0])
    print("radio Coifficent :",model.coef_[1])
    print("newspaper Coifficent :",model.coef_[2])

    print(Border)
    print("Intercept :")
    print(model.intercept_)
    



#----------------------------------------------------
# Funcation Name :  main
# Description    :  Entry point function
# Input          :  none
# output         :  Data frame
# Author         :  Omkar Ramchandra Kolte
# Date           :  24/08/2026
#-----------------------------------------------------

def main():
    df = LoadData()

    df = Preprocessing(df)

    model,X_train, X_test, Y_train, Y_test = TrainModel(df)

    Y_pred = TestModel(model,X_test,Y_test)

    EvaluateModel(model,Y_test,Y_pred)


if __name__ == "__main__":
    main()