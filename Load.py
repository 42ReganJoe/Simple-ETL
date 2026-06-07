import os
import pandas as pd
import sqlite3



# Ensure the output directory exists before saving
output_dir = 'data_output'
os.makedirs(output_dir, exist_ok=True)

# 1. Save to Parquet in the new folder
parquet_path = os.path.join(output_dir, 'machine_learning_ready.parquet')
merged_df.to_parquet(parquet_path, engine='pyarrow', index=False)

# 2. Save to SQLite in the new folder
db_path = os.path.join(output_dir, 'factory_operations.db')
conn = sqlite3.connect(db_path)
daily_stats.to_sql('daily_equipment_stats', conn, if_exists='replace', index=False)
conn.close()