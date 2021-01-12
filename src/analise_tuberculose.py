import pandas as pd

url_file = 'dados\A105613189_28_143_208.csv'

dados = pd.read_csv(url_file, encoding='ISO-8859-1', sep=';', skiprows=3, skipfooter=16, engine='python')
print(dados.head())



# Desafio 01: Transformar os dados em uma série temporal: ANO-MES