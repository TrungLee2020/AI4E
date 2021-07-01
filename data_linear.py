import pandas as pd
import matplotlib.pyplot as plt

#load data
data = pd.read_csv('./dataset_entry_test/data_linear.csv').values
# print(data)

#visualize data
x = data[:, 0].reshape(-1, 1)
y = data[:, 1].reshape(-1, 1)

plt.scatter(x, y)
plt.xlabel('Diện tích (m2)')
plt.ylabel('Giá nhà')
plt.show()