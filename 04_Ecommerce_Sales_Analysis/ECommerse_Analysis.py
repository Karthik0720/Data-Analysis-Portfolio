import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
class EcommerseAnalysis:
    def __init__(self,file):
        self.dp=pd.read_csv(file)
        self.dp['Totalspend']=self.dp['Quantity']*self.dp['Price']
    def details(self):
        print("======DATA======")
        print(self.dp)
        highcost=self.dp['Price'].idxmax()
        print("\nHighcost Product:",self.dp.loc[highcost])
        mostexpensive=self.dp.groupby('Category')['Price'].sum()
        print("\nMost Expensive Category:",mostexpensive.idxmax())
        mostordered=self.dp['CustomerName'].value_counts()
        print("\nMost ordered Customer:",mostordered.idxmax())
        mostselling=self.dp['Totalspend'].idxmax()
        print("\nMost Selling Product:",self.dp.loc[mostselling])
        print("\nAverage Price:",np.mean(self.dp['Price']))
    def plot(self):
        plt.figure(figsize=(18,8),facecolor='whitesmoke')

        plt.subplot(2,2,1)
        sns.lineplot(x=self.dp['Product'],y=self.dp['Quantity'],color='black', marker='o')
        plt.title("Product Quantity")
        plt.xticks(rotation=45)

        plt.subplot(2,2,2)
        sns.barplot(x=self.dp['Product'],y=self.dp['Price'],color='black')
        plt.title("Product Price")
        plt.xticks(rotation=45)

        plt.subplot(2,2,3)
        sns.barplot(x=self.dp['Product'],y=self.dp['Totalspend'],color='black')
        plt.title("Total Product Spend")
        plt.xticks(rotation=45)

        plt.subplot(2,2,4)
        plt.pie(
            self.dp['Totalspend'],
            labels=self.dp['Product'],
            autopct='%1.1f%%',
            startangle=90,
            colors=['#4f4f4f','#6f6f6f','#8f8f8f','#afafaf','#cfcfcf','#efefef']
        )
        plt.title("Products Sales")
        plt.legend(title="Products",loc="right",bbox_to_anchor=(2, 0.5))

        plt.suptitle("ECOMMERSE ANALYSIS DASHBOARD",fontsize=16,color='black',fontweight='bold')
        plt.tight_layout()
        sns.set_style("whitegrid")
        plt.show()


EC=EcommerseAnalysis('ECommerse_data.csv')
EC.details()
EC.plot()

