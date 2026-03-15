import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
class TrafficAccident:
    def __init__(self,file):
        self.dp=pd.read_csv(file)
    def details(self):
        print("==========DATA==========")
        print(self.dp)
        count=self.dp['City'].count()
        print("\nNo of Accident occur in India:",count)
        print("\nAccident Cities:",self.dp['City'])
        M_injured=self.dp['Injuries'].idxmax()
        L_injured=self.dp['Injuries'].idxmin()
        print("\nMost Injured City:",self.dp.loc[M_injured])
        print("\nLeast Injured City:",self.dp.loc[L_injured])
        M_Deaths=self.dp['Deaths'].idxmax()
        L_Deaths=self.dp['Deaths'].idxmin()
        print("\nMost Deaths City:",self.dp.loc[M_Deaths])
        print("\nLeast Deaths City:",self.dp.loc[L_Deaths])
        print("\nDuring Accident Weather Condition:",self.dp[['City','Weather']])
        print("\nAverage Deaths:",np.mean(self.dp['Deaths']))
    
    def plot(self):
        plt.figure(figsize=(18,8),facecolor='tomato')

        plt.subplot(2,2,1)
        sns.barplot(x=self.dp['City'],y=self.dp['Injuries'],color='crimson')
        plt.title("Accident Injuries by City")
        plt.xticks(rotation=45)

        plt.subplot(2,2,2)
        sns.barplot(x=self.dp['City'],y=self.dp['Deaths'],color='black')
        plt.title("Accident Deaths")
        plt.xticks(rotation=45)

        plt.subplot(2,2,3)
        sns.lineplot(x=self.dp['City'],y=self.dp['Injuries'],color='crimson',label='Injured')
        sns.lineplot(x=self.dp['City'],y=self.dp['Deaths'],color='black',label='Deaths')
        plt.title("No of Accidents and Deaths")
        plt.xticks(rotation=45)

        plt.subplot(2,2,4)
        plt.pie(
            self.dp['VehiclesInvolved'],
            labels=self.dp['City'],
            autopct='%1.1f%%',
            colors=['darkred','firebrick','indianred','lightcoral','salmon','tomato'],
            startangle=90
        )
        plt.title("Vehicles Involved in Accidents")
        plt.legend(title="City",loc="right",bbox_to_anchor=(2, 0.5))

        plt.suptitle("TRAFFIC ACCIDENT ANALYSIS DASHBOARD",fontsize=16,color='black',fontweight='bold')
        
        plt.tight_layout()
        plt.show()
TA=TrafficAccident('Traffic_data.csv')
TA.details()
TA.plot()