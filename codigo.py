import pyautogui
import time

pyautogui.PAUSE = 0.3
#pyautogui.write escrever texto
#pyautogui.press apertar uma tecla
#pyautogui.click clicar o botao do mouse
#pyautogui.hotkey apertar um atlho de teclado ex (ctrl+c)

#abrir navegador
pyautogui.press ("win")
pyautogui.write ("opera")
pyautogui.press ("enter")

#entar no site
pyautogui.write ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press ("enter")

#pausa segundos
time.sleep(1)

#fazer o login
pyautogui.click(x=1025, y=405)
pyautogui.write ("sannaclara65@gmail.com")
pyautogui.press ("tab")
pyautogui.write ("Clara555")
pyautogui.press ("tab")
pyautogui.press ("enter")

time.sleep(2)

#importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)
#cadastrar produto
pyautogui.click(x=881, y=291)

for linha in tabela.index:

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca= tabela.loc[linha,"marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo= tabela.loc[linha,"tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    categoria= tabela.loc[linha,"categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco= tabela.loc[linha,"preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    custo= tabela.loc[linha,"custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs= tabela.loc[linha,"obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.click(x=881, y=291)

    pyautogui.scroll(6000)

