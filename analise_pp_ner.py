### Classificacao por meio de Reconhecimento de Entidades Nomeadas
import spacy
import pre_processamento
import zipfile
import pandas as pd

PATH = (".")

with zipfile.ZipFile("./raw_data/saude.csv.zip", 'r') as zip_ref:
    with zip_ref.open('saude.csv') as arquivo_csv:
        df = pd.read_csv(arquivo_csv)

nlp = spacy.load("pt_core_news_sm")

df_excerpt, list_df_stopwords = pre_processamento.remove_stopwords(df)
#print(list_df_stopwords[1:5])

#doc = [nlp(excerpt) for excerpt in list_df_stopwords]
doc2 = [nlp(excerpt) for excerpt in list_df_stopwords[1:5]]
print([(w.ents) for w in doc2])