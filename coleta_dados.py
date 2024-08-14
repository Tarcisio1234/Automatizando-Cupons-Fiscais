from tkinter import *
from tkinter import messagebox
import re
import pyautogui
import time
import random

#define o tamanho e a posição inicial na janela 1
def iniciarJanela2():
    janela = Tk()
    janela.title('Fazedor de cartões')



    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    largura_janela = 550
    altura_janela = 620
    x = (largura_tela - largura_janela) // 2
    y = (altura_tela - altura_janela) // 2

    janela.geometry(f'{largura_janela}x{altura_janela}+{x}+{y}')

    return janela

#extrai os valores do cartão já scaneado
def extrair_valores(texto):
    regex = r'[Rr]\$(\d+,\d{2})'
    valores = re.findall(regex, texto)
    return valores

def iniciarCodigo2(listaProduto, listaValor,dadosdoCartao):
    valor = extrair_valores(dadosdoCartao.get("1.0", "end-1c"))
    iniciarCodigo(listaProduto, listaValor,valor, dadosdoCartao.get("1.0", "end-1c"))
    # Limpar o campo de texto após a execução
    dadosdoCartao.delete("1.0", END)

#o codigo para poder realizar as operaçoes e controlar o teclado para o cupom fiscal
def iniciarCodigo(listaProduto, listaValor, parametro_Valor, dadosCartao):

    quantidadeItens = len(parametro_Valor)
    
    if quantidadeItens < 1:
        messagebox.showerror(title="Valor não encontrado", message="Não foi encontrado o valor da compra")
    else:
        extraindo = parametro_Valor[0]
        extraindo = str(extraindo)
        if "," in extraindo:
            extraindo = extraindo.replace(",", ".")

        valor3 = extraindo.replace(".", ",")


        itemEscolhido = random.choice(listaProduto)
        indexe = listaProduto.index(itemEscolhido)
        kg = float(extraindo) / float(listaValor[indexe])
        kg += 0.001
        kgForamtado = '{:.3f}'.format(kg)
        kgForamtado = str(kgForamtado)
        pyautogui.press('f2')
        kgForamtado = kgForamtado.replace('.', ',')
        time.sleep(1)
        pyautogui.write(f"{kgForamtado}*{itemEscolhido}", interval=0.2)
        pyautogui.press('enter')
        time.sleep(0.2)
        pyautogui.press('f3')
        time.sleep(0.2)
        pyautogui.press('f3')
        time.sleep(0.2)
        pyautogui.write(f"{valor3}", interval=0.4)
        time.sleep(0.2)
        pyautogui.press('enter')
        time.sleep(0.2)

        if "Pix" in dadosCartao:
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('enter')
            pyautogui.press('f3')
            pyautogui.press('f3')
        else:
            pyautogui.press('down')
            time.sleep(0.2)
            pyautogui.press('enter')
            time.sleep(0.2)
            pyautogui.press('enter')
            time.sleep(0.2)
            pyautogui.press('enter')
            time.sleep(0.2)
            pyautogui.press('enter')
            time.sleep(0.2)

            if "DEBITO" in dadosCartao or "Debito" in dadosCartao:
                pyautogui.press('down')
                pyautogui.press("enter")
            elif "Credito" in dadosCartao or "CREDITO" in dadosCartao:
                pyautogui.press("enter")
            else:
                pyautogui.press('enter')

            if "MASTERCARD" in dadosCartao or "maestro" in dadosCartao or "MAESTRO" in dadosCartao:
                pyautogui.write("MASTERCARD", interval=0.2)
                pyautogui.press("enter")
            elif "Visa" in dadosCartao or "visa" in dadosCartao or "VISA" in dadosCartao:
                pyautogui.write("VISA", interval=0.2)
                pyautogui.press("enter")
            elif "ELO" in dadosCartao or "ELD" in dadosCartao:
                pyautogui.write("ELO", interval=0.2)
                pyautogui.press("enter")
            elif "TICKET" in dadosCartao:
                pyautogui.write("TICKET ALIMENTACAO", interval=0.2)
                pyautogui.press("enter")
            elif "ALELO" in dadosCartao:
                pyautogui.write("ALELO", interval=0.2)
                pyautogui.press("enter")
            elif "AMEX" in dadosCartao:
                pyautogui.write("AMEX", interval=0.2)
                pyautogui.press("enter")
            elif "PLUXEE" in dadosCartao or "Pluxee" in dadosCartao:
                pyautogui.write("PLUXEE",interval=0.2)
                pyautogui.press("enter")
            else:
                messagebox.showerror(title="Bandeira do Cartão não encontrada", message="Não foi encontrada a bandeira do cartão")
                exit()

            if "PagBank" in dadosCartao or "pagbank" in dadosCartao:
                pyautogui.write("PAGBANK", interval=0.2)
                pyautogui.press("f3")
            elif "sipag" in dadosCartao or "sipAg" in dadosCartao or "Sipag" in dadosCartao or "SipAg" in dadosCartao:
                pyautogui.write("SIPAG")
                pyautogui.press("f3")
            else:
                messagebox.showerror(title="Maquininha não encontrada", message="Não foi encontrada Maquina de cartão")
                exit()


#toda a construção da janela 2 como foto e os textos
def segundaJanela(listaProduto, listaValor, janela1):
    janela1.destroy()
    janela2 = iniciarJanela2()
    janela2.configure(bg='CornflowerBlue')
    janela2.resizable(width=False, height=False)

    janela2.iconbitmap("imagens/teste.ico")

    textoExplicando = Label(janela2, text="Coloque os dados do cartão aqui", font=("Helvetica", 15))
    textoExplicando.place(x=96, y=14)
    textoExplicando.configure(background='CornflowerBlue')

    logo = PhotoImage(file="imagens/teste2.png")
    logo = logo.subsample(3, 3)
    figura1 = Label(image=logo, bg='CornflowerBlue')
    figura1.place(x=420, y=510)

    frame= Frame(janela2, borderwidth=0, relief="solid",background='Gold')
    frame.place(x=12, y=52, width=524, height=437)

    dadosdoCartao = Text(janela2, font=("Helvetica", 12))
    dadosdoCartao.place(x=15, y=55, width=517, height=430)

    botao1 = Button(janela2, text="Iniciar", command=lambda: iniciarCodigo2(listaProduto, listaValor ,dadosdoCartao), background="SpringGreen",font=("Helvetica", 13))
    botao1.place(x=15, y=530, width=140, height=50)

    botao2 = Button(janela2, text="Voltar", command=lambda: primeiroCodigo(janela2), background="Salmon",font=("Helvetica", 13))
    botao2.place(x=200, y=530, width=140, height=50)

    janela2.mainloop()

#define o tamanho e a posição inicial na janela 1
def iniciarJanela():
    janela = Tk()
    janela.title('Fazedor de cartões')

    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    largura_janela = 350
    altura_janela = 470
    x = (largura_tela - largura_janela) // 2
    y = (altura_tela - altura_janela) // 2

    janela.geometry(f'{largura_janela}x{altura_janela}+{x}+{y}')
    janela.resizable(width=False, height=False)

    return janela


#função que adiciona os itens nas listas para poder ser usadas mais tardas como o codigo do produto e o valor
def addItens(iten, valor, listaProdutosMain, listaPrecoMain):
    item_cod = str(iten.get("1.0", "end-1c").strip())
    item_val = str(valor.get("1.0", "end-1c").strip())  

    if item_cod and item_val:  
        if "," in item_val:
            item_val = item_val.replace(',','.')
            listaProdutosMain.append(item_cod)
            listaPrecoMain.append(item_val)
            iten.delete("1.0", "end")
            valor.delete("1.0", "end")
            
    else:
        print("Por favor, preencha ambos os campos.")


#essa função distroi a tela ficticia e prepara todo a tela de add os produtos como as fotos e tudo mais
def primeiroCodigo(janela2):
    janela2.destroy()
    janela1 = iniciarJanela()
    janela1.title("Adicionando itens")
    janela1.config(bg='CornflowerBlue')

    titulo = Label(janela1, text="Cadastrando os produtos", font=('Helvetica', 14))
    titulo.config(bg='CornflowerBlue')
    titulo.place(x=43, y=8)

    titulo2 = Label(janela1, text="Adicione o código do produto:", font=('Helvetica', 12))
    titulo2.config(bg='CornflowerBlue')
    titulo2.place(x=35, y=60)

    produtoCod = Text(janela1, font=('Helvetica', 11))
    produtoCod.place(x=36, y=90, width=95, height=25)

    titulo3 = Label(janela1, text="Adicione o valor do produto:", font=('Helvetica', 12))
    titulo3.config(bg='CornflowerBlue')
    titulo3.place(x=35, y=135)

    valorProduto = Text(janela1, font=('Helvetica', 11))
    valorProduto.place(x=36, y=165, width=95, height=25)

    frame1= Frame(janela1, borderwidth=0, relief="solid",background='Gold')
    frame1.place(x=97, y=282, width=156, height=46)

    logo1 = PhotoImage(file="imagens/maquina.png")
    logo1 = logo1.subsample(6, 6)
    figura3 = Label(image=logo1, bg='CornflowerBlue')
    figura3.place(x=255, y=370)


    logo2 = PhotoImage(file="imagens/teste2.png")
    logo2 = logo2.subsample(5, 5)
    figura4 = Label(image=logo2, bg='CornflowerBlue')
    figura4.place(x=20, y=215)
    # Inicializa as listas de produtos e valores'''
    listaProduto = []
    listaValor = []

    botao1 = Button(janela1, text="Adicionar", command=lambda: addItens(produtoCod, valorProduto, listaProduto, listaValor))
    botao1.place(x=100, y=285, width=150, height=40)

    botao1 = Button(janela1, text="Iniciar", command=lambda: segundaJanela(listaProduto, listaValor,janela1), background="SpringGreen")
    botao1.place(x=100, y=355, width=150, height=40)

    janela1.mainloop()


# incio do código na qual inicia com uma tela vazia como argumento
#o motivo disso vai ser visto mais tarde
n= Tk()
primeiroCodigo(n)

