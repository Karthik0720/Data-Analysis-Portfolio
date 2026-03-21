import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

class StockMarket:
    def __init__(self,file):
        self.dp = pd.read_csv(file)

        self.dp['Date'] = pd.to_datetime(self.dp['Date'])
        self.dp['TradingValue'] = self.dp['Close'] * self.dp['Volume']
        self.dp['Volatility'] = self.dp['High'] - self.dp['Low']
        self.dp['DailyReturn'] = self.dp['Close'] - self.dp['Open']

    def details(self):
        print("==========DATA==========")
        print(self.dp)

        No_stock = self.dp['Stock'].nunique()
        stock = self.dp['Stock'].unique()

        print("\nNo of stocks:", No_stock)
        print("\nStock Names:", stock)

        high_value_stock = self.dp.groupby('Stock')['High'].mean()
        print("\nHighest Avg Price Stock:", high_value_stock.idxmax(), high_value_stock.max())

        low_value_stock = self.dp.groupby('Stock')['High'].mean()
        print("\nLowest Avg Price Stock:", low_value_stock.idxmin(), low_value_stock.min())

        trading_value = self.dp.groupby('Stock')['TradingValue'].sum()
        print("\nTrading Value by Stock:\n", trading_value)

        print("\nHighest Trading Value Stock:", trading_value.idxmax())
        print("Lowest Trading Value Stock:", trading_value.idxmin())

        volatility = self.dp.groupby('Stock')['Volatility'].mean()
        print("\nStock Volatility:\n", volatility)

        daily_return = self.dp.groupby('Stock')['DailyReturn'].mean()
        print("\nAverage Daily Return:\n", daily_return)

        print("\nHighest Profit Stock:", daily_return.idxmax())
        print("Lowest Profit Stock:", daily_return.idxmin())

        print("\nOverall Average Return:", np.mean(daily_return))

    def plot(self):
        sns.set_style("whitegrid")
        plt.figure(figsize=(18,8), facecolor='black')

        plt.subplot(2,3,1)
        idx = self.dp.groupby('Stock')['High'].mean()
        sns.lineplot(x=idx.index, y=idx.values, marker='o', color='white')
        plt.gca().set_facecolor('black')
        plt.title("Average Stock High Price", color='white')
        plt.tick_params(colors='white')

        plt.subplot(2,3,2)
        idx = self.dp.groupby('Stock')['Volume'].sum()
        sns.lineplot(x=idx.index, y=idx.values, marker='o', color='lightgray')
        plt.gca().set_facecolor('black')
        plt.title("Total Stock Volume", color='white')
        plt.tick_params(colors='white')

        plt.subplot(2,3,3)
        idx = self.dp.groupby('Stock')['Volatility'].mean()
        sns.barplot(x=idx.index, y=idx.values, color='gray')
        plt.gca().set_facecolor('black')
        plt.title("Stock Volatility", color='white')
        plt.tick_params(colors='white')

        plt.subplot(2,3,4)
        idx = self.dp.groupby('Stock')['DailyReturn'].mean()
        sns.barplot(x=idx.index, y=idx.values, color='silver')
        plt.gca().set_facecolor('black')
        plt.title("Average Daily Return", color='white')
        plt.tick_params(colors='white')

        plt.subplot(2,3,5)
        idx = self.dp.groupby('Stock')['TradingValue'].sum()
        sns.barplot(x=idx.index, y=idx.values, color='white')
        plt.gca().set_facecolor('black')
        plt.title("Total Trading Value", color='white')
        plt.tick_params(colors='white')

        plt.subplot(2,3,6)
        idx = self.dp.groupby('Stock')['DailyReturn'].mean()

        colors = ['gray','lightgray','gray','silver','dimgray']

        plt.pie(
            idx.values,
            labels=idx.index,
            autopct='%1.1f%%',
            startangle=90,
            colors=colors,
            textprops={'color':'white'}
        )
        plt.title("Return Percentage", color='white')

        plt.legend(title="Company", loc="right", bbox_to_anchor=(2, 0.5))

        plt.suptitle(
            "STOCK MARKET ANALYSIS DASHBOARD",
            fontsize=16,
            fontweight='bold',
            color='white'
        )

        plt.tight_layout()
        plt.show()


SM = StockMarket('Stock_Market_data.csv')
SM.details()
SM.plot()

        