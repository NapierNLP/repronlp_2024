# Description: This script reads the combined_results.csv file and checks if each task number has exactly three unique ids.

import pandas as pd

# Load the CSV file
df = pd.read_csv('combined_results.csv')

# Check if task_number column has values from 1 to 60
if set(range(1, 61)) != set(df['task_number']):
    print("Not all task numbers from 1 to 60 are present.")
else:
    # Group by task_number and count the unique ids
    grouped = df.groupby('task_number')['id'].nunique()

    # Check if each task_number has exactly three unique ids
    if (grouped == 3).all():
        print("Each task number has exactly three unique ids.")
    else:
        print("Not all task numbers have exactly three unique ids.")
