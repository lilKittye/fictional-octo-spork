import time
import tkinter
from tkinter import *
from PIL import Image, ImageTk


class Hora:

    def __init__(self):
        atual_hora = time.localtime()
        self.hora_atual = atual_hora.tm_hour
        self.minuto_atual = atual_hora.tm_min

    def hora_atual(self, nova_hora):
        self.hora_atual = nova_hora.get(self.hora_atual)

    def mostra_hora(self):
        return f"Hora: {self.hora_atual}:{self.minuto_atual}"


def feedbackola():
    #botão oi

    if(horaatual.hora_atual > 12 and horaatual.hora_atual < 18 ):
        feedbackoi.set("Olá, boa tarde!")

    elif (horaatual.hora_atual >= 18 ):
        feedbackoi.set("Olá, boa noite!")

    elif (horaatual.hora_atual > 6):
        feedbackoi.set("Olá, bom dia!")

    oi.config(state=tkinter.DISABLED)
    janela.after(1000, limpar_feedbackoi)
def limpar_feedbackoi():
    feedbackoi.set("")  # Limpa o texto de feedback
    oi.config(state=tkinter.NORMAL)  # Restaura o estado normal do botão

def feedbackTEMPO(): #botao hora
    feedbackTIME.set(horaatual.mostra_hora())
    oi.config(state=tkinter.DISABLED)
    janela.after(4000, limpar_feedbackTEMPO)
def limpar_feedbackTEMPO():
    feedbackTIME.set("")  # Limpa o texto de feedback
    oi.config(state=tkinter.NORMAL)  # Restaura o estado normal do botão

horaatual=Hora()

janela=Tk()
janela.title("Robozinho do Dia")
#janela.geometry("400x350")


feedbackoi = tkinter.StringVar()
label_feedbackola = tkinter.Label(janela, textvariable=feedbackoi, justify=tkinter.CENTER, font=("Helvetica", 8, "bold"))
label_feedbackola.grid(column=1, row=7)

feedbackTIME = tkinter.StringVar()
label_feedbackTIME = tkinter.Label(janela, textvariable=feedbackTIME, justify=tkinter.CENTER, font=("Helvetica", 8, "bold"))
label_feedbackTIME.grid(column=2, row=2)

oi=Button(janela,text="Oi", font=("Arial",9,"bold"), command=feedbackola)
oi.grid(row=1,column=1)

null=Label(janela,text=" ")
null.grid(row=1, column=2)

horaagora=Button(janela,text="Hora?", font=("Arial",9,"bold"), command=feedbackTEMPO)
horaagora.grid(row=1,column=3)

horaatual.mostra_hora()

janela.mainloop()
