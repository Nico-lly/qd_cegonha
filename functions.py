import requests
import pandas as pd
import urllib.request
import re
import zipfile
import re
import numpy as np
import itertools

def new_concat(df, new_column, *args):
    df[new_column] = ''
    for col in args:
        df[new_column] += df[col]
    return df


def padronizar_coluna(df, nome_coluna):
    substituicoes = {
        'ã': 'a',
        'á': 'a',
        'à' : 'a',
        'é' : 'e',
        'í' : 'i',
        'ó' : 'o',
        'ú' : 'u',
        '\'' : '' 
    }
    df[nome_coluna] = df[nome_coluna].str.lower()
    df.replace({' ': '-'}, regex=True)
    for padrao, substituicao in substituicoes.items():
        regex = re.compile(padrao, flags=re.IGNORECASE | re.UNICODE)
        df[nome_coluna] = df[nome_coluna].apply(lambda x: regex.sub(substituicao, str(x)))
 
    return df


def edit_plot():
    pass
