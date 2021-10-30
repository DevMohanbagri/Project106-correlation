import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    ice_cream_sales = []
    cold_drink_sales = []

    with open(data_path) as f:
        csvReader = csv.DictReader(f)
        for row in csvReader:
            ice_cream_sales.append(float(row['Temperature']))
            cold_drink_sales.append(float(row['Ice-cream Sales']))
        
    return{'x': ice_cream_sales, 'y':cold_drink_sales }
    
def find_correlation(data_source):
    correlation = np.corrcoef(data_source['x'],data_source['y'])
    print('Correlation between temperature v/s Ice-cream sales:\n--->',correlation[0,1])

def setup():
    data_path = './data/ice-temp.csv'
    data_source = getDataSource(data_path)
    find_correlation(data_source)

setup()