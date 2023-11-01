import pandas as pd
import pathlib

PATH = (".")

diarios = pd.read_csv("./raw_data/saude_dataset1.csv", delimiter = ',', header = TRUE)
print(diarios.head(10))