import pyautogui
import time

pyautogui.PAUSE = 0.5

# pyautogui.click clicar
# pyautogui.press pressionar tecla 
# pyautogui.write escrever
# pyautogui.hotkey tecla de atalho
# Sistema Python PowerUp https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.press("win")

# digitar o texto chrome
pyautogui.write("chrome")

# apertar enter
pyautogui.press("enter")

# entar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

# apertar enter
pyautogui.press("enter")

# esperar o site carregar
time.sleep(3)

# fazer login
# seleciona o 1 campo
# pyautogui.click(x=1,y=1)
pyautogui.write("noreply@google.com")

# passa para o campo senha 
pyautogui.press("tab")
pyautogui.write("senha super dificil")

# passa para o botão de logar
pyautogui.press("tab")
pyautogui.press("enter")

# impirtar a base de dados 
import pandas

tabela = pandas.read_csv("produtos.csv")

# esperar o site carregar
time.sleep(2)

# cadastra o produto


for linha in tabela.index:
    
    # seleciona o 1 campo
    # pyautogui.click(x=1,y=1)

    # CODIGO
    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # MARCA
    marca = tabela.loc[linha,"codigo"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # TIPO
    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # CATEGORIA
    categoria = tabela.loc[linha,"categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preco_unitario
    preco_unitario = tabela.loc[linha,"preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    # custo
    custo = tabela.loc[linha,"custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs
    obs = str(tabela.loc[linha,"obs"])

    # prenche o obs se não for nan
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    # apertar botão de enviar
    pyautogui.press("enter")

    # numero positivo igual a scroll pra cima
    # numero negativo igual a scroll pra baixo
    pyautogui.scroll(10000)