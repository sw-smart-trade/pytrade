import os
import io
import json
import wget
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

directory = 'data'

portfolio_map = [[0, 30],[31,69],[70,100]]


def portfolio_builder(profile: int):
    """Function called by portfolio endpoint."""
    data = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f) and f != 'data/.DS_Store':
            print(f)
            df = pd.read_csv(f)
            pot = 0
            if isinstance(np.float64(df['Close'].iloc[-1]), np.floating) and isinstance(np.float64(df['High'].max()), np.floating):
                pot = (df['Close'].iloc[-1]/df['High'].max())*100
                pot = pd.to_numeric(pot, errors='coerce')
                pot = pot.astype(int)
            data.append([f.split('/')[1].split('.')[0],df['Close'].iloc[-1],df['Low'].min(),df['High'].max(),pot])
            
    recom = pd.DataFrame(data, columns=['STOCK','CLOSING', 'MIN', 'MAX', 'POTENTIAL']).sort_values('POTENTIAL') 

    if profile > 0 and profile < 4:
        recom = recom[recom['POTENTIAL'].between(portfolio_map[profile-1][0], portfolio_map[profile-1][1])]
        return recom.to_json(orient='records')
    else:
        return json.dumps({"error": "Profile should be between 1 and 3"})
        
