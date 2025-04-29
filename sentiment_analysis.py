# import pandas as pd

# # Replace this with the path to your parquet file
# file_path = '/Users/trisharayan/Documents/mistrust-healthcare/notes_extract.parquet'

# # Read the parquet file into a DataFrame
# df = pd.read_parquet(file_path)

# # Now df has all the data!
# print(df.head())



import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import numpy as np
import pickle
from tqdm import tqdm

file_path = '/Users/trisharayan/Documents/mistrust-healthcare/notes_extract.parquet'
df = pd.read_parquet(file_path)

df['HADM_ID'] = range(len(df))

analyzer = SentimentIntensityAnalyzer()

sentiments = {}

for _, row in tqdm(df.iterrows(), total=len(df)):
    hadm_id = row['HADM_ID']
    text = row['TEXT']
    
    sentiment_score = analyzer.polarity_scores(text)['compound']
    sentiments[hadm_id] = sentiment_score

scores = np.array(list(sentiments.values()))
mu = scores.mean()
std = scores.std()

standardized_sentiments = {k: (v - mu) / std for k, v in sentiments.items()}

with open('neg_sentiment.pkl', 'wb') as f:
    pickle.dump(standardized_sentiments, f)

print('DONE!')


