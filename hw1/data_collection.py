import pandas as pd

# Read csv data into pandas dataframe
df = pd.read_csv('IRAhandle_tweets_1.csv')

# Select only first 10000 tweets
df = df.drop(df[df.index >= 10000].index)

# Filter out non-English tweets
df = df.drop(df[df['language'] != 'English'].index)

# Filter out tweets with questions
df = df.drop(df[df['content'].str.contains('?', regex=False)].index)

# Create tsv file with selected data
df.to_csv('initialized_data.tsv', sep="\t")