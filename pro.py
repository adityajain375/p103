import csv
import pandas as pd
import plotly.express as px

data = pd.read_csv('data.csv')

dates = data['date'].tolist()
cases = data['cases'].tolist()
countries = data['country'].tolist()

fig = px.scatter(x = dates, y = cases, color= countries)
fig.show()