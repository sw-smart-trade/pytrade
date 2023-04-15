import os
import io
import json
import wget
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

directory = 'data'

portfolio_map = [[0, 30],[31,69],[70,100]]

def stock_recommendations(top: int):
    """Function called by recommendations endpoint."""
    print(top)
    data = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f) and f != 'data/.DS_Store':
            df = pd.read_csv(f)
            data.append([f.split('/')[1].split('.')[0],df['Close'].iloc[-1],df['Low'].min(),df['High'].max(),df['Close'].iloc[-1]/df['High'].max()])
            
    recom = pd.DataFrame(data, columns=['STOCK','CLOSING', 'MIN', 'MAX', 'POTENTIAL']).sort_values('POTENTIAL') 
    return recom.head(top).to_json(orient='records')


def recommendation(stock: str):
    """Function called by recommendation endpoint."""
    data = []
    f = os.path.join(directory, stock)
    f = f + '.csv'

    # checking if it is a file
    if os.path.exists(f):
        print("File exist!")
    else:
        url = 'https://query1.finance.yahoo.com/v7/finance/download/' + stock + '?period1=1649458964&period2=1680994964&interval=1d&events=history&includeAdjustedClose=true'
        wget.download(url, './data/' + stock + '.csv') 

    if os.path.isfile(f) and f != 'data/.DS_Store':
        df = pd.read_csv(f)
        data.append([f.split('/')[1].split('.')[0],df['Close'].iloc[-1],df['Low'].min(),df['High'].max(),df['Close'].iloc[-1]/df['High'].max()])
        recom = pd.DataFrame(data, columns=['STOCK','CLOSING', 'MIN', 'MAX', 'POTENTIAL']).sort_values('POTENTIAL')
        return recom.to_json(orient='records')
    else:
        return "Stock not found."
