import numpy as np
import pandas as pd

orders = pd.read_csv('orders.csv')
# print(orders.head(3))

cheap_shoes = orders.groupby('shoe_color').price.apply(lambda x: np.percentile(x,25)).reset_index()
# print(cheap_shoes)

shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()
# print(shoe_counts)

shoe_counts_pivot = shoe_counts.pivot(
  columns = 'shoe_color',
  index = 'shoe_type',
  values = 'id'
).reset_index()

print(shoe_counts_pivot)