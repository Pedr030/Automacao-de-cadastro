import pyautogui
import pandas as pd
import time

pyautogui.PAUSE = 0.4

#Abrir no navegador
pyautogui.press ("win")
pyautogui.write ("chrome")
pyautogui.press ("enter")

#Entrar no site 
time.sleep(1)
pyautogui.click (x=513, y=52)
pyautogui.write ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press ("enter")

#Fazer login no sistema
time.sleep(0.8)
pyautogui.click (x=679, y=363)
pyautogui.write ("P3drinh01456@gmail.com")
pyautogui.press ("tab")
pyautogui.write ("301022")
pyautogui.press ("tab")
pyautogui.press ("enter")
time.sleep (0.5)

#Importar base de dados
tabela = pd.read_csv("produtos.csv")

#cadastrar os produtos
for linha in tabela.index:
    pyautogui.click (x=715, y=255)
    pyautogui.write (str(tabela.loc[linha, "codigo"])) #pega o codigo da tabela e escreve no campo
    pyautogui.press ("tab") #passa para o proximo campo
    #REPETIR EM TODOS OS OUTROS
    pyautogui.write (str(tabela.loc[linha, "marca"]))
    pyautogui.press ("tab")
    pyautogui.write (str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write (str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write (str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write (str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs): #olha se tem informação no "obs", se n tiver deixa em branco
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.click (x=600, y=499)
    pyautogui.scroll(5000)
