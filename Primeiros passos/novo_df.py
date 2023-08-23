##### Criando um dataframe enriquecido dos dados coletados
### Importando bilbiotecas
import pandas as pd
import pathlib
import json

# Definindo diretório
PATH = (".")

# Funcao para extrair informacoes do json
## Dataset final: c("territory_id", "date", "territory_name", "state_code",
# "excerpts")
def extract_urls(json_file):
    diarios = []
    for item in json_file['gazettes']:
        pass

    return diarios

with open('./raw_data/dataset1_rede_cegonha.json', 'r', encoding='utf-8') as json_file:
    df = json_file.read()

dict= json.loads(df["gazettes"])
df2 = pd.DataFrame.from_dict(dict, orient="index")
print(df2.head())

