import pandas as pd

df = pd.read_csv('dataset.tsv', sep='\t')

trump_mentions_percent = df['trump_mention'].value_counts(normalize=True)[True]

new_df = pd.DataFrame(columns=['result', 'value'])

new_df.loc[0] = ['frac-trump-mentions', round(trump_mentions_percent, 3)]

new_df.to_csv('results.tsv', sep='\t')