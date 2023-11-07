import pandas as pd
import pathlib

PATH = (".")

diarios = pd.read_csv("./raw_data/saude_dataset1.csv", header = 0, encoding='utf-8')
print(diarios.head(10))

print(list(diarios.columns))
diarios_dataset = diarios[['excerpt', 'excerpt_subthemes']]
print(diarios_dataset.head(5))

### Tecnicas de Pré-processamento
# Stopwords

# Remover pontuação

