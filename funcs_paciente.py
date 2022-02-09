from paciente_classe import paciente
from tkinter.messagebox import showinfo


def criar_txt():
    #Função que cria o arquivo de texto "dados_pacientes.txt" caso ele não exista
    textfile = open("dados_pacientes.txt", "w") #ao chamar open("xyz","w"), o arquivo será criado caso ele não exista 
    textfile.close()

def ler_dados(lista_pacientes):
    #Função que recupera dados salvos no arquivo txt

    textfile = open("dados_pacientes.txt", "r")
    list_data = textfile.readlines()

    for x in list_data:
        lista_pacientes.append(0)

        tuple_dados_paciente = x.strip("'\n").split(", ") # Preparando os dados do arquivo de texto

        #criando um objeto com os atributos estabelecidos no arquivo de texto:
        lista_pacientes[len(lista_pacientes)-1] = paciente(tuple_dados_paciente[0],tuple_dados_paciente[2],tuple_dados_paciente[3])

        #colocando a data_entrada registrasda no arquivo:
        lista_pacientes[len(lista_pacientes)-1].data_entrada = tuple_dados_paciente[1]

        #colocando a data_saida registrada no arquivo, caso presente:
        if len(tuple_dados_paciente) == 5:
            lista_pacientes[len(lista_pacientes)-1].data_saida = tuple_dados_paciente[4]

def salvar_dados(lista_pacientes):
    #Função que salva os dados dos pacientes para um arquivo de texto

    textfile = open("dados_pacientes.txt", "w")
    for element in lista_pacientes:
        if hasattr(element,'data_saida') == True:
            print(f"{element.nome}, {element.data_entrada}, {element.ala}, {element.estado}, {element.data_saida}", file=textfile)
        else:
            print(f"{element.nome}, {element.data_entrada}, {element.ala}, {element.estado}", file = textfile)
    textfile.close()


def apagar_dados(lista_pacientes):
    #limpa todos os registros no arquivo de texto e na lista que contém os pacientes
    f = open("dados_pacientes.txt", 'r+')
    f.truncate(0) # limpando o arquivo de texto
    lista_pacientes.clear() # limpando a lista usada para armazenar os dados dos pacientes


def novo_paciente(nome, ala, estado, lista_pacientes):
    #Função que adiciona um novo paciente ao sistema

    lista_pacientes.append(0)
    lista_pacientes[len(lista_pacientes)-1] = paciente(nome, ala, estado)


def procurar_paciente(pac_cod, lista_pacientes):
    #Procurar um paciente em específico na database
    if 0 < int(pac_cod) <= len(lista_pacientes):
        return(f"Código: {pac_cod}, paciente: {lista_pacientes[int(pac_cod)-1].nome}, entrada: {lista_pacientes[int(pac_cod)-1].data_entrada}, ala: {lista_pacientes[int(pac_cod)-1].ala}, estado: {lista_pacientes[int(pac_cod)-1].estado}")
    else:
        return("Paciente não encontrado")

def alterar_dado(cod_paciente, dado_a_alterar, alterar_para, lista_pacientes):
    #alterar dado de um paciente

    if 0 < int(cod_paciente) <= len(lista_pacientes):
        lista_pacientes[int(cod_paciente)-1].alterar_paciente(dado_a_alterar, alterar_para)
    else:
        showinfo(title="", message="Paciente não encontrado")


def dar_alta(cod_paciente, lista_pacientes):
    #Dar alta a um paciente e registrar seu horário de saída

    if 0 < int(cod_paciente) <= len(lista_pacientes):
        lista_pacientes[int(cod_paciente)-1].dar_alta()
    else:
        showinfo(title="", message="Paciente não encontrado")


def mostrar_todos_pacientes(lista_pacientes):
    mostrar_lista = []
    #Função que mostra uma lista com todos os pacientes registrados:
    for element in lista_pacientes:
        if hasattr(element, 'data_saida') == True:   # Caso data_saida exista:
            mostrar_lista.append(f"Código: {lista_pacientes.index(element)+1}, paciente: {element.nome}, entrada: {element.data_entrada}, ala: {element.ala}, estado: {element.estado}, saída: {element.data_saida}\n\n")
        else:   # Caso data_saida não exista:
            mostrar_lista.append(f"Código: {lista_pacientes.index(element)+1}, paciente: {element.nome}, entrada: {element.data_entrada}, ala: {element.ala}, estado: {element.estado}\n\n")
    return(''.join(mostrar_lista)) # Juntando as diversas strings que compõem mostrar_lista para que elas possam ser exibidas em uma textbox do TKinter