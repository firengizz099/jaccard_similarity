import pandas as pd
import numpy as np
df = pd.read_csv('your_dataset.csv')

df['column_name_filled'] = df['column_name']

def jaccard_similarity(s1, s2):
    set1 = set(s1.split())
    set2 = set(s2.split())
    return len(set1 & set2) / len(set1 | set2)


for i, row in df.iterrows():
    if pd.isna(row['column_name']):
        max_similarity = 0
        max_similarity_index = 0
        for j, other_row in df.iterrows():
            if i == j or pd.isna(other_row['column_name']):
                continue
            similarity = jaccard_similarity(row['column_name_filled'], other_row['column_name'])
            if similarity > max_similarity:
                max_similarity = similarity
                max_similarity_index = j
        df.at[i, 'column_name_filled'] = df.at[max_similarity_index, 'column_name']

df.to_csv('your_filled_dataset.csv', index=False)