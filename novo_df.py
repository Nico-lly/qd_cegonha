##### Criando um dataframe enriquecido dos dados coletados
### Importando bibliotecas
import pandas as pd
import pathlib
import json
#https://github.com/okfn-brasil/querido-diario-api

# Definindo diretório
PATH = (".")

# Funcao para extrair informacoes do json
## Dataset final: c("territory_id", "date", "territory_name", "state_code",
# "excerpts")

with open('./raw_data/response_1000db.json', 'r', encoding='utf-8') as json_file:
    data1 = json.load(json_file)
    
with open('./raw_data/response_406db.json', 'r', encoding='utf-8') as json_file:
    data2 = json.load(json_file)

data1 = data1['gazettes']
data2 = data2['gazettes']
data = data1 + data2

## Checando os dados
print(len(data))

# Criando um dataframe e checando o territory_id
df = pd.DataFrame(data, columns=['territory_id', 'date', 'territory_name', 'state_code', 'excerpts'])
df['mes_dia'] = df['date'].str.extract(r'(\d{2}-\d{2})')

#df['date'] = pd.to_datetime(df['date'])
#df['mes_dia'] = df['date'].dt.strftime('%m-%d')

count_id = df['territory_id'].value_counts()
count_date = df['date'].value_counts()
##count_mes_dia = df['mes_dia'].value_counts().reset_index()

df['count_id'] = df['territory_id'].map(count_id)
df['count_date'] = df['date'].map(count_date)
##df['count_mes_dia'] = df['territory_id'].map(count_mes_dia)

print("Dia/mes/ano com mais publicações")
print(df.sort_values(by='count_date', ascending=False).head(20))
### Muitas repetições do dia 30/12, mas o dia exato foram 18 datas que se repetiram 3 vezes.
print("Dia/mes com mais publicações")
#print(df.sort_values(by='count_dia_mes', ascending=False).head(20))
###
print('Publicações mais antigas')
print(df.sort_values(by='date', ascending=True))
### Publicações mais antigas 11/08/2011 (Santos), 06/01/2012 (Salvador), 02/05/2012 (Salvador), 03/05/2012 (Rio de Janeiro).

df_cities = df.drop_duplicates(subset=['territory_id'])
print("Cidades que mais publicaram")
pd.set_option('display.max_columns', None)
print(df_cities.sort_values(by='count_id', ascending=False))
### Cidades que mais publicaram: Cuiabá (60), Uberaba (45), Jundiaí (43) e Guarulhos (28)

