import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# i inserted this cell
url = 'https://pynative.com/wp-content/uploads/2019/01/company_sales_data.csv'

data = pd.read_csv('./data/company_sales_data.csv')
print(data.head())


data.plot.bar(x='month_number', y=['facecream', 'facewash'], figsize=(10,8))
plt.xlabel('Month Number')
plt.ylabel('Sales units in numbers')
plt.title('Facewash and Facecream Sales Data')
plt.legend(['Facecream Sales', 'Facewash Sales'], loc='upper left')
plt.grid(True, linestyle='--', linewidth=2)

#data.head()