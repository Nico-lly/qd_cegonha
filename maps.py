import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
import pathlib
import json
import functions
import re

#https://geopandas.org/en/stable/docs/user_guide.html

PATH = (".")

map_meso = gpd.read_file('./mapas/mesoregiao-ipeageo/mesoregiao.shp')
map_mun = gpd.read_file('./mapas/BR_Municipios_2022/BR_Municipios_2022.shp')
print(map_mun.head())

#sns.set(style="white", palette="deep", color_codes=True)
#map_meso.plot()
#map_mun.plot()
#plt.figure(figsize=(10, 6))
#plt.show()

### Enriquecendo o shapefile
# 1 - Cidades que estão no QD

with open('./mapas/cidades_qd_011123.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

data = data['cities']
df_qd = pd.DataFrame(data, columns=['territory_id', 'territory_name', 'state_code', 'publication_urls', 'level'])
print(df_qd.head(10))

# lista de municipios por id
lista_id = df_qd['territory_id']
## Conferindo se todos os codigos estão em CD_MUN

# Verificar se todos os valores da lista_id estão em map_mun['CD_MUN']
print(lista_id.isin(map_mun['CD_MUN']).all())

### Inserindo população e Mesorregioes
pop = pd.read_excel("./raw_data/pop_2021.xls", skiprows=1, sheet_name='Municípios', converters={'COD. UF': str, 'COD. MUNIC': str})

new_df = functions.new_concat(pop, 'CD_MUN', 'COD. UF', 'COD. MUNIC')
new_df = new_df.rename(columns={'UF': 'uf', 'COD. UF': 'cod_uf', 'COD. MUNIC': 'cod_mun_old',
                                'NOME DO MUNICÍPIO': 'nome_mun', 'POPULAÇÃO ESTIMADA': 'pop_estim'})

new_df_padrao = functions.padronizar_coluna(new_df, 'nome_mun')
df_qd_padrao = functions.padronizar_coluna(df_qd, 'territory_name')
print(new_df_padrao.head(15))

### Criando nova coluna
map_mun['in_qd'] = map_mun['CD_MUN'].isin(lista_id).astype(int)
print(map_mun['in_qd'].sum())

##### Testando Padronização das colunas
dict_qd = dict(zip(df_qd_padrao['territory_name'], df_qd_padrao['state_code']))
dict_pop = dict(zip(new_df_padrao['nome_mun'], new_df_padrao['uf']))
print(all(val in dict_pop.values() for val in dict_qd.values()))

### Criar nova coluna de proporcao 
regioes = pd.read_excel('./mapas/regioes_geograficas-ibge.xlsx')
regioes.rename(columns={'CD_GEOCODI': 'CD_MUN'}, inplace=True)
regioes['CD_MUN'] = regioes['CD_MUN'].astype(str)
regioes['cod_rgint'] = regioes['cod_rgint'].astype(str)

### Merge populacao e mesorregioes no shapefile
map_enrich = pd.merge(map_mun, new_df_padrao, on='CD_MUN')
map_enrich = pd.merge(map_enrich, regioes, on='CD_MUN')
print(map_enrich.dtypes)
map_enrich['pop_estim'] = map_enrich['pop_estim'].astype(float)

pop_regiao = map_enrich.groupby('cod_rgint')['pop_estim'].sum()
map_enrich['prop_pop'] = map_enrich.apply(lambda row: row['pop_estim'] / pop_regiao[row['cod_rgint']], axis=1)
print(map_enrich.head(5))

# Criando Mapa
## Selecionar maiores concentracoes de populacao por mesorregião?

cidades_valor_1 = map_enrich[map_enrich['in_qd'] == 1]

# Selecione as cidades com proporção maior que 0.4
pop_selected = map_enrich[map_enrich['prop_pop'] > 0.45]

# Ajuste o tamanho da bolha de acordo com a proporção da população
sizes = pop_selected['prop_pop'] * 1000  # Ajuste o fator multiplicador conforme necessário

# Criar figura e eixos
fig, ax = plt.subplots(figsize=(10, 6))

# Primeira camada: cidades com valor 1 em vermelho
map_enrich.plot(ax=ax, color='gray', edgecolor='0.8', linewidth=0.8)
cidades_valor_1.plot(ax=ax, color='red', edgecolor='0.8', linewidth=0.8)

# Segunda camada: bolhas de concentração
#pop_selected.plot(ax=ax, column='pop_estim', cmap='viridis', linewidth=0.8, edgecolor='0.8', legend=True)

# Plotar bolinhas proporcionais à população estimada
pop_selected.geometry.centroid.plot(ax=ax, marker='o', color='blue', markersize=sizes, alpha=0.7)

# Configurações do mapa
ax.set_title("Municípios Incluídos no Querido Diário e Distribuição da População em 2021")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")

# Mostrar o mapa
plt.show()



