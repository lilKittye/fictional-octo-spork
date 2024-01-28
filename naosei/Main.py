import tkinter
from tkinter import *
from CadastroPessoa import CadastroPessoas

cadastrar = CadastroPessoas()

def textoDigitado():
    nomeDigitado = ent_nome.get()
    idadeDigitada = ent_idade.get()
    cpfDigitado = ent_cpf.get()
    cadastrar.adicionarPessoas(nomeDigitado, idadeDigitada, cpfDigitado)


def salvarCadastros():
    with open('cadastros.txt', 'a') as cadastros:
        cadastros.write(f"\nNome: {ent_nome.get()} \nIdade: {ent_idade.get()} \nCPF: {ent_cpf.get()} ")
def apagarCadastros():
    with open('cadastros.txt', 'w') as cadastros:
        cadastros.write('')


def feedback():
    texto_feedback.set("Cadastro realizado com sucesso!")
    cadastro.config(state=tkinter.DISABLED)  # Desabilita o botão temporariamente
    janela.after(1000, limpar_feedback)  # Chama limpar_feedback após 2 segundos

def limpar_feedback():
    texto_feedback.set("")  # Limpa o texto de feedback
    cadastro.config(state=tkinter.NORMAL)  # Restaura o estado normal do botão


janela = Tk()
janela.title("Cadastro")
janela.geometry("400x300")

texto_feedback = tkinter.StringVar()
label_feedback = tkinter.Label(janela, textvariable=texto_feedback, justify=tkinter.LEFT, font=("Helvetica", 8, "bold"))
label_feedback.grid(column=1, row=7)


texto_nome = Label(janela,text="Nome: ", font=("8"), justify=tkinter.LEFT, highlightcolor=("black"))
texto_nome.grid(column=0,row=0)
null=Label(janela,text=" ")
null.grid(column=0,row=1)

texto_idade = Label(janela, text="Idade: ", font=("8"), justify=tkinter.LEFT, highlightcolor=("black"))
texto_idade.grid(column=0, row=2)

null1=Label(janela,text=" ")
null1.grid(column=0,row=3)

text_cpf = Label(janela, text="CPF: ",font=("8"),justify=tkinter.LEFT, highlightcolor=("black"))
text_cpf.grid(column=0, row=4)

null2=Label(janela,text=" ")
null2.grid(column=0,row=5)

ent_nome=tkinter.Entry(janela, font=5, justify=tkinter.LEFT)
ent_nome.grid(column=1,row=0)

null3=Label(janela,text=" ")
null3.grid(column=0,row=1)

ent_idade=tkinter.Entry(janela, font=5, justify=tkinter.LEFT)
ent_idade.grid(column=1,row=2)

null4=Label(janela,text=" ")
null4.grid(column=0,row=3)

ent_cpf=tkinter.Entry(janela, font=5, justify=tkinter.LEFT)
ent_cpf.grid(column=1,row=4)

null5=Label(janela,text=" ")
null5.grid(column=0,row=5)

cadastro = Button(janela, text="Cadastrar", command=textoDigitado)
cadastro.grid(column=2, row=6)
cadastro2 = Button(janela, text="Cadastrar", command=feedback)
cadastro2.grid(column=2, row=6)

salvarnoarquivo = Button(janela, text="Salvar no Arquivo", command=salvarCadastros)
salvarnoarquivo.grid(column=0, row=6)

apagarcadastros = Button(janela, text="Apagar Cadastros", command=cadastrar.apagarPessoas)
apagarcadastros.grid(column=1, row=6)
apagarcadastros = Button(janela, text="Apagar Cadastros", command=apagarCadastros)
apagarcadastros.grid(column=1, row=6)

janela.mainloop()