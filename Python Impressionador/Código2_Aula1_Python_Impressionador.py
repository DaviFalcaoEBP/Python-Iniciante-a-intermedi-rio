import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.75

def abrir_navegador():
    pyautogui.press("win")
    pyautogui.write("Microsoft Edge")
    pyautogui.press("enter")

def entrar_no_site(link):
    pyautogui.write(link)
    pyautogui.press("enter")
    time.sleep(3)

def fazer_login(email, senha):
    pyautogui.click(x=204, y=309)
    pyautogui.write(email)
    pyautogui.press("tab")
    pyautogui.write(senha)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(3)

def importar_base_dados(caminho_arquivo):
    tabela = pd.read_csv(caminho_arquivo)
    print(tabela)
    return tabela

def cadastrar_produto(codigo, marca, tipo, categoria, preco, custo_unitario, obs):
    pyautogui.click(x=380, y=222)

    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    pyautogui.write(str(marca))
    pyautogui.press("tab")

    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    pyautogui.write(str(preco))
    pyautogui.press("tab")

    pyautogui.write(str(custo_unitario))
    pyautogui.press("tab")

    if not pd.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(5000)

def main():
    link_empresa = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
    email_usuario = "python.impressionador@gmail.com"
    senha_usuario = "sua_senha_aqui"
    caminho_arquivo_csv = 'C:\\Users\Davi Falcão\\Downloads\\produtos.csv'

    abrir_navegador()
    entrar_no_site(link_empresa)
    fazer_login(email_usuario, senha_usuario)

    tabela_produtos = importar_base_dados(caminho_arquivo_csv)

    for linha in tabela_produtos.index:
        produto_info = tabela_produtos.loc[linha]
        cadastrar_produto(*produto_info)

if __name__ == "__main__":
    main()