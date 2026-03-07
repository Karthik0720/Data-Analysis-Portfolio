import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
class SalesAnalysis:
    def __init__(self,file):
        self.dp=pd.read_csv(file)
        self.dp['Totalcost']=self.dp['Quantity']*self.dp['CostPrice']
        self.dp['Totalrevenue']=self.dp['Quantity']*self.dp['SellingPrice']
        self.dp['Date']=pd.to_datetime(self.dp['Date'])
    def details(self):
        print("======DATA======")
        print(self.dp)
        print("\nTotalcost:",self.dp['Totalcost'].sum())
        print("\nTotalrevenue:",self.dp['Totalrevenue'].sum())
        print("\nTotalProfit:",self.dp['Totalrevenue'].sum()-self.dp['Totalcost'].sum())
        idx=self.dp['Totalrevenue'].idxmax()
        print("\nTopselling Product:",self.dp.loc[idx])
        idx=self.dp.groupby('Category')['SellingPrice'].sum()
        print("\nTopSelling Category:",idx.idxmax())
        print("Average Price",np.mean(self.dp['Totalcost']))
    def plot(self):
        plt.figure(figsize=(18,8),facecolor="whitesmoke")

        plt.subplot(2,3,1)
        sns.lineplot(x=self.dp['Product'],y=self.dp['Totalcost'],color='darkorange')
        plt.title("Product Cost")
        plt.xticks(rotation=45)

        plt.subplot(2,3,2)
        sns.barplot(x=self.dp['Product'],y=self.dp['Totalrevenue'],color='skyblue')
        plt.title("Product Revenue")
        plt.xticks(rotation=45)

        plt.subplot(2,3,3)
        sns.barplot(x=self.dp['Date'],y=self.dp['Totalrevenue'],color='seagreen')
        plt.title("Daily Sales")
        plt.xticks(rotation=45)

        plt.subplot(2,3,4)
        sns.scatterplot(x=self.dp['Product'],y=self.dp['SellingPrice'],color='crimson')
        plt.title("Each Selling Product")
        plt.xticks(rotation=45)

        plt.subplot(2,3,5)
        sns.boxplot(x=self.dp['Category'],y=self.dp['Totalrevenue'],color='mediumpurple')
        plt.title("Category wise selling")

        plt.subplot(2,3,6)
        plt.pie(
            self.dp['Totalrevenue'],
            labels=self.dp['Product'],
            autopct='%1.1f%%',
            colors=['skyblue','seagreen','darkorange','mediumpurple','crimson','gold','lightcoral','turquoise'],
            startangle=90
        )
        plt.title("Products Sales")
        plt.legend(title="Products",loc="right",bbox_to_anchor=(2, 0.5))

        plt.suptitle("Sales Performance",fontsize=16,color='black',fontweight='bold')
        plt.tight_layout()
        sns.despine()
        plt.show()


SA=SalesAnalysis('Sales_data.csv')
SA.details()
SA.plot()
