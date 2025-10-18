# Class
class Usuarioss:
    def __init__(self, name, dtNasc, filhos):
        self.name = name
        self.dtNasc = dtNasc
        self.filhos = filhos
    def apresentar(self):
        print(f"Olá meu nome é {self.name} nasci em {self.dtNasc} e tenho {self.filhos} filhos" )   