import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
class NetflixAnalysis:
    def __init__(self,file):
        self.dp=pd.read_csv(file)
    def details(self):
        print("==========DATA==========")
        print(self.dp)
        highest=self.dp['Rating'].idxmax()
        lowest=self.dp['Rating'].idxmin()
        print("\nHighest Movie Rating:",self.dp.loc[highest])
        print("\nLowest Movie Rating:",self.dp.loc[lowest])
        highest=self.dp['Reviews'].idxmax()
        lowest=self.dp['Reviews'].idxmin()
        print("\nHighest Movie Reviews:",self.dp.loc[highest])
        print("\nLowest Movie Reviews:",self.dp.loc[lowest])
        like=self.dp.groupby('Genre')['Rating'].mean()
        print("\nMost Peoples liked Movie Type:",like.idxmax())
        print("\nLeast Peoples liked Movie Type:",like.idxmin())
        print("\nAverage Rating:",np.mean(self.dp['Rating']))
    def plot(self):
        plt.figure(figsize=(18,8),facecolor='r')

        plt.subplot(2,2,1)
        sns.lineplot(x=self.dp['Movie'],y=self.dp['Reviews'],markers='o',color='r')
        plt.title("Movies Reviews")
        plt.xticks(rotation=45)

        plt.subplot(2,2,2)
        sns.barplot(x=self.dp['Movie'],y=self.dp['Rating'],color='crimson')
        plt.title("Movies Ratings")
        plt.xticks(rotation=45)

        plt.subplot(2,2,3)
        like=self.dp.groupby('Genre')['Rating'].mean()
        plt.barh(like.index,like.values,height=0.5,color='darkred')
        plt.title("Peoples liked Movie")
        plt.xlabel("Movies")
        plt.ylabel("Ratings")
        plt.xticks(rotation=45)

        plt.subplot(2,2,4)
        plt.pie(
            self.dp['Rating'],
            labels=self.dp['Movie'],
            autopct='%1.1f%%',
            colors=['red','darkred','firebrick','indianred','lightcoral','salmon','tomato','crimson','maroon'],
            startangle=90
        )
        plt.title('Movies Comparision')
        plt.legend(title="Movies",loc="right",bbox_to_anchor=(2, 0.5))

        plt.suptitle("NETFLIX ANALYSIS DASHBOARD",fontsize=16,color='black',fontweight='bold')
        plt.tight_layout()
        plt.show()

NA=NetflixAnalysis('Netflix_data.csv')
NA.details()
NA.plot()