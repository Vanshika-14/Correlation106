import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path, encoding = 'utf-8') as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Size of TV", y="Average time spent watching TV in a week (hours)")
        fig.show()

def getDataSource(data_path):
    size_of_tv = []
    time_spent = []
    with open(data_path, encoding = 'utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            size_of_tv.append(float(row["Size of TV"]))
            time_spent.append(float(row["Average time spent watching TV in a week (hours)"]))

    return {"x" : size_of_tv, "y": time_spent}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between TV size vs Watch hours :-  \n--->",correlation[0,1])

def setup():
    data_path  = "tv.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()