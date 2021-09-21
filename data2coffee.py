import csv
import pandas as pd
import plotly.express as px

with open('data2coffee.csv', encoding = 'utf-8') as f:
   df = csv.DictReader(f)
   fig = px.scatter(df, x = "Coffee in ml", y = "sleep in hours")
   fig.show()