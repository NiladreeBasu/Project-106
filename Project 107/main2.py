import csv
import plotly.express as px
import numpy as np

def plotlyfigure(datapath):
    with open(datapath) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x = 'Marks', y = 'DaysPresent')
        fig.show()

def getdatasource(datapath):
    marks = []
    days = []

    with open(datapath) as f:
        df = csv.DictReader(f)
        for row in df:
            marks.append(int(row['Marks']))
            days.append(int(row['DaysPresent']))
    
    return{'x': marks, 'y': days}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource['x'],datasource['y'])
    print(correlation[0,1])

def setup():
    datapath = './Student Marks vs Days Present.csv'
    datasource = getdatasource(datapath)
    findCorrelation(datasource)
    plotlyfigure(datapath)

setup() 