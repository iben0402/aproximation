import pandas as pd
import numpy as np

def get_data_random(path, amount=50):
    data = pd.read_csv(path)
    data.columns = ['x','y']
    idx = np.random.choice(range(len(data)), amount, replace=False)
    idx = np.sort(idx)
    x = data['x'].to_numpy()
    y = data['y'].to_numpy()
    x = x[idx]
    y = y[idx]
    return x, y

def get_data_regular(path, amount=50):
    data = pd.read_csv(path)
    data.columns = ['x','y']
    x = data['x'].to_numpy()
    y = data['y'].to_numpy()
    idx = np.linspace(0, len(data)-1, amount, dtype=int)
    x = x[idx]
    y = y[idx]
    return x, y

def get_all_data(path):
    data = pd.read_csv(path)
    data.columns = ['x','y']
    x = data['x'].to_numpy()
    y = data['y'].to_numpy()
    return x, y