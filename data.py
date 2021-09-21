import csv
import pandas as pd
import plotly.express as px

with open('data.csv', encoding = 'utf-8') as f:
   df = csv.DictReader(f)
   fig = px.scatter(df, x = "Temperature", y = "Ice-cream Sales( ₹ )")
   fig.show()