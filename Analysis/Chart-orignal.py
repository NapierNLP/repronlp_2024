import matplotlib.pyplot as plt

# Data
data = {
    'VAE': 36,
    'Latent BoW': -16,
    'Separator': -24,
    'HRQ-VAE': 4
}

# Create a list of labels and values
labels = list(data.keys())
values = list(data.values())

# Define colors for each bar
colors = ['blue', 'green', 'red', 'orange']

# Create the bar chart
fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.bar(labels, values, color=colors, width=1)

# Set the y-axis limits to -20 and 20
ax.set_ylim(-40, 40)

# Add a horizontal line at y=0
ax.axhline(y=0, color='black', linestyle='-', linewidth=0.8)

# Add labels and title
ax.set_xlabel('System', fontsize=12)
ax.set_ylabel('Relative Preference %', fontsize=12)
ax.set_title('Original Authors\' Results', fontsize=14)

# Adjust the tick labels font size
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Add value labels on top of each bar
for bar in bars:
    height = bar.get_height()
    if height > 0:
        ax.text(bar.get_x() + bar.get_width() / 2, height+0.5,
                f'+{height}%', ha='center', va='bottom', fontsize=10)
    else:
        ax.text(bar.get_x() + bar.get_width() / 2, height-1,
                f'{height}%', ha='center', va='top', fontsize=10)

# Adjust the layout and display the chart
plt.tight_layout()
plt.show()