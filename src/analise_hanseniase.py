import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plotar_grafico(var_data, var_x, var_y, var_title, var_media_movel=""):
    plt.figure(figsize=(15,5))

    sns.lineplot(x=var_x, y=var_y, data=var_data, palette="tab10", linewidth=1.5)

    if var_media_movel != "":
        sns.lineplot(x='Data', y= var_media_movel, data= var_data)

    plt.title(var_title)
    plt.xticks(rotation= 30)
    plt.show()


#importar dados
url_file_han = 'E:/DADOS/Marcelo/Bootcamp/DS/analise_previsao_series_temporais/dados/Hanseniase.csv'

dados = pd.read_csv(url_file_han, encoding='ISO-8859-1', sep=';', skiprows=3, skipfooter=10, engine='python')


#dropar as colunas e as linhas
dados = dados.drop("Total",axis=1)
dados = dados.drop(0,axis=0)
dados = dados.drop(46,axis=0)
dados = dados.replace('-',0)

#verificar os dados
#print(dados.head(10))

#criar um novo dataframe para facilitar o trabalhos com as séries temporais
dados_time_series = dados.melt(id_vars="Ano Diagnóstico", value_name="Casos", var_name="Mes")
dados_time_series['Data'] = dados_time_series["Ano Diagnóstico"] + "-" + dados_time_series["Mes"]

#Converter a coluna Caos em int
dados_time_series['Casos'] = pd.to_numeric(dados_time_series['Casos'])


#print(dados_time_series.info())


#converter a coluna Data em datetime
meses_dict = {'Jan':'Jan',
                'Fev':'Feb',
                'Mar':'Mar',
                'Abr':'Apr',
                'Mai':'May',
                'Jun':'Jun',
                'Jul':'Jul',
                'Ago':'Aug',
                'Set':'Sep',
                'Out':'Oct',
                'Nov':'Nov',
                'Dez':'Dec'}

dados_time_series['Mes'] = dados_time_series['Mes'].map(meses_dict)
dados_time_series.sample(5)
dados_time_series['Data'] = dados_time_series["Ano Diagnóstico"] + "-" + dados_time_series["Mes"]
dados_time_series['Data'] = pd.to_datetime(dados_time_series['Data'])
dados_time_series = dados_time_series[['Data','Casos']]

#ordenar o dataset pela data
dados_time_series =  dados_time_series.sort_values(by=['Data'])

dados_time_series = dados_time_series.reset_index(drop= True)

#criar as médias móveis
dados_time_series['MM_3'] = dados_time_series['Casos'].rolling(3).mean()
dados_time_series['MM_6'] = dados_time_series['Casos'].rolling(6).mean()
dados_time_series['MM_3c'] = dados_time_series['Casos'].rolling(3, center= True).mean()
dados_time_series['MM_6c'] = dados_time_series['Casos'].rolling(6, center= True).mean()
dados_time_series['MM_12c'] = dados_time_series['Casos'].rolling(12, center= True).mean()



#verificar os dados
#print(dados_time_series)


plotar_grafico(dados_time_series, 'Data', 'Casos', 'Número de casos de hanseníase - Ano do Diagnóstico','MM_6c')
