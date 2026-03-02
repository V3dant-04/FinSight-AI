import numpy as np

def forecast_next(values, window=3):
    if len(values) < window:
        return round(np.mean(values), 2)
    return round(np.mean(values[-window:]), 2)
