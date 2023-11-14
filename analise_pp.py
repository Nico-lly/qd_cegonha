import pandas as pd 
import numpy as np 
import re, string 

import nltk.corpus
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import make_scorer, accuracy_score, precision_score, recall_score, f1_score
from sklearn import metrics
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
import zipfile
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline

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
y = np.ravel(y)

### Regressão Logística
X1_train, X1_test, y_train, y_test = train_test_split(X1_tfidf, y, test_size=0.35, random_state=42)
clf = LogisticRegression(random_state=42, C = 0.1, max_iter=100, solver='sag').fit(X1_train, y_train)
#multinomial: 'sag'
previsao = clf.predict(X1_test)
#previsao_proba = clf.predict_proba(X1_test)
#clf.score(X1_test, y_test)

#### Acurácia, precisão, recall e F1-score.
# Calculando a acurácia
#accuracy = accuracy_score(y_test, previsao)
#print(f'Acurácia: {accuracy} \n')

### Calculando as métricas de precisão, recall e F1-score
#precision = precision_score(y_test, previsao, average='weighted')
#recall = recall_score(y_test, previsao, average='weighted')
#f1 = f1_score(y_test, previsao, average='weighted')
#print(f'Precisão: {precision} \n')
#print(f'Recall: {recall} \n')
#print(f'F1: {f1} \n')

#accuracy_scorer = make_scorer(accuracy_score)
#precision_scorer = make_scorer(precision_score)
#recall_scorer = make_scorer(recall_score)
#f1_scorer = make_scorer(f1_score)

y_pred = clf.predict(X1_test)

#scores_ac = cross_val_score(clf, X1_test, y_test, cv=5, scoring=accuracy_score(y_test, y_pred))
scores_pre = cross_val_score(clf, X1_test, y_test, cv=5, scoring=precision_score(y_test, y_pred, average='weighted', zero_division=1))
scores_rec = cross_val_score(clf, X1_test, y_test, cv=5, scoring=recall_score(y_test, y_pred, average='weighted', zero_division=1))
scores_f1 = cross_val_score(clf, X1_test, y_test, cv=5, scoring=f1_score(y_test, y_pred, average='weighted', zero_division=1))

print('LOGISTIC REGRESSION')
#print("%0.4f de acuracia com D.P de  %0.2f" % (scores_ac.mean(), scores_ac.std()))
print("%0.4f de precisao com D.P de  %0.2f" % (scores_pre.mean(), scores_pre.std()))
print("%0.4f de recall com D.P de  %0.2f" % (scores_rec.mean(), scores_rec.std()))
print("%0.4f de f1 com D.P de  %0.2f" % (scores_f1.mean(), scores_f1.std()))
print('\n\n\n\n')


### SVM
#https://scikit-learn.org/stable/auto_examples/svm/plot_svm_kernels.html#sphx-glr-auto-examples-svm-plot-svm-kernels-py

clf = svm.SVC(kernel='rbf', C=0.5, random_state=42, max_iter=500, decision_function_shape='ovo').fit(X1_train, y_train)

#scores_ac = cross_val_score(clf, X1_test, y_test, cv=5, scoring=accuracy_score(y_test, y_pred))
scores_pre = cross_val_score(clf, X1_test, y_test, cv=5, scoring=precision_score(y_test, y_pred, average='weighted', zero_division=1))
scores_rec = cross_val_score(clf, X1_test, y_test, cv=5, scoring=recall_score(y_test, y_pred, average='weighted', zero_division=1))
scores_f1 = cross_val_score(clf, X1_test, y_test, cv=5, scoring=f1_score(y_test, y_pred, average='weighted', zero_division=1))


print('SVM')
#print("%0.2f de acuracia com D.P de  %0.2f" % (scores_ac.mean(), scores_ac.std()))
print("%0.2f de precisao com D.P de  %0.2f" % (scores_pre.mean(), scores_pre.std()))
print("%0.2f de recall com D.P de  %0.2f" % (scores_rec.mean(), scores_rec.std()))
print("%0.2f de f1 com D.P de  %0.2f" % (scores_f1.mean(), scores_f1.std()))
print('\n\n\n\n')



### Naive Bayes