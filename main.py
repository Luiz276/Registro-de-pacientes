import tkinter as tk
from tkinter import Scrollbar, font as tkfont
from tkinter.constants import BOTH, RIGHT, VERTICAL
from funcs_paciente import *    #Funções que processam os dados
from tkinter.messagebox import showinfo

#Listas necessárias para rodar o backend:
lista_pacientes = []    #Armazena os objetos criados com a classe paciente
list_data = []          #Auxilia na leitura do arquivo de texto usado para salvar

#------
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry("900x600")
        self.title("PRP")

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # o container é onde os frames são colocados um em cima do outro
        # quando um frame especifico é chamado, ele é colocado no topo

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, NovoPac, ProcurarPac, AlterarDado, DarAlta, ListaPac):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # colocar todas as páginas no mesmo lugar
            # a página no topo é a que está visível
            
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")
    #função showframe, pertencente a clase SampleApp
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
    

class StartPage(tk.Frame):
    #primeira tela a ser mostrada na aplicação
    def __init__(self, parent, controller):
        #------
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #Título da aplicação:
        label_topo = tk.Label(self, text="PRP - Programa de Registro de Paciente", font=controller.title_font)

        #Subtítulo:
        label_sub = tk.Label(self, text="Não se esqueça de salvar!")

        #Botões:
        button0 = tk.Button(self, text = "Salvar dados", width=40,
                            command=lambda: salvar_dados(lista_pacientes))
        button1 = tk.Button(self, text="Novo paciente", width=40,
                            command=lambda: controller.show_frame("NovoPac"))
        button2 = tk.Button(self, text="Procurar por paciente registrado", width=40,
                            command=lambda: controller.show_frame("ProcurarPac"))
        button3 = tk.Button(self, text="Alterar dado de um paciente", width=40,
                            command=lambda: controller.show_frame("AlterarDado"))
        button4 = tk.Button(self, text="Dar alta", width=40,
                            command=lambda: controller.show_frame("DarAlta"))
        button5 = tk.Button(self, text="Lista com todos os pacientes", width=40,
                            command=lambda: controller.show_frame("ListaPac"))
        button6 = tk.Button(self, text = "Apagar todos os dados", width=40,
                            command=lambda: apagar_dados(lista_pacientes))

        #posicionando os elementos:
        label_topo.pack(side="top", fill="x", pady=10)
        label_sub.pack(side="top", fill="x", pady=10)
        button0.pack()
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()
        button6.pack()


class NovoPac(tk.Frame):
    #Tela para registrar novo paciente
    def __init__(self, parent, controller):
        #declarando as variáveis usadas:
        nome_var = tk.StringVar()
        ala_var = tk.StringVar()
        estado_var = tk.StringVar()

        #Convertendo de StringVar para string normal
        nome_var.set('')
        ala_var.set('')
        estado_var.set('')

        #------
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #texto no topo:
        label_NovoPac = tk.Label(self, text="Adicionar paciente", font=controller.title_font) #titulo da pagina

        #campos de texto:
        nome_label = tk.Label(self, text = "Nome:", font = ('calibre',10, 'bold'))
        ala_label = tk.Label(self, text = "Ala hospitalar:", font = ('calibre',10, 'bold'))
        estado_label = tk.Label(self, text = "Estado:", font = ('calibre',10, 'bold'))

        nome_entry = tk.Entry(self, textvariable = nome_var, font = ('calibre',10, 'bold'))
        ala_entry = tk.Entry(self, textvariable = ala_var,  font = ('calibre',10, 'bold'))
        estado_entry = tk.Entry(self, textvariable = estado_var,  font = ('calibre',10, 'bold'))

        #botão de finalizar:
        button_add = tk.Button(self, text="Adicionar",
                           command=lambda: novo_paciente(nome_var.get(), ala_var.get(), estado_var.get(), lista_pacientes)) #mudar
        button_end = tk.Button(self, text="Finalizar",
                           command=lambda: controller.show_frame("StartPage"))
        
        #posicionando tudo:
        label_NovoPac.grid(row=0,column=0) # titulo da pagina
        nome_label.grid(row=1,column=0)
        nome_entry.grid(row=1,column=1)
        ala_label.grid(row=2,column=0)
        ala_entry.grid(row=2,column=1)
        estado_label.grid(row=3,column=0)
        estado_entry.grid(row=3,column=1)
        button_add.grid(row=4, column=1) # botão de adicionar
        button_end.grid(row=5, column=0)


class ProcurarPac(tk.Frame):
    #tela para procurar por um paciente em específico
    def __init__(self, parent, controller):
        #declaração de variável:
        cod_var = tk.StringVar()

        #Convertendo de StringVar para string normal
        cod_var.set('')

        #------
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #Texto no topo:
        label_ProcurarPac = tk.Label(self, text="Procurar paciente", font=controller.title_font)
        
        #Label e campo de entrada do código:
        cod_label = tk.Label(self, text = "Código do paciente:", font = ('calibre',10, 'bold'))
        cod_entry = tk.Entry(self, textvariable = cod_var, font = ('calibre',10, 'bold'))

        #Botões:
        button_busca = tk.Button(self, text="Buscar",
                           command=lambda: showinfo(title="", message=str(procurar_paciente(cod_var.get(), lista_pacientes))))
        button_end = tk.Button(self, text="Finalizar",
                           command=lambda: controller.show_frame("StartPage"))
        
        #posicionando tudo:
        label_ProcurarPac.grid(row=0,column=0)
        cod_label.grid(row=1, column=0)
        cod_entry.grid(row=1, column=1)
        button_busca.grid(row=2, column=1)
        button_end.grid(row=4,column=0)


class AlterarDado(tk.Frame):
    #Tela para alterar dados de um paciente
    def __init__(self, parent, controller):
        #Declarando variáveis:
        cod_var = tk.StringVar()
        campo_var = tk.StringVar()
        dado_var = tk.StringVar()

        #Convertendo de StringVar para string normal
        cod_var.set('')
        campo_var.set('')
        dado_var.set('')

        #------
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #Texto no topo:
        label_AlterarDado = tk.Label(self, text="Alterar dado", font=controller.title_font)

        #Label e campo de entrada:
        cod_label = tk.Label(self, text = "Código do paciente:", font = ('calibre',10, 'bold'))
        cod_entry = tk.Entry(self, textvariable = cod_var, font = ('calibre',10, 'bold'))
        campo_label = tk.Label(self, text = "Campo a alterar:", font = ('calibre',10, 'bold'))
        campo_entry = tk.Entry(self, textvariable = campo_var, font = ('calibre',10, 'bold'))
        label_aviso = tk.Label(self, text = "nome - ala - entrada", font = ('calibre',10, 'bold'))
        dado_label = tk.Label(self, text = "Alterar para:", font = ('calibre',10, 'bold'))
        dado_entry = tk.Entry(self, textvariable = dado_var, font = ('calibre',10, 'bold'))

        #Botões:
        button_alterar = tk.Button(self, text="Alterar",
                           command=lambda: alterar_dado(cod_var.get(), campo_var.get(), dado_var.get(), lista_pacientes))
        button_end = tk.Button(self, text="Finalizar",
                           command=lambda: controller.show_frame("StartPage"))
        
        #Posicionando tudo:
        label_AlterarDado.grid(row=0, column=0)
        cod_label.grid(row=1, column=0)
        cod_entry.grid(row=1, column=1)
        campo_label.grid(row=2, column=0)
        campo_entry.grid(row=2, column=1)
        label_aviso.grid(row=2, column=2)
        dado_label.grid(row=3,column=0)
        dado_entry.grid(row=3, column=1)
        button_alterar.grid(row=4, column=1)
        button_end.grid(row=5,column=0)


class DarAlta(tk.Frame):
    #Tela para dar alta a um paciente
    def __init__(self, parent, controller):
        #Declarando variáveis:
        cod_var = tk.StringVar()

        #Convertendo de StringVar para string normal
        cod_var.set('')

        #------
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #Texto do topo:
        label_DarAlta = tk.Label(self, text="Alta", font=controller.title_font)

        #Labels e entradas de texto:
        cod_label = tk.Label(self, text = "Código do paciente:", font = ('calibre',10, 'bold'))
        cod_entry = tk.Entry(self, textvariable = cod_var, font = ('calibre',10, 'bold')) 
        #Botões:
        button_alta = tk.Button(self, text = "Dar alta",
                           command=lambda: dar_alta(cod_var.get(), lista_pacientes))
        button_end = tk.Button(self, text="Finalizar",
                           command=lambda: controller.show_frame("StartPage"))
        
        #Posicionando tudo:
        label_DarAlta.grid(row=0, column=0)
        cod_label.grid(row=1, column=0)
        cod_entry.grid(row=1, column=1)
        button_alta.grid(row=2, column =1)
        button_end.grid(row= 3, column= 0)


class ListaPac(tk.Frame):
    #Exibe uma lista contendo todos os pacientes registrados
    def __init__(self, parent, controller):
        #declarando variaveis:

        #------
        tk.Frame.__init__(self, parent)
        self.controller = controller

        pacientes_relacao = mostrar_todos_pacientes(lista_pacientes)

        def change_textbox():
            caixaTexto.delete("1.0","end")
            caixaTexto.insert("end", mostrar_todos_pacientes(lista_pacientes))

        #Texto no topo:
        label = tk.Label(self, text="Lista de pacientes", font=controller.title_font)

        #Caixa de texto que contém a lista:
        caixaTexto = tk.Text(self, height=25, width=100)

        #Scrollbar da caixa de texto:
        sb = Scrollbar(self, orient=VERTICAL)

        #Botões:
        button_end = tk.Button(self, text="Retornar",
                            command=lambda: controller.show_frame("StartPage"))
        button_refresh = tk.Button(self, text="Atualizar lista",
                            command=lambda: change_textbox())
        
        #Posicionando tudo:
        label.pack(side="top", fill="x", pady=10)
        caixaTexto.pack()
        sb.pack(side=RIGHT, fill=BOTH)
        button_refresh.pack()
        button_end.pack()

        #Configurando a textbox:
        caixaTexto.config(state='normal', yscrollcommand=sb.set)
        sb.config(command=caixaTexto.yview)
        caixaTexto.insert("end", pacientes_relacao)
        

#Mainloop responsável por fazer toda a aplicação funcionar
if __name__ == "__main__":
    ler_dados(lista_pacientes)
    app = SampleApp()
    app.mainloop()