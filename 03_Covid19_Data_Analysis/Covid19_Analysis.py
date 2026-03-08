import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
class Covid19:
    def __init__(self,file):
        self.dp=pd.read_csv(file)
        self.dp['Date']=pd.to_datetime(self.dp['Date'])
    def details(self):
        print("======DATA======")
        print(self.dp)
        affected=self.dp.groupby('Country')['Confirmed'].sum()
        print("\nAffected Country:",affected)
        print("\n No of countries:",affected.count())
        print("\nMost affected Country:",affected.idxmax())
        print("\nLeast affected Country:",affected.idxmin())
        recovered=self.dp.groupby('Country')['Recovered'].sum()
        print("\nRecovered people:",recovered)
        print("\nMost recovered Country:",recovered.idxmax())
        print("\nLeast recovered Country:",recovered.idxmin())
        deaths=self.dp.groupby('Country')['Deaths'].sum()
        print("\npeoples deaths:",deaths)
        print("\nMost deaths Country:",deaths.idxmax())
        print("\nLeast deaths Country:",deaths.idxmin())
    def plot(self):
        plt.figure(figsize=(18,8),facecolor="lightgrey")
        country_data = self.dp.groupby('Country')[['Confirmed','Recovered','Deaths']].sum()

        plt.subplot(2,3,1)
        sns.lineplot(x=country_data.index,y=country_data['Confirmed'],color='r')
        plt.title("Corana Affected Peoples")
        plt.xticks(rotation=45)

        plt.subplot(2,3,2)
        deaths=country_data['Deaths']
        sns.barplot(x=deaths.index,y=deaths.values,color='black')
        plt.title("Countries Peoples Deaths")
        plt.xticks(rotation=45)

        plt.subplot(2,3,3)
        recovered=country_data['Recovered']
        sns.barplot(x=recovered.index,y=recovered.values,color='green')
        plt.title("Countries Peoples Recovered")
        plt.xticks(rotation=45)

        plt.subplot(2,3,4)
        affected=country_data['Confirmed']
        recovered=country_data['Recovered']
        deaths=country_data['Deaths']
        sns.scatterplot(x=affected.index,y=affected.values,color='r',label='Confirmed')
        sns.scatterplot(x=recovered.index,y=recovered.values,color='green',label='Recovered')
        sns.scatterplot(x=deaths.index,y=deaths.values,color='black',label='Deaths')
        plt.title("Corona Situation")
        plt.xticks(rotation=45)
        plt.legend(title="category")

        plt.subplot(2,3,5)
        sns.histplot(x=self.dp['Confirmed'],kde=True,bins=10,color='orange')
        plt.title("Overall Corana Affected")
        plt.xticks(rotation=45)

        plt.subplot(2,3,6)
        confirm=country_data['Confirmed']
        plt.pie(
            confirm.values,
            labels=confirm.index,
            autopct='%1.1f%%',
            startangle=90
        )
        plt.title("Countries Affected")
        plt.legend(title="Countries",loc="right",bbox_to_anchor=(2, 0.5))

        plt.suptitle("COVID19 ANALYSIS",fontsize=16,color='black',fontweight='bold')
        plt.tight_layout()
        sns.set_style("whitegrid")
        sns.despine()
        plt.show()

C19=Covid19('Covid_data.csv')
C19.details()
C19.plot()
    
