import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1 

# abre o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# procura a base de dados
pyperclip.copy("https://drive.google.com/drive/folders/1Ewh4n724sf7SKNLoU4XxQ5o7abe5p4dT?usp=sharing")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(5)

# faz o download do arquivo
pyautogui.click(x=1316, y=467) # posição do arquivo
pyautogui.click(x=1661, y=234) # posição do menu
pyautogui.click(x=1309, y=744) # posição do botão fazer download
time.sleep(5)

# lê o arquivo
import pandas as pd
tabela = pd.read_csv(r"C:\Users\Renato\Downloads\telecom_users.csv")
tabela = tabela.drop("Unnamed: 0", axis=1) # remove coluna unnamed:0
time.sleep(1)

# print(tabela.info())
# ajuste de valores
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")
time.sleep(1)

# deletando as colunas vazias
tabela = tabela.dropna(how="all", axis=1)
time.sleep(1)
# deletando as linhas vazias
tabela = tabela.dropna(how="any", axis=0)
time.sleep(1)

# análise sobre os cancelamentos
print(tabela["Churn"].value_counts())  # qtd - sim; qtd - não
time.sleep(1)
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format)) # percentual -> qtd - sim; qtd - não
time.sleep(1)

# compara cada coluna da tabela com a coluna de cancelamento e gera um gráfico
import plotly.express as px
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn")
    grafico.show()