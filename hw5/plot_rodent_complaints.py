import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# File path to your CSV file
csv_file = 'rodent_complaints_location_counts.csv'

# Grouped categories dictionary
grouped_categories = {
    'Family Residences': [
        '1-2 Family Dwelling', '1-2 Family Mixed Use Building', '1-3 Family Dwelling',
        '1-3 Family Mixed Use Building', '3+ Family Apartment Building',
        '3+ Family Apt. Building', '3+ Family Mixed Use Building', 'Residential Building', 'Residence'
    ],
    'Vacant Properties': [
        'Vacant Building', 'Vacant Lot'
    ],
    'Commercial Properties': [
        'Commercial Building', 'Retail Store', 'Restaurant', 'Restaurant/Bar/Deli/Bakery',
        'Parking Lot/Garage', 'Construction Site'
    ],
    'Other': []
}

# Initialize counts for each category
category_counts = {
    'Family Residences': 0,
    'Vacant Properties': 0,
    'Commercial Properties': 0,
    'Other': 0
}

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file, header=None, names=['count', 'location_type'])

# Iterate over each row and categorize the location types
for index, row in df.iterrows():
    location_type = row['location_type']
    count = row['count']

    # Check which category the location type belongs to
    found_category = False
    for category, types in grouped_categories.items():
        if location_type in types:
            category_counts[category] += count
            found_category = True
            break

    # If location type doesn't fit any predefined category, add it to 'Other'
    if not found_category:
        category_counts['Other'] += count

# Prepare data for visualization
categories = list(category_counts.keys())
complaint_counts = list(category_counts.values())

# Create the bar chart
x = np.arange(len(categories))  # the label locations
width = 0.7  # the width of the bars

fig, ax = plt.subplots()
bars = ax.bar(x, complaint_counts, width, label='Rodent Complaints')

# Add labels, title, and custom ticks
ax.set_ylabel('Number of Complaints')
ax.set_title('Rodent Complaints by Building/Property Type')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.bar_label(bars, padding=3)

# Display the chart
plt.tight_layout()
plt.savefig('task2_plot.png')
plt.show()
