import csv
import pandas as pd
import pprint

word_freq = dict()
tag_freq = dict()
tagged_words = pd.read_csv('training-data-with-start-tag-dummy.tsv', delimiter='\t', encoding='utf-8',
    names=['word', 'tag'], header=None)
transition = ['present', 'new']
trans_list = []
for index, row in tagged_words.iterrows():
    if row['tag'] != 'START':
        trans_list.append((tagged_words.iloc[index - 1]['tag'], row['tag']))

df_transition = pd.DataFrame(trans_list)
df_transition.rename(columns={0:'present', 1:'new'}, inplace=True)
print(df_transition.head(30))

grouped = df_transition.groupby(['present'])
print(grouped.count())
print(grouped.get_group('CC'))
print(grouped.filter(lambda x: x if x.new == "NN"))

# with open('training-data.tsv') as tsvfile:
#     reader = csv.DictReader(tsvfile, dialect='excel-tab', fieldnames=['kata', 'tag'])
#     for row in reader:
#         if row['kata'] == '\n':
#             print("Batas")
#         if row['kata'] in word_freq:
#             word_freq[row['kata']] += 1
#         else:
#             word_freq[row['kata']] = 1
        
#         if row['tag'] in tag_freq:
#             tag_freq[row['tag']] += 1
#         else:
#             tag_freq[row['tag']] = 1

# pprint.pprint(word_freq['.'])
# pprint.pprint(tag_freq)
