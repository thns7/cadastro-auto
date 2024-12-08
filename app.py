import pyautogui as py
import pandas as pd
import time

py.PAUSE = 0.5

py.press("win")
py.write("chrome")
py.press("enter")
time.sleep(1)
py.write("https://www.sauer.pro.br/python/automacao/index.html")
py.press("enter")
time.sleep(4)
py.press("tab")
py.write("admin")
py.press("tab")
py.write("SimplificaPython")
py.press("enter")

tabela = pd.read_csv("alunos.csv")

time.sleep(5)

for linha in tabela.index:
    py.click(x=694, y=390)



    nome = tabela.loc[linha, "Nome"]
    py.write(str(nome))
    py.press("tab")

    email = tabela.loc[linha, "Email"]
    py.write(str(email))
    py.press("tab")

    endereco = tabela.loc[linha, "Endereco"]
    py.write(str(endereco))
    py.press("tab")

    telefone = tabela.loc[linha, "Telefone"]
    py.write(str(telefone))
    py.press("tab")
    py.press("enter")

    py.scroll(5000)