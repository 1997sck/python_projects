import pandas as pd

# reading two csv files
data1 = pd.read_csv('datasetsloan.csv')
data2 = pd.read_csv('datasetsborrower.csv')

# using merge function by setting how='inner'
output1 = pd.merge(data1, data2)

# displaying result
print(output1)