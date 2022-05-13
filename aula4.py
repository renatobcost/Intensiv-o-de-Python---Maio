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
pyautogui.click(x=460, y=469) # posição do arquivo
pyautogui.click(x=1660, y=234) # posição do menu
pyautogui.click(x=1300, y=744) # posição do botão fazer download
time.sleep(5)

# lê o arquivo
import pandas as pd

tabela = pd.read_csv(r"C:\Users\Renato\Downloads\advertising.csv") 

# análise exploratória para compreender o comportamento da base de dados
import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(tabela.corr(), annot=True, cmap="Wistia")
plt.show()

# separa dados de treino e de testee
from sklearn.model_selection import train_test_split

y = tabela["Vendas"]
x = tabela.drop("Vendas", axis=1)

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=1)

# escolha do modelo de regressão que será utilizado
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# cria as inteligencias aritificiais
modelo_regressaolinear = LinearRegression()
modelo_arvoredecisao = RandomForestRegressor()

# treina as inteligencias artificias
modelo_regressaolinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)

# teste da IA e avaliação do melhor modelo#
from sklearn import metrics

# criar as previsoes
previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)

# comparar os modelos
print(metrics.r2_score(y_teste, previsao_regressaolinear))
print(metrics.r2_score(y_teste, previsao_arvoredecisao)) 

#visualização gráfica das previsões
tabela_auxiliar = pd.DataFrame()
tabela_auxiliar["y_teste"] = y_teste
tabela_auxiliar["Previsoes ArvoreDecisao"] = previsao_arvoredecisao
tabela_auxiliar["Previsoes Regressao Linear"] = previsao_regressaolinear

plt.figure(figsize=(15,6))
sns.lineplot(data=tabela_auxiliar)
plt.show()