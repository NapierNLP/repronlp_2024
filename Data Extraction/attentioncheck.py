import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('full_data.csv')
counter = 0

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    failed_attention_check = False

    # Iterate over each task/row (0 to 31)
    for i in range(32):
        # Check if the system is 'distractor' and the participant selected it as the best for 'meaning'
        if (row[f'systema{i}'] == 'distractor' and row[f'meaning_{i}'] == 'A') or \
                (row[f'systemb{i}'] == 'distractor' and row[f'meaning_{i}'] == 'B'):
            failed_attention_check = True
            break

    # If the attention check failed, print the 'id' column and the failure message
    if failed_attention_check:
        print(f"Prolific ID: {row['prolific_id']} - Failed attention check.")
        counter += 1

# Print the total number of participants who failed the attention check
print(f"Total number of participants who failed the attention check: {counter}")
