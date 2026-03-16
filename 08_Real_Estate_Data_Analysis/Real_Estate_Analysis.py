import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
class RealEstate:
    def __init__(self,file):
        self.dp=pd.read_csv(file)
    def details(self):
        print("===========DATA==========")
        print(self.dp)
        idx=self.dp['HouseID'].count()
        print("\nHouses for Sales:",idx)
        print("\nHouses City:",self.dp['City'])
        print("\nArea squareft:",self.dp[['City','Area_sqft']])
        hsq=self.dp['Area_sqft'].idxmax()
        lsq=self.dp['Area_sqft'].idxmin()
        print("\nHigh Squareft City:",self.dp.loc[hsq])
        print("\nlow Squareft City:",self.dp.loc[lsq])
        print("\nNo of Bedrooms:",self.dp[['City','Bedrooms']])
        print("\nHouses Price:",self.dp[['City','Price']])
        mp=self.dp['Price'].idxmax()
        lp=self.dp['Price'].idxmin()
        print("\nHigh Price House:",self.dp.loc[mp])
        print("\nLow Price House:",self.dp.loc[lp])
        print("\nAverage Price:",np.mean(self.dp['Price']))
    def plot(self):
        plt.figure(figsize=(18,8),facecolor='seashell')

        plt.subplot(2,2,1)
        sns.barplot(x=self.dp['City'],y=self.dp['Price'],color='darkgreen')
        plt.title("House Prices")
        plt.xticks(rotation=45)

        plt.subplot(2,2,2)
        sns.barplot(x=self.dp['City'],y=self.dp['Area_sqft'],color='royalblue')
        plt.title("House Area_sqft")
        plt.xticks(rotation=45)

        plt.subplot(2,2,3)
        sns.barplot(x=self.dp['City'],y=self.dp['Bedrooms'],color='goldenrod')
        plt.title("No of Bedrooms")
        plt.xticks(rotation=45)
        
        plt.subplot(2,2,4)
        plt.pie(
            self.dp['Price'],
            labels=self.dp['City'],
            autopct='%1.1f%%',
            colors = ['darkgreen','forestgreen','limegreen','gold','tan','peru'],
            startangle=90
        )
        plt.title("Price Percentage")
        plt.legend(title="city",loc="right",bbox_to_anchor=(2,0.5))
        plt.suptitle("REALESTATE ANALYSIS DASHBOARD",fontsize=16,color='black',fontweight='bold')

        plt.tight_layout()
        plt.show()

RE=RealEstate('Real_estate_data.csv')
RE.details()
RE.plot()