import joblib
import datetime
import numpy as np

def predict(stop, line, direction):
    time_info = datetime.datetime.now()
    data = np.array([[stop, line, direction, time_info.month, time_info.year, time_info.hour, time_info.minute, time_info.second]])
    regr = joblib.load("/app/machine_learning/model.joblib")
    prediction = regr.predict(data)
    return prediction