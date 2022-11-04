import datetime

class Paciente:
    def __init__(self, nome: str, ala: str, estado: str):
        self.__nome = nome
        self.__ala = ala
        self.__estado = estado
        self.__data_entrada = (datetime.now()).strftime("%d/%m/%Y %H:%M")
    
    @property
    def getEstado(self) -> str:
        return self.__estado
    
    @property
    def getNome(self) -> str:
        return self.__nome
    
    @property
    def getAla(self) -> str:
        return self.__ala
    
    @property
    def getDataEntrada(self) -> str:
        return self.__data_entrada
    
    @nome.setter
    def setNome(self, nome):
        self.__nome = nome
    
    @ala.setter
    def setAla(self, ala):
        self.__ala = ala
    
    @estado.setter
    def setEstado(self, estado):
        self.__estado = estado
    
    @data_entrada.setter
    def setDataEntrada(self, data_entrada):
        self.__data_entrada = data_entrada

    def return_dados(self) -> str:
        #retorna todos os dados de um paciente em específico
        return(f"Paciente: {self.getEstado()}, entrada: {self.getDataEntrada()}, ala: {self.getAla()}, estado: {self.getEstado()}")
