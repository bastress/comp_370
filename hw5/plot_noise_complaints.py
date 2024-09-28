import pandas as pd
import matplotlib.pyplot as plt

# Function to read the CSV files without headers and process them into complaint categories
def process_csv(file_path):
    # Read the CSV without headers and assign column names
    df = pd.read_csv(file_path, header=None, names=['Date', 'Complaint Type'])
    # Simplify the complaint type by removing "Noise - "
    df['Complaint Type'] = df['Complaint Type'].str.replace('Noise - ', '', regex=False)
    # Return the percentage of each complaint type
    return df['Complaint Type'].value_counts(normalize=True) * 100

# File paths for your CSV files
csv_files = ['quarter1.csv', 'quarter2.csv', 'quarter3.csv', 'quarter4.csv']

# Process the data for each quarter
quarterly_data = [process_csv(file) for file in csv_files]

# Get all unique complaint categories across all quarters
all_categories = pd.concat(quarterly_data).index.unique()

# Define a color map (you can adjust the colors as needed)
color_map = {
    category: plt.cm.tab20(i / len(all_categories)) for i, category in enumerate(all_categories)
}

# Labels for each chart
labels = ["1st Quarter", "2nd Quarter", "3rd Quarter", "4th Quarter"]

# Set up the figure and axes for the pie charts
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
axs = axs.ravel()

# Loop through each quarter and plot a pie chart without individual legends
for i, data in enumerate(quarterly_data):
    # Ensure consistent color order based on all categories
    colors = [color_map[category] for category in data.index]
    
    axs[i].pie(data, autopct='%1.1f%%', startangle=90, colors=colors)
    axs[i].set_title(labels[i])

# Create a single legend for all charts
handles = [plt.Line2D([0], [0], color=color_map[category], marker='o', linestyle='') for category in all_categories]
fig.legend(handles, all_categories, title="Complaint Category", loc="lower center", ncol=4)

# Adjust layout to prevent overlapping
plt.tight_layout(rect=[0, 0.1, 1, 1])  # Leave space for the legend at the bottom

# Save the figure with all pie charts and a single legend
plt.savefig('task1_plot.png')

# Show the plots
plt.show()


