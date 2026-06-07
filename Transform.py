import pandas as pd

from Extract import extract_logs, extract_sensor

df_sensor = extract_sensor()
df_logs = extract_logs()

df_sensor["temperature_celsius"] = df_sensor.groupby("equipment_id")["temperature_celsius"].transform(lambda x:x.fillna(x.rolling(window=3, min_periods=1).mean()))

df_merge =df_sensor.merge(df_logs,on="equipment_id")
df_merge["timestamp"] = pd.to_datetime(df_merge["timestamp"],format="mixed").dt.date
df_merge["last_maintenance_date"] = pd.to_datetime(df_merge["last_maintenance_date"], format="mixed").dt.date
df_merge["days_since_maintenance"] = df_merge["timestamp"] - df_merge["last_maintenance_date"]
daily_stats = df_merge.groupby(['last_maintenance_date', 'equipment_id']).agg(
    max_vibration_hz=('vibration_hz', 'max'),
    avg_temperature_celsius=('temperature_celsius', 'mean')
).reset_index()

print(df_merge["days_since_maintenance"])
print(daily_stats)