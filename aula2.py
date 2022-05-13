# lê o arquivo
import pandas as pd

tabela = pd.read_csv("base-de-dados/telecom_users.csv")
tabela = tabela.drop("Unnamed: 0", axis=1) # remove coluna unnamed:0

# ajuste de valores
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# deletando as colunas vazias
tabela = tabela.dropna(how="all", axis=1)

# deletando as linhas vazias
tabela = tabela.dropna(how="any", axis=0)

# análise sobre os cancelamentos
print(tabela["Churn"].value_counts())  # qtd - sim; qtd - não
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format)) # percentual -> qtd - sim; qtd - não

# compara cada coluna da tabela com a coluna de cancelamento e gera um gráfico
import plotly.express as px
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn")
    grafico.show()