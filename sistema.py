class Sistema:
    def __init__(self, arq: str):
        self.__arq = textfile = open(arq, "w")    #arq é referente ao arquivo txt usado para persistência