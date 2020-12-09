import joblib
from datetime import datetime
import numpy as np
from sklearn.preprocessing import StandardScaler


def predict(stop, line, direction):
    
    day = datetime.today().weekday()
    now = datetime.now().time()

    time = now.strftime("%H:%M:%S").split(":")
    hour = int(time[0])
    minutes = int(time[1])
    seconds = int(time[2])
    if stop in ["6608G", "6650G"]:
        stop = 0.0
    elif stop == "0089":
        stop = 10.0
    else:
        return

    if line == "51":
        line = 20.0
    elif line == "39":
        line = 0.0
    elif line == "44":
        line = 10.0
    elif line == "82":
        line = 30.0
    else:
        return

    if direction == "suburb":
        direction = 10.0
    elif direction == "city":
        direction = 0.0
    else:
        return
    
    print(stop, line, direction, hour, minutes, seconds, day)
    
    data = np.array([stop, line, direction, hour, minutes, seconds, day])

    # Apply a standardscaler
    scaler = StandardScaler()

    data = scaler.fit_transform(data[:,np.newaxis])
    data = np.transpose(data)

    regr = joblib.load("/app/machine_learning/model.joblib")
    prediction = regr.predict(data)
    return prediction