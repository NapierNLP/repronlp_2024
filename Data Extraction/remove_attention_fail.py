# Based on a list of prolific ids, this script will get the ids from the db that should be reset to rerun
# The script will print the ids that will be removed and the number of rows removed
# I will manually remove the rows from the db - both results and tasks tables

import sqlite3
import pandas as pd

# prolific_ids to remove
#prolific_ids = ['60d390bf1edffb6fdd78488b', '5c50cd6cd5f934000198d5d6', '5efc4644f6f5950008d892a2', '6384f755b4cc19e1153f51bb', '642ee08bca2effffc9e754e2']
prolific_ids = ['629e112d75f3665c8362ab6f']

# Connect to the SQLite database
conn = sqlite3.connect('database.db')

# Query the data from the tables and join them based on the primary key
query = '''
    SELECT r.id, r.json_string, r.prolific_id, t.task_number, t.time_allocated, t.session_id, t.status
    FROM results r
    JOIN tasks t ON r.id = t.id
'''
df = pd.read_sql_query(query, conn)

# Remove the rows associated with the specified prolific_ids
removed_rows = df[df['prolific_id'].isin(prolific_ids)]
df = df[~df['prolific_id'].isin(prolific_ids)]

# Print the id and for each row that is removed
for index, row in removed_rows.iterrows():
    print(f"Prolific ID: {row['prolific_id']} - Removed row with id: {row['id']}")

# Output the number of rows removed from the database
print(f"Number of rows removed: {len(removed_rows)}")

# Close the database connection
conn.close()

