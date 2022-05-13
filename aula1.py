import pyautogui
import pyperclip
import pandas as pd
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
pyautogui.click(x=1590, y=457) # posição do arquivo
pyautogui.click(x=1660, y=234) # posição do menu
pyautogui.click(x=1300, y=744) # posição do botão fazer download
time.sleep(5)

# lê o arquivo
tabela = pd.read_excel(r"C:\Users\Renato\Downloads\Vendas - Dez.xlsx")
faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()

# acessa o email
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(5)

# envia o email
pyautogui.click(x=140, y=252) # posição do botão Escrever
time.sleep(2)

pyautogui.write("britocostarenato@gmail.com")
pyautogui.press("tab") #seleciona destinatário
pyautogui.press("tab") # pula pro campo de assunto
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v") # escreve o assunto
pyautogui.press("tab") #pula pro corpo do email

texto = f"""
Prezados, bom dia

O faturamento de ontem foi de: R${faturamento:,.2f}
A quantidade de produtos foi de: {quantidade:,}

At.te."""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

# aperta Ctrl Enter para enviar o email
pyautogui.hotkey("ctrl", "enter")