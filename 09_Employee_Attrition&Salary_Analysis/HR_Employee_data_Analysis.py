import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
class HREmployee:
    def __init__(self,file):
        self.dp=pd.read_csv(file)
    def details(self):
        print("==========DATA=========")
        print(self.dp)
        print("\nNo of Departments:",self.dp['Department'].unique())
        salary=self.dp.groupby('Department')['Salary'].mean()
        print("\nDepartment Salary:",salary)
        print("\nHighest Salary Department:",salary.idxmax())
        print("\nLowest Salary Department:",salary.idxmin())
        print("\nAverage Salary:",np.mean(self.dp['Salary']))
        print("\nEmployee Experience:",self.dp[['EmployeeID','Experience']])
        HE=self.dp['Experience'].idxmax()
        LE=self.dp['Experience'].idxmin()
        print("\nhigh Experience Employee:",self.dp.loc[HE])
        print("\nLess Experience Employee:",self.dp.loc[LE])
        yes=self.dp[self.dp['Attrition']=='Yes']
        no=self.dp[self.dp['Attrition']=='No']
        print("\nCurrent Working Employee:",yes)
        print("\nNot Working Employee:",no)
    def plot(self):
        plt.figure(figsize=(18,8),facecolor='#f5f7fa')

        plt.subplot(2,2,1)
        sns.barplot(x=self.dp['Department'],y=self.dp['Salary'],color='#4c72b0')
        plt.title("Department Salary")
        plt.xticks(rotation=45)

        plt.subplot(2,2,2)
        sns.barplot(x=self.dp['Department'],y=self.dp['Experience'],color='#55a868')
        plt.title("Employee Salary")
        plt.xticks(rotation=45)

        plt.subplot(2,2,3)
        sns.countplot(x='Attrition', data=self.dp,palette=['#c44e52', '#4c72b0'])
        plt.title("Employee Salary")

        plt.subplot(2,2,4)
        idx=self.dp.groupby('Department')['Salary'].mean()
        plt.pie(
            idx.values,
            labels=idx.index,
            autopct='%1.1f%%',
            colors = ['#4c72b0', '#55a868', '#c44e52', '#8172b2'],
            startangle=90
        )
        plt.legend(title="Department",loc='right',bbox_to_anchor=(2,0.5))
        
        plt.suptitle("HR EMPLOYEE DATA ANALYSIS DASHBOARD",fontsize=16,color='black',fontweight='bold')
        plt.tight_layout()
        plt.show()
HRE=HREmployee('HR_Employee_data.csv')
HRE.details()
HRE.plot()