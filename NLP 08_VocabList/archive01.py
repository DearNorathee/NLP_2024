# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 13:14:44 2023

@author: Heng2020
"""
import nltk
import spacy
from collections import Counter
import pandas as pd
import seaborn as sns
import textstat
import matplotlib.pyplot as plt


doc = model(single_text)
entities = [[ent.text,ent.label_] for ent in doc.ents]
entities = pd.DataFrame(entities, columns=['Text', 'Label'])
sentence = [sent.text for sent in doc.sents]

df_group['easy_score1'] = df_group['word'].apply(lambda row: textstat.crawford(row))
df_group['easy_score2'] = df_group['word'].apply(lambda row: textstat.gutierrez_polini(row))
df_group['easy_score3'] = df_group['word'].apply(lambda row: textstat.szigriszt_pazos(row))
df_group['easy_score4'] = df_group['word'].apply(lambda row: textstat.fernandez_huerta(row))

x = 'count_infinitive'
y = 'easy_score1'
plot_score['counts'] = df_group.groupby(['count_infinitive', 'easy_score1'])['easy_score1'].transform('count')
sns.scatterplot(data = plot_score, x = 'count_infinitive', y = 'easy_score1',size='counts', sizes=(20, 300))
plt.title('Easyscore 1')

x = 'count_infinitive'
y = 'easy_score2'
plot_score['counts'] = df_group.groupby([x, y])[y].transform('count')
sns.scatterplot(data = plot_score, x = x, y = y,size='counts', sizes=(20, 300))
plt.title('Easyscore 2')

x = 'count_infinitive'
y = 'easy_score3'
plot_score['counts'] = df_group.groupby([x, y])[y].transform('count')
sns.scatterplot(data = plot_score, x = x, y = y,size='counts', sizes=(20, 300))
plt.title('Easyscore 3')

x = 'count_infinitive'
y = 'easy_score4'
plot_score['counts'] = df_group.groupby([x, y])[y].transform('count')
sns.scatterplot(data = plot_score, x = x, y = y,size='counts', sizes=(20, 300))
plt.title('Easyscore 4')
