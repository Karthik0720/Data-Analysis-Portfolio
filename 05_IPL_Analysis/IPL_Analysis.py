import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
class IPLAnalysis:
    def __init__(self,file):
        self.dp=pd.read_csv(file)
    def details(self):
        print("========DATA========")
        print(self.dp)
        total_teams = self.dp['Team'].nunique()
        team_names = self.dp['Team'].unique()
        print("\nTotal Teams:", total_teams)
        print("Team Names:", team_names)
        idx=self.dp.groupby('Team')['Opponent'].count()
        print("\nNo of Matches a Team Played:",idx)
        idx=self.dp.groupby('Team')['Runs'].sum()
        print("\nHighest Runs:",idx.idxmax())
        print("\nLowest Runs:",idx.idxmin())
        idx=self.dp.groupby('Team')['Wickets'].sum()
        print("\nMost Wicket Taken:",idx.idxmax())
        print("\nLeast Wicket Taken:",idx.idxmin())
        idx=self.dp[self.dp['Result']=='Win']['Team'].unique()
        print("\nWinning Teams:",idx)
        idx=self.dp[self.dp['Result']=='Lose']['Team'].unique()
        print("\nLosing Teams:",idx)
    def plot(self):
        plt.figure(figsize=(18,8),facecolor='mintcream')
        
        plt.subplot(2,2,1)
        idx=self.dp.groupby('Team')['Opponent'].count()
        sns.barplot(x=idx.index,y=idx.values,color='skyblue')
        plt.title("Matches Played by Each Team")
        plt.xlabel("Team")
        plt.ylabel("Matches")
        plt.xticks(rotation=45)

        plt.subplot(2,2,2)
        idx=self.dp.groupby('Team')['Runs'].sum()
        sns.barplot(x=idx.index,y=idx.values,color='lightgreen')
        plt.title("Total Runs by Team")
        plt.xlabel("Team")
        plt.ylabel("Runs")
        plt.xticks(rotation=45)

        plt.subplot(2,2,3)
        idx=self.dp.groupby('Team')['Wickets'].sum()
        sns.barplot(x=idx.index,y=idx.values,color='orange')
        plt.title("Total Wickets Taken by Team")
        plt.xlabel("Team")
        plt.ylabel("Wickets")
        plt.xticks(rotation=45)

        plt.subplot(2,2,4)
        result=self.dp.groupby(['Team','Result']).size().reset_index(name='Count')
        sns.barplot(x='Team',y='Count',hue='Result',data=result,palette={'Win':'green','Lose':'red'})
        plt.title("Team Win vs Lose Comparison")
        plt.xlabel("Team")
        plt.ylabel("Matches")
        plt.xticks(rotation=45)

        plt.suptitle("IPL TEAM PERFORMANCE ANALYSIS",fontsize=16,fontweight='bold')

        plt.tight_layout()
        plt.show()
        



IPL=IPLAnalysis('IPL_data.csv')
IPL.details()
IPL.plot()