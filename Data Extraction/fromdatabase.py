# This file reads the data from the SQLite database and combines the results and tasks tables based on the primary key.
# It then parses the JSON string in the 'json_string' column and extracts the relevant data.
# The final DataFrame is saved as a CSV file.
# Written by: Lewis Watson

import sqlite3
import json
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('database.db')

# Query the data from the tables and join them based on the primary key
query = '''
    SELECT r.id, r.json_string, r.prolific_id, t.task_number, t.time_allocated, t.session_id, t.status
    FROM results r
    JOIN tasks t ON r.id = t.id
'''
df = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# Parse the JSON string and extract the relevant data
import re

def parse_json(json_string):
    try:
        # Replace single quotes with double quotes
        json_string = re.sub(r"'", '"', json_string)
        data = json.loads(json_string)
        meanings = {int(key): value['meaning'] for key, value in data.items() if key.isdigit()}
        task_id = data.get('task_id')
        prolific_pid = data.get('prolific_pid')
        session_id = data.get('session_id')
        return pd.Series({
            **{f'meaning_{key}': value for key, value in meanings.items()},
            'task_id': task_id,
            'prolific_pid': prolific_pid,
            'session_id': session_id
        })
    except (json.JSONDecodeError, KeyError) as e:
        # Print the problematic JSON string and the error message
        print(f"Failed to parse JSON string: {json_string}")
        print(f"Error: {str(e)}")
        return pd.Series()

# Apply the parsing function to the 'json_string' column
df = pd.concat([df, df['json_string'].apply(parse_json)], axis=1)

# Drop the original 'json_string' column
df = df.drop('json_string', axis=1)

# Save the DataFrame as a CSV file
df.to_csv('combined_results.csv', index=False)