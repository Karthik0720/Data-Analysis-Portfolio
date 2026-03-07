import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
class StudentPerformance:
    def __init__(self,file):
        self.dp=pd.read_csv(file)
        self.dp['Total']=self.dp[['Math','Science','English']].sum(axis=1)
        self.dp['Average']=self.dp['Total']/3
    def details(self):
        print("=======DATA=======")
        print(self.dp)
        print("Overall Average",np.mean(self.dp['Average']))
        topper=self.dp['Total'].idxmax()
        print("\nTop Student",self.dp.loc[topper])
    def plot(self):
        plt.figure(figsize=(18,8),facecolor='lavender')

        plt.subplot(2,3,1)
        sns.barplot(x=self.dp['Name'],y=self.dp['Total'],color='skyblue')
        plt.title("Students Score")
        plt.xticks(rotation=45)

        plt.subplot(2,3,2)
        sns.lineplot(x=self.dp['Name'],y=self.dp['StudyHours'],color='darkorange')
        plt.title("Study Hours")
        plt.xticks(rotation=45)

        plt.subplot(2,3,3)
        sns.histplot(x=self.dp['Average'],bins=10,color='seagreen')
        plt.title("Average Score")

        plt.subplot(2,3,4)
        sns.boxplot(x=self.dp['Gender'],y=self.dp['Total'],color='lightcoral')
        plt.title("Gender Performance")

        plt.subplot(2,3,5)
        sns.scatterplot(x=self.dp['Name'],y=self.dp['Total'],color='darkblue')
        plt.title("difference")
        plt.xticks(rotation=45)

        plt.subplot(2,3,6)
        sns.heatmap(self.dp[['Math','Science','English']].corr(),
            annot=True,
            cmap="coolwarm")
        plt.title("Subject Correlation")

        plt.suptitle("Students Performance",fontsize=16,color='black')
        plt.tight_layout()
        plt.show()

        

SP=StudentPerformance('Student_performance.csv')
SP.details()
SP.plot()
        