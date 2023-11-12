import pandas as pd 
import numpy as np 
import re, string 

import nltk.corpus
from sklearn.linear_model import LogisticRegression
#from sklearn.linear_model import svm
#from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
import zipfile

import pre_processamento
PATH = (".")

with zipfile.ZipFile("./raw_data/saude.csv.zip", 'r') as zip_ref:
    with zip_ref.open('saude.csv') as arquivo_csv:
        # Ler o CSV usando o pandas
        df = pd.read_csv(arquivo_csv)

#diarios = pd.read_csv("./raw_data/saude_dataset1.csv", header = 0, encoding='utf-8')
stopwords_pt = set(nltk.corpus.stopwords.words('portuguese'))

df['numeric_values'] = LabelEncoder().fit_transform(df['excerpt_subthemes'].apply(lambda x: ' '.join(x)))

##### Classificadores
X1 = pre_processamento.remove_stopwords(df, stopwords_pt).values
X1_tfidf = TfidfVectorizer(lowercase=True, analyzer='word').fit_transform(X1)

y = df[['numeric_values']].values
#y_tfidf = TfidfVectorizer(lowercase=False).fit_transform(y)

### Regressão Logística
X_train, X_test, y_train, y_test = train_test_split(X1_tfidf, y, test_size=0.25, random_state=42)
clf = LogisticRegression(random_state=42, C = 0.1, max_iter=500).fit(X_train, y_train)
previsao = clf.predict(X_test)
previsao_proba = clf.predict_proba(X_test)
clf.score(X_test, y_test)

### SVM

### Naive Bayes

#### Acurácia, precisão, recall e F1-score.
# Calculando a acurácia
#accuracy = accuracy_score(y_test, previsao)
#print(f'Acurácia: {accuracy} \n')

# Calculando as métricas de precisão, recall e F1-score
precision = precision_score(y_test, previsao, average='weighted')
recall = recall_score(y_test, previsao, average='weighted')
f1 = f1_score(y_test, previsao, average='weighted')

print(f'Precisão: {precision} \n')
print(f'Recall: {recall} \n')
print(f'F1: {f1} \n')