## 🐍 Intensivão de python 🐍

Projeto para estudo sobre [Python](https://www.python.org). O material disponível neste repositório foi desenvolvido durante o curso Intensivão de Python, disponibilizado pela [HashTag Programação](https://www.youtube.com/c/HashtagProgramação).

O objetivo deste projeto é compreender um pouco mais sobre o funcionamento do python aplicado a uso cotidiano. Ao total, foram 4 aulas que abordaram conceitos de manipulação e análise de dados, automação de comandos, criação de gráficos, web scraping, ..., entre outros conteúdos.
Segue a relação das aulas e seus conteúdos.


### 💡 Conceitos abordados
-----------------------
- Aula 1: Automação de Sistemas e Processos com Python
    - Desafio: Todos os dias, o sistema atualiza as vendas do dia anterior. O trabalho diário, como analista, é enviar um e-mail para a diretoria com o faturamento e a quantidade de produtos vendidos no dia anterior. Para resolver isso, foi utilizado o pyautogui, uma biblioteca de automação de comandos do mouse e do teclado;
- Aula 2: Análise de Dados com Python
    - Desafio: Você trabalha em uma empresa de telecom e tem clientes de vários serviços diferentes, entre os principais: internet e telefone. O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a empresa está com Churn de mais de 26% dos clientes. Isso representa uma perda de milhões para a empresa. O que a empresa precisa fazer para resolver isso? Para resolver isso, foi utilizado o pandas (uma biblioteca para manipulação e anáçlise de dados) e o plotly (uma biblioteca para visualização de dados).
- Aula 3: Automação Web e Busca de Informações com Python
    - Desafio: Você trabalha em uma importadora e o preço dos produtos é vinculado a cotação de: Dólar, Euro e Ouro. É necessário pegar na internet, de forma automática, a cotação desses 3 itens e saber quanto cobrar pelos produtos, considerando uma margem de contribuição que há na base de dados. Para resolver isso, foi utilizado uma automação web com o selenium.
- Aula 4: Projeto Ciência de Dados - Previsão de Vendas
    - O desafio é conseguir prever as vendas em determinado período com base nos gastos em anúncios nas 3 grandes redes que a empresa Hashtag investe: TV, Jornal e Rádio. Para resolver isso, foi utilizado o pandas (uma biblioteca para manipulação e anáçlise de dados), o matplotlib (uma biblioteca para visualização de dados) e o sklearn (uma biblioteca de aprendizado de máquina para obter predições do modelo)


### ⚠️ Instalação e uso do projeto
-----------------------
- Instale o [Python](https://www.python.org);
- Para instalar as bibliotecas que foram utilizadas execute os seguintes comandos:
    - `pip install pyautogui`
    - `pip install pyperclip`
    - `pip install pandas`
    - `pip install plotly`
    - `pip install matplotlib`
    - `pip install sklearn`
    - `pip install seaborn`


### ⚙️ Arquitetura do projeto
-----------------------

```
intesivao-python/
  ├─  base-de-dados/
  │        ├── advertising.csv   
  │        ├── novos.csv 
  │        ├── produtos.xls 
  │        ├── telecom_users.csv 
  │        └── vendas-dez.xls 
  │
  ├── aula1.py
  ├── aula2.py
  ├── aula3.py
  ├── aula4.py
  └── README.md
```

