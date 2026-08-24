import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler


Boreder = '-'*40
# step 1 : Load Data
#----------------------------------------------------
# Funcation Name : StudentMarks
# Description    : Create Data Set 
# Input          : None
# output         : Data frame
# Author         : Omkar Ramchandra Kolte
# Date           : 21/08/2026
#-----------------------------------------------------
def StudentMarks():

    data ={
        'Name' : ['Amit','Sager', 'Pooja'],
        'Math' : [85,90,78],
        'Science': [92,88,80],
        'English': [75,85,82]
    }

    data2 ={
        'Name' : ['Amit','Sager', 'Pooja'],
        'Math' : [np.nan,90,78],
        'Science': [92,88,80],
        'English': [75,85,82]
    }

    df2 = pd.DataFrame(data2)

    df = pd.DataFrame(data)

    print(df)
    print(Boreder)

    print(df2)
    print(Boreder)

    print("Descriptive Statistic : \n",df.describe())

    print(Boreder)

    df['Total'] = df[['Math','Science', 'English']].sum(axis=1)
    print(df)

    return df,df2

# step 2 : Check who score > 85 in Science 
#----------------------------------------------------
# Funcation Name : ChkGrater
# Description    : Check who score grater then 85 in Science
# Input          : Data frame
# output         : list of Students
# Author         : Omkar Ramchandra Kolte
# Date           : 21/08/2026
#-----------------------------------------------------

def ChkGrater(df):
    # Lst = []

    # for i in range(len(df)):
    #     if df['Science'][i] > 85 :
    #         Lst.append(df['Name'][i])

    #.loc[] syntax
    #The general syntax is: df.loc[rows, columns]
    #df.loc[0, 'Name'] --> for Spcific Row
    #df.loc[:, 'Name'] --> select a column & The ':' (colon) means all rows.
    #df.loc[condition, column] 

    Lst = df.loc[df['Science']>85,'Name'].tolist()

    return Lst

# step 3 : Sort Data in Decending Order & replace Some Names
#----------------------------------------------------
# Funcation Name : SortData
# Description    : Sort Data in Decending Order & replace Some Names
# Input          : Data frame
# output         : Sorted Data frame
# Author         : Omkar Ramchandra Kolte
# Date           : 21/08/2026
#-----------------------------------------------------

def SortData(df):

    print(Boreder)
    print("Replacing names Pooja to puja..")
    print(Boreder)

    df['Name'] = df['Name'].replace('Pooja','puja')

    print(df)
    print(Boreder)

    #Pandas sort_values() is fun for this  by='Total' for Columns Names & ascending=False/Ture 
    # reset_index(drop=True) reset index so start form 0,1,2 without it will not change index only values are in decending oreder
    #df = df.sort_values(by='Total', ascending=False).reset_index(drop=True)

    for i in range(len(df)):
        for j in range(0,len(df)-i - 1):

                if df.loc[j, 'Total'] < df.loc[j + 1, 'Total']:

                    #Swap only Total columns Values
                    # temp = df.loc[j, 'Total']
                    # df.loc[j, 'Total'] = df.loc[j + 1, 'Total']
                    # df.loc[j + 1, 'Total'] = temp

                    # Swap complete rows
                    temp = df.loc[j].copy()
                    df.loc[j] = df.loc[j + 1]
                    df.loc[j + 1] = temp

    return df

# step 4 : Visulization Charts
#----------------------------------------------------
# Funcation Name : Chart
# Description    : Visulization Charts Bar,line plots
# Input          : Data frame
# output         : Bar Chart, Line Plot
# Author         : Omkar Ramchandra Kolte
# Date           : 21/08/2026
#-----------------------------------------------------

def Chart(df):
    # ----------------------------------------------------
    # 1. Bar Chart: Student Names vs Total Marks
    # ----------------------------------------------------
    Names = df['Name']
    Total = df['Total']

    plt.bar(
          Names,
          Total,
          width=0.6,
          edgecolor = 'black',
          linewidth = 1,
          alpha = 0.8,
          label = "Student Names vs Total Marks",
     ),

    plt.title("Student Names vs Total Marks")
    plt.xlabel("Student Names")
    plt.ylabel("Total Marks")

    plt.legend()
    plt.show()

    # ----------------------------------------------------
    # 2. Line Plot: Amit's Marks (Optimized using native Pandas filtering)
    # ----------------------------------------------------
    marks = []
    subj = ['Math','Science','English']

    for i in range(len(df)):

        if df['Name'][i] == 'Amit':
            marks.append(df['Math'][i])
            marks.append(   df['Science'][i])
            marks.append(df['English'][i])


    plt.plot(
        subj,
        marks,
        marker = 'o',
        linestyle = '--',
        markersize = 7,
        linewidth = 2,
        label = "Amit's Marks"
    )

    plt.title("Amits Marks")
    plt.xlabel("Subject")
    plt.ylabel("Marks")

    plt.grid(True)
    plt.legend()
    plt.show()

    # ----------------------------------------------------
    # 3. Pie Chart: Sager's Marks (Optimized)
    # ----------------------------------------------------
    marks = []
    subj = ['Math','Science','English']

    for i in range(len(df)):

        if df['Name'][i] == 'Sager':
            marks.append(df['Math'][i])
            marks.append(   df['Science'][i])
            marks.append(df['English'][i])

    plt.pie(
    marks,
    labels=subj,
    autopct='%1.1f%%',              # --> This displays the percentage inside each slice.
    startangle=90                   # --> means the first slice starts at 90 degrees, which is the top of the circle.
    )
                                        # %1.1f  → number with 1 digit after decimal
                                         # %%     → display the % symbol

    plt.title("Sager's Marks")
    plt.show()

    # ----------------------------------------------------
    # 4. Box Plot: English Marks Distribution
    # ----------------------------------------------------
    
    plt.boxplot(df['English'])
    plt.title("Box Plot of English Marks")
    plt.ylabel("Marks")
    plt.grid(True)
    plt.show()
    

# step 5 : Filling Missing values & Droping Tables
#----------------------------------------------------
# Funcation Name : EDA
# Description    :  Filling Missing values & Droping Tables
# Input          : Data frame 2
# output         : Data frame 2 (EDA)
# Author         : Omkar Ramchandra Kolte
# Date           : 21/08/2026
#-----------------------------------------------------
def EDA(df2):
    print(Boreder)
    print(df2.isnull())
    df2['Math'] = df2['Math'].fillna(df2['Math'].mean())

    print(Boreder)
    print(df2)

    print("Deleting English Column ...")
    df2 = df2.drop(columns = ['English'], errors = "ignore")

    print(df2)

# step 6 : Min Max Scale using pandas & MinMaxScaler Sklearn.preprocessing
#----------------------------------------------------
# Funcation Name : Min_Max
# Description    :  Min Max Scale using pandas & MinMaxScaler Sklearn.preprocessing
# Input          : Data frame 
# output         : Normailze Data Frame
# Author         : Omkar Ramchandra Kolte
# Date           : 21/08/2026
#-----------------------------------------------------

def Min_Max(df):

    # Min = df['Math'].min()
    # Max = df['Math'].max()

    # df['Math_Normalization'] = (df['Math']-Min)/(Max-Min)

    # print(df)

    #with MinMaxScaler in sklearn.preprocessing

    scaler = MinMaxScaler()

    df['Math_Normalization'] = scaler.fit_transform(df[['Math']])

    return(df)
# step 8 : Avreage using Group by
#----------------------------------------------------
# Funcation Name : Avg
# Description    : Avreage using Group by gender on Marks
# Input          : Data frame 
# output         : Data frame + Avg
# Author         : Omkar Ramchandra Kolte
# Date           : 21/08/2026
#-----------------------------------------------------

def Avg(df):

    df['Gender'] = ['Male', 'Male', 'Female']
    print(Boreder)

    Ret = df.groupby('Gender')[['Math','Science','English']].mean()
    print(Boreder)
    print("Avreage Base on Gender")
    print(Ret)
    print(Boreder)

    return df
   

# step 7 : Creating/ Adding new Column & performing hot encoding
#----------------------------------------------------
# Funcation Name : Encoding
# Description    : Creating/ Adding new Column name Gender & performing hot encoding 
# Input          : Data frame 
# output         : Data frame 
# Author         : Omkar Ramchandra Kolte
# Date           : 21/08/2026
#-----------------------------------------------------

def Encoding(df):
    # df['Gender'] = ['Male','Male','Female']
    # print(df)
    print(Boreder)
    print("Encoding....")
    print(Boreder)
    # df = pd.get_dummies(df,columns=['Gender'],dtype=int) --> for 0,1 we can use dtype
    df = pd.get_dummies(df,columns=['Gender'])
    print(df)
    return df

# step 9 : Creating/ Adding new Column & Check where pass/fail
#----------------------------------------------------
# Funcation Name : PassFail
# Description    : Creating/ Adding new Column & Check where pass/fail
# Input          : Data frame 
# output         : Data frame 
# Author         : Omkar Ramchandra Kolte
# Date           : 24/08/2026
#-----------------------------------------------------

def PassFail(df):
    df['Status'] = df['Total'].apply(lambda x: 'Pass' if x>250 else 'Fail')
    print(Boreder)
    print(df[['Name','Total','Status']])
    print("Total Passed :", df[df['Status']=='Pass'].shape[0]) # -> count how many std pass
    print(Boreder)
    return df

# step 10 : Export Final Dataframe
#----------------------------------------------------
# Funcation Name : FinalDataFrame
# Description    : Export Final Dataframe
# Input          : Data frame 
# output         : None
# Author         : Omkar Ramchandra Kolte
# Date           : 24/08/2026
#-----------------------------------------------------

def FinalDataFrame(df):

    df.rename(columns = {'Math': 'Mathematics'},inplace = True) # -> renameing columns 
    df.to_csv("Students_result.csv",index = False) # -> Create(New) or Export dataframe into csv

#----------------------------------------------------
# Funcation Name :  main
# Description    :  Entry point function
# Input          :  none
# output         :  Data frame
# Author         :  Omkar Ramchandra Kolte
# Date           :  21/08/2026
#-----------------------------------------------------

def main():

    df, df2 = StudentMarks()

    greterScience = ChkGrater(df)

    print(greterScience)

    Sortdf = SortData(df)
    print(Sortdf)

    Chart(df)
    print(Boreder)

    EDA(df2)
    print(Boreder)

    df = Min_Max(df)
    print(df)
    print(Boreder)

    df =  Avg(df)

    df = Encoding(df)
    print(Boreder)

    df = PassFail(df)
    print(Boreder)

    df = FinalDataFrame(df)



if __name__ == "__main__":
    main()