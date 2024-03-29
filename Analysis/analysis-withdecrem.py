import pandas as pd

# Read the CSV file
data = pd.read_csv('full_data.csv')

# Get the unique task numbers
unique_tasks = data['task_number'].unique()

# Initialise a dictionary to store the preference counts for each system
system_preferences = {}

# Initialize a variable to keep track of total comparisons
total_comparisons = 0

# Iterate over each unique task number
for task_number in unique_tasks:
    # Get the rows for the current task number
    task_data = data[data['task_number'] == task_number]

    # Iterate over the meaning columns
    for i in range(32):
        # Get the count of 'A' and 'B' for the current meaning column
        count_a = (task_data[f'meaning_{i}'] == 'A').sum()
        count_b = (task_data[f'meaning_{i}'] == 'B').sum()

        # Get the system names for the current meaning column
        systema = task_data[f'systema{i}'].iloc[0]
        systemb = task_data[f'systemb{i}'].iloc[0]

        # Attention check: skip if systema or systemb is 'inputs' or 'golds'
        if systema == 'inputs' or systema == 'golds' or systemb == 'inputs' or systemb == 'golds':
            continue

        # Update the preference counts for each system: increment preferred system by 1 and decrement non-preferred system by 1
        if count_a > count_b:
            system_preferences[systema] = system_preferences.get(systema, 0) + 1
            system_preferences[systemb] = system_preferences.get(systemb, 0) - 1
        elif count_b > count_a:
            system_preferences[systemb] = system_preferences.get(systemb, 0) + 1
            system_preferences[systema] = system_preferences.get(systema, 0) - 1

        # Increment the total comparisons
        total_comparisons += 1

# Calculate the average number of preferences across all systems
total_systems = len(system_preferences)
average_preferences = total_comparisons / total_systems
print("Average preferences:", average_preferences)
print("Total comparisons:", total_comparisons)
print("Total systems:", total_systems)
print()

# Calculate the relative preference percentage for each system
relative_preferences = {}
for system, preferences in system_preferences.items():
    relative_preference = (preferences / total_comparisons) * 100
    relative_preferences[system] = relative_preference

# Print the results
for system, preference in relative_preferences.items():
    print(f"{system}: {preference:.2f}%")

print()
print(system_preferences)