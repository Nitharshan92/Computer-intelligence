# -*- coding: utf-8 -*-
"""Loan Approval.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CObp0n5HlIn_VBxjosuf_iOmx2wK10sA
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

#from google.colab import drive
#drive.mount('/content/drive', force_remount=True)

#df = pd.read_csv("/content/drive/MyDrive/Dataset/Training Dataset.csv")
df = pd.read_csv('Training Dataset.csv')
df

df.head()

df.shape

df.info()

df.describe()

df.isnull().sum()

df.LoanAmount=df.LoanAmount.fillna(df.LoanAmount.mean())
df.Credit_History=df.Credit_History.fillna(df.Credit_History.mean())
df.Loan_Amount_Term=df.Loan_Amount_Term.fillna(df.Loan_Amount_Term.mean())
df['Gender'].fillna(df['Gender'].value_counts().idxmax(), inplace=True)
df['Married'].fillna(df['Married'].value_counts().idxmax(), inplace=True)
df.Dependents.fillna(df.Dependents.value_counts().idxmax(), inplace=True)
df.Self_Employed.fillna(df.Self_Employed.value_counts().idxmax(), inplace=True)

df.isnull().sum()

df.duplicated().sum()

df.drop(['Loan_ID'], axis=1)

df.skew()

df.ApplicantIncome=df.ApplicantIncome.clip(lower=df.ApplicantIncome.quantile(0.05),upper=df.ApplicantIncome.quantile(0.95))
df.CoapplicantIncome=df.CoapplicantIncome.clip(lower=df.CoapplicantIncome.quantile(0.05),upper=df.CoapplicantIncome.quantile(0.95))
df.Loan_Amount_Term=df.Loan_Amount_Term.clip(lower=df.Loan_Amount_Term.quantile(0.14),upper=df.Loan_Amount_Term.quantile(0.86))
df.LoanAmount=df.LoanAmount.clip(lower=df.LoanAmount.quantile(0.05),upper=df.LoanAmount.quantile(0.95))
df.Credit_History=df.Credit_History.clip(lower=df.Credit_History.quantile(0.05),upper=df.Credit_History.quantile(0.95))
df.ApplicantIncome=df.ApplicantIncome.clip(lower=df.ApplicantIncome.quantile(0.10),upper=df.ApplicantIncome.quantile(0.90))

df.skew()

fig = plt.figure(figsize=(2,4))
fig.canvas.set_window_title('Count of Gender')
sb.countplot(df.Gender)
#plt.title("Tests")
plt.show()

fig = plt.figure(figsize=(2,4))
fig.canvas.set_window_title('Count of Marital status')
sb.countplot(df.Married)
plt.show()

fig = plt.figure(figsize=(2,4))
fig.canvas.set_window_title('Count of number of Dependents')
sb.countplot(df.Dependents)
plt.show()

fig = plt.figure(figsize=(3,6))
fig.canvas.set_window_title('Count of Education status')
sb.countplot(df.Education)
plt.show()

fig = plt.figure(figsize=(2,4))
fig.canvas.set_window_title('Count of Employment type')
sb.countplot(df.Self_Employed)
plt.show()

fig = plt.figure(figsize=(4,8))
fig.canvas.set_window_title('Count of Area type')
sb.countplot(df.Property_Area)
plt.show()

fig = plt.figure(figsize=(5,10))
fig.canvas.set_window_title('Count of Credit history')
sb.countplot(df.Credit_History)
plt.show()

num=['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term']
for column in num:
    plt.figure(figsize=(8,4))
    plt.hist(df[column])
    plt.title(column)
    plt.show()

df.Loan_Status.replace('N',0,inplace=True)
df.Loan_Status.replace('Y',1,inplace=True)

df.head()

fig = plt.figure(figsize=(12,5))
fig.canvas.set_window_title('Graph of Applicant income vs Loan status')
sb.distplot(df['ApplicantIncome'][df.Loan_Status==0])
sb.distplot(df['ApplicantIncome'][df.Loan_Status==1])
plt.legend(['Loan_Status=0','Loan_Status=1'])
plt.show()

fig = plt.figure(figsize=(12,5))
fig.canvas.set_window_title('Graph of Loan amount vs Loan status')
sb.distplot(df['LoanAmount'][df.Loan_Status==0])
sb.distplot(df['LoanAmount'][df.Loan_Status==1])
plt.legend(['Loan_Status=0','Loan_Status=1'])
plt.show()

pivot = pd.crosstab(df.Married,df.Loan_Status,margins=True)
pivot

pivot['All']

pivot[1]

ratio = pivot[1]/pivot['All']*100
ratio

ratio.plot(kind='bar')

pivot1 = pd.crosstab(df.Gender,df.Loan_Status,margins=True)
pivot1

pivot1['All']

pivot1[1]

ratio1 = pivot1[1]/pivot1['All']*100
ratio1

ratio1.plot(kind='bar')

pivot2 = pd.crosstab(df.Dependents,df.Loan_Status,margins=True)
pivot2

pivot2['All']

pivot2[1]

ratio2 = pivot2[1]/pivot2['All']*100
ratio2

ratio2.plot(kind='bar')

pivot3 = pd.crosstab(df.Education,df.Loan_Status,margins=True)
pivot3

pivot3['All']

pivot3[1]

ratio3 = pivot3[1]/pivot3['All']*100
ratio3

ratio3.plot(kind='bar')

pivot4 = pd.crosstab(df.Self_Employed,df.Loan_Status,margins=True)
pivot4

pivot4['All']

pivot4[1]

ratio4 = pivot4[1]/pivot4['All']*100
ratio4

ratio4.plot(kind='bar')

pivot5= pd.crosstab(df.Credit_History,df.Loan_Status,margins=True)
pivot5

pivot5['All']

pivot5[1]

ratio5 = pivot5[1]/pivot5['All']*100
ratio5

ratio5.plot(kind='bar')

pivot6= pd.crosstab(df.Property_Area,df.Loan_Status,margins=True)
pivot6

pivot6['All']

pivot6[1]

ratio6 = pivot6[1]/pivot6['All']*100
ratio6

ratio6.plot(kind='bar')

df

from sklearn.preprocessing import LabelEncoder
df['Education']=LabelEncoder().fit_transform(df['Education'])
df['Dependents']=LabelEncoder().fit_transform(df['Dependents'])
df['Self_Employed']=LabelEncoder().fit_transform(df['Self_Employed'])
df['Gender']=LabelEncoder().fit_transform(df['Gender'])
df['Married']=LabelEncoder().fit_transform(df['Married'])
df['Property_Area']=LabelEncoder().fit_transform(df['Property_Area'])

df

cor=df.corr()
fig = plt.figure(figsize=(20,12))
fig.canvas.set_window_title('My title')
sb.heatmap(cor,annot=True,cmap='seismic')
plt.show()

from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error as mae,median_absolute_error as mee,classification_report as cr,accuracy_score as ac

df2=df
df2.head(10)

col=['Loan_ID','Gender','Self_Employed','CoapplicantIncome','Loan_Amount_Term']
df2=df2.drop(columns=col,axis=1)
df2

x=df2[['Married','Dependents','Education','ApplicantIncome','LoanAmount','Credit_History','Property_Area']]
y=df2[['Loan_Status']]

x

y

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=123456)

from sklearn.tree import DecisionTreeClassifier 
model=DecisionTreeClassifier()

model.fit(x_train,y_train)

y_pre1 = model.predict(x_test)
y_pre1

from sklearn.model_selection import cross_val_score
print(ac(y_test,y_pre1)*100)
sco1=(cross_val_score(model,x,y,cv=5))
print(np.mean(sco1)*100)

from  sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pre1)
fig = plt.figure(figsize=(8,6))
fig.canvas.set_window_title('Output Confusion Matrix')
fg=sb.heatmap(cm,annot=True,cmap="Reds")
figure=fg.get_figure()
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title("Output Confusion Matrix")
plt.show()

#newinput=[[1,1,0,4583.0,128.000000,1.0,0]]
#output1=model.predict(newinput)
#output1

import os


def clear_console():
    os.system('cls')


clear_console()

import time

marital_status = input("Are you married? (Yes/No) - ")
marital_status = marital_status.lower()
if marital_status == "yes" or marital_status == "no":

  marital_status = marital_status.replace('no','0')
  marital_status = marital_status.replace('yes','1')
  marital_status = int(marital_status)

  dependents_details = input("How many dependents you have? (Only numbers allowed to input) - ")
  if dependents_details.isnumeric():

    dependents_details = int(dependents_details)

    graduation_level = input("Are you gratuated? (Yes/No) - ")
    graduation_level = graduation_level.lower()
    if graduation_level == "yes" or graduation_level == "no":

      graduation_level = graduation_level.replace('no','0')
      graduation_level = graduation_level.replace('yes','1')
      graduation_level = int(graduation_level)

      monthly_income = input("How much is your monthly salary? (Only numbers allowed to input) - ")  
      if monthly_income.isnumeric():

        monthly_income = float(monthly_income)/10

        loan_amount = input("How much do you applied for a loan? (Only numbers allowed to input) - ")
        if loan_amount.isnumeric():

          loan_amount = int(loan_amount)/1000

          credit_history = input("Did you finish your previous loan? (Yes/No) - ")
          credit_history = credit_history.lower()
          if credit_history == "yes" or credit_history == "no":
            
            credit_history = credit_history.replace('no','0')
            credit_history = credit_history.replace('yes','1')
            credit_history = float(credit_history)

            prop_area = input("Where is your property located? (Rural: Press R, Semi-urben: Press S, Urber: Press U) - ")
            prop_area = prop_area.lower()
            if prop_area == "r" or prop_area == "s" or prop_area == "u":

              prop_area = prop_area.replace('r','0')
              prop_area = prop_area.replace('s','1')
              prop_area = prop_area.replace('u','2')
              prop_area = int(prop_area)

              newinput=[[marital_status,dependents_details,graduation_level,monthly_income,loan_amount,credit_history,prop_area]]
              output1=model.predict(newinput)

              if output1[0] == 0:
                print("Sorry, as my prediction you will not get loan approval, programme will close in 10 seconds.")
                time.sleep(10)
              elif output1[0] == 1:
                print("You have high change of getting loan approval, programme will close in 10 seconds.")
                time.sleep(10)
              else:
                print("Invalid argument, programme will close in 10 seconds.")
                time.sleep(10)

            else:
              print("invalid input")
              time.sleep(10)
          else:
            print("invalid input")
            time.sleep(10)
        else:
          print("invalid input")
          time.sleep(10)
      else:
        print("invalid input")
        time.sleep(10)
    else:
      print("invalid input")
      time.sleep(10)
  else:
    print("invalid input")
    time.sleep(10)
else:
  print("invalid input")
  time.sleep(10)