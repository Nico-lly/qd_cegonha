import pandas as pd
import pathlib

PATH = (".")

diarios = pd.read_csv("./raw_data/saude_dataset1.csv", header = 0, encoding='utf-8')
print(diarios.head(10))

print(list(diarios.columns))
diarios_dataset = diarios[['excerpt', 'excerpt_subthemes']]
print(diarios_dataset.head(5))

### Tecnicas de Pré-processamento
# 1. Stopwords

# 2. Normalização
#remover pontuacao
#remover jargoes ?
#ref: Investigating the impact of pre‑processing techniques and pre‑trained word embeddings 
#in detecting Arabic health information on social media

# 3. Lowercase

# 4. Lematização

# 5. Tokenização

# 6. POS

# 7. Remover números

# 8. Generalização das palavras

## outra ref: Repositorio Fabio Colado

