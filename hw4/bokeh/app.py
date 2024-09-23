from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Select
from bokeh.plotting import figure
import pandas as pd
from datetime import datetime

# Function to preprocess the data (no need for 2020 filtering)
def preprocess_data(filename):
    # Load only the columns you need (Created Date, Closed Date, and Incident Zip)
    df = pd.read_csv(filename, header=None, usecols=[1, 2, 8], parse_dates=[1, 2])

    # Assign custom column names to the selected columns
    df.columns = ['Created Date', 'Closed Date', 'Incident Zip']

    # Convert the date columns to datetime format (this should already be handled by parse_dates)
    df['Created Date'] = pd.to_datetime(df['Created Date'], format='%m/%d/%Y %I:%M:%S %p', errors='coerce')
    df['Closed Date'] = pd.to_datetime(df['Closed Date'], format='%m/%d/%Y %I:%M:%S %p', errors='coerce')

    # Filter out incidents that are not closed
    df = df.dropna(subset=['Closed Date'])

    # Create a new column for response time in hours
    df['Response Time (hours)'] = (df['Closed Date'] - df['Created Date']).dt.total_seconds() / 3600

    # Group data by month and zipcode and calculate the average response time
    df_aggregated = df.groupby([df['Created Date'].dt.to_period('M'), 'Incident Zip'])['Response Time (hours)'].mean().reset_index()

    # Convert 'Created Date' back to timestamp for Bokeh compatibility
    df_aggregated['Created Date'] = df_aggregated['Created Date'].dt.to_timestamp()

    return df_aggregated

# Preprocess the data
data_file = '../large_test_data.csv'  # Replace with your actual file path
df = preprocess_data(data_file)

# Create a ColumnDataSource for all data (default data for all zipcodes)
source_all = ColumnDataSource(df.groupby('Created Date')['Response Time (hours)'].mean().reset_index())

# Function to filter data by zipcode
def filter_zipcode_data(zipcode):
    return df[df['Incident Zip'] == zipcode].groupby('Created Date')['Response Time (hours)'].mean().reset_index()

# Create default ColumnDataSource for two example zipcodes
source_zip1 = ColumnDataSource(filter_zipcode_data(df['Incident Zip'].unique()[0]))
source_zip2 = ColumnDataSource(filter_zipcode_data(df['Incident Zip'].unique()[1]))

# Create the dropdown widgets
zipcode_select_1 = Select(title="Zipcode 1", value=str(df['Incident Zip'].unique()[0]), options=[str(zip) for zip in df['Incident Zip'].unique()])
zipcode_select_2 = Select(title="Zipcode 2", value=str(df['Incident Zip'].unique()[1]), options=[str(zip) for zip in df['Incident Zip'].unique()])

# Create the plot
plot = figure(title="Average Incident Response Time (Hours)", x_axis_type='datetime', height=400, width=700)
plot.line('Created Date', 'Response Time (hours)', source=source_all, legend_label="All Zipcodes", color="blue", line_width=2)
plot.line('Created Date', 'Response Time (hours)', source=source_zip1, legend_label="Zipcode 1", color="green", line_width=2)
plot.line('Created Date', 'Response Time (hours)', source=source_zip2, legend_label="Zipcode 2", color="red", line_width=2)

# Configure the plot axes and legend
plot.legend.location = "top_left"
plot.xaxis.axis_label = "Date"
plot.yaxis.axis_label = "Response Time (Hours)"

# Function to update the plot when the dropdown values change
def update_plot(attr, old, new):
    zipcode1 = zipcode_select_1.value
    zipcode2 = zipcode_select_2.value

    new_data_zip1 = filter_zipcode_data(zipcode1)
    new_data_zip2 = filter_zipcode_data(zipcode2)
    
    # Update the data property with a dictionary, not another CDS object
    source_zip1.data = dict(ColumnDataSource(new_data_zip1).data)
    source_zip2.data = dict(ColumnDataSource(new_data_zip2).data)

# Set up callbacks for the dropdown widgets
zipcode_select_1.on_change('value', update_plot)
zipcode_select_2.on_change('value', update_plot)

# Layout the dashboard
layout = column(zipcode_select_1, zipcode_select_2, plot)

# Add layout to the current document
curdoc().add_root(layout)
curdoc().title = "NYC 311 Response Time Dashboard"
