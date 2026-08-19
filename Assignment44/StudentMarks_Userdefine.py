import pandas as pd
import numpy as np

import matplotlib.pyplot as plt


Boreder = '-'*40
# step 1 : Load Data
#----------------------------------------------------
# Funcation Name : StudentMarks
# Description    : Create Data Set 
# Input          : None
# output         : Data frame
# Author         : Omkar Ramchandra Kolte
# Date           : 19/08/2026
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
# Date           : 19/08/2026
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
# Date           : 19/08/2026
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
# Date           : 19/08/2026
#-----------------------------------------------------

def Chart(df):

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

# step 5 : Filling Missing values & Droping Tables
#----------------------------------------------------
# Funcation Name : EDA
# Description    :  Filling Missing values & Droping Tables
# Input          : Data frame 2
# output         : Data frame 2 (EDA)
# Author         : Omkar Ramchandra Kolte
# Date           : 19/08/2026
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

#----------------------------------------------------
# Funcation Name :  main
# Description    :  Entry point function
# Input          :  none
# output         :  Data frame
# Author         :  Omkar Ramchandra Kolte
# Date           :  18/08/2026
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



if __name__ == "__main__":
    main()