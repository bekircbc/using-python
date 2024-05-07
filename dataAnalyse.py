import pandas from pd

data = pd.read_csv('dat.csv')

grouped_data = data.groupby('category')['value'].sum()
print(grouped_data)
