import pandas as pd

# Read the combined_results.csv file
combined_df = pd.read_csv('combined_results.csv')

# Read the authors_data.csv file
authors_df = pd.read_csv('authors_data.csv')

# Reset the index of authors_df to start from 1 instead of 0
authors_df.reset_index(inplace=True)
authors_df['index'] += 1  # Adjust the index to start from 1
authors_df.rename(columns={'index': 'task_number'}, inplace=True)

# Ensure the 'task_number' columns in both dataframes are of the same data type
combined_df['task_number'] = combined_df['task_number'].astype(int)
authors_df['task_number'] = authors_df['task_number'].astype(int)

# Merge the dataframes based on the 'task_number' column
merged_df = pd.merge(combined_df, authors_df, on='task_number', how='left')

# Save the merged dataframe to a new file called full_data.csv
merged_df.to_csv('full_data.csv', index=False)
