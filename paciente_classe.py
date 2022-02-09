from datetime import datetime

class paciente:
    #classe que define os parâmetros de um paciente registrado no sistema
    
    def __init__(self, nome, ala, estado):
        #inicializando
        self.nome = nome
        self.data_entrada = (datetime.now()).strftime("%d/%m/%Y %H:%M")
        self.ala = ala
        self.estado = estado
    
    def exibir_dados(self):
        #printa todos os dados do paciente especificado
        print(f"Paciente: {self.nome}, entrada: {self.data_entrada}, ala: {self.ala}, estado: {self.estado}", end = "")

        if hasattr(self,'data_saida') == True:
            print(f", saída: {self.data_saida}")
        else:
            print("")

    def return_dados(self):
        #retorna todos os dados de um paciente em específico
        if hasattr(self,'data_saida') == True:
            return(f"Paciente: {self.nome}, entrada: {self.data_entrada}, ala: {self.ala}, estado: {self.estado}, saída: {self.data_saida}")
        else:
            return("Paciente: {self.nome}, entrada: {self.data_entrada}, ala: {self.ala}, estado: {self.estado}")
    
    def dar_alta(self):
        #Muda o estado de um paciente para alta e salva o horário de saída
        self.estado = "alta"
        self.data_saida = (datetime.now()).strftime("%D %H:%M")

    def alterar_paciente(self, dado, dado_alt):
        #Altera algum dado de um paciente
        if dado == "nome":
            self.nome = dado_alt
        elif dado == "ala":
            self.ala = dado_alt
        elif dado == "estado":
            self.estado = dado_alt
        else:
            print("campo não encontrado")