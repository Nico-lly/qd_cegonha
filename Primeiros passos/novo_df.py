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
    data = json.load(json_file)

data = data['gazettes']

# Create a DataFrame
df = pd.DataFrame(data, columns=['territory_id', 'date', 'territory_name', 'state_code', 'excerpts'])

count_id = df['territory_id'].value_counts()
count_date = df['date'].value_counts()

df['count_id'] = df['territory_id'].map(count_id)
df['count_date'] = df['date'].map(count_date)

print(df.sort_values(by='count_id', ascending=False))
print(df.sort_values(by='date', ascending=False))
print(df.sort_values(by='date', ascending=True))

### Não tem nenhuma data repetida. Mais menções são Goiânia e Maceió.