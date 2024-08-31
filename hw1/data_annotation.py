import pandas as pd

df = pd.read_csv('initialized_data.tsv', sep='\t')

df = df.filter(['tweet_id', 'publish_date', 'content'])

df['trump_mention'] = df['content'].str.contains('([^a-zA-Z\\d]Trump[^a-zA-Z\\d]|^Trump[^a-zA-Z\\d]|[^a-zA-Z\\d]Trump$)', case=True, regex=True)

df.to_csv('dataset.tsv', sep='\t')