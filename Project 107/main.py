import csv
import plotly.express as px
import numpy as np

def plotlyfigure(datapath):
    with open(datapath) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x = 'Coffee', y = 'sleep')
        fig.show()

def getdatasource(datapath):
    coffee = []
    sleep = []

    with open(datapath) as f:
        df = csv.DictReader(f)
        for row in df:
            coffee.append(int(row['Coffee']))
            sleep.append(int(row['sleep']))
    
    return{'x': coffee, 'y': sleep}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource['x'],datasource['y'])
    print(correlation[0,1])

def setup():
    datapath = './cups of coffee vs hours of sleep.csv'
    datasource = getdatasource(datapath)
    findCorrelation(datasource)
    plotlyfigure(datapath)

setup() 