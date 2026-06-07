import pandas as pd



def extract_logs():
    data1 = pd.read_json(r"C:\Users\USER\PycharmProjects\PythonProject6\maintenance_logs.json")
    df1 = pd.DataFrame(data1)
    return df1

def extract_sensor():
    data2 = pd.read_csv(r"C:\Users\USER\PycharmProjects\PythonProject6\sensor_telemetry.csv")
    df2 = pd.DataFrame(data2)
    return df2

