import pandas as pd

df = pd.read_csv('initialized_data.tsv', sep='\t')

df = df.filter(['tweet_id', 'publish_date', 'content'])

df['trump_mention'] = df['content'].str.contains('Trump', regex=False)

df.to_csv('dataset.tsv', sep='\t')