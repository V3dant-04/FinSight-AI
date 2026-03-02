import numpy as np

def detect_anomalies(amounts, threshold=2.0):
    """
    Z-score based anomaly detection
    """
    mean = np.mean(amounts)
    std = np.std(amounts)

    anomalies = []
    for i, val in enumerate(amounts):
        z = (val - mean) / std if std != 0 else 0
        if abs(z) > threshold:
            anomalies.append({"index": i, "amount": val, "z_score": round(z, 2)})

    return anomalies
