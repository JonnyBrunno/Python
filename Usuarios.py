class Usuario:    
    dic = {}
    def __init__(self, name, dtNasc, filhos): #CADASTRAR USUARIO
        self.name = name
        self.dtNasc = dtNasc
        self.filhos = filhos
        
      
    def apresentar(self):
        print(f"Olá meu nome é {self.name} nasci em {self.dtNasc} e tenho {self.filhos} filhos" )  

    def CadastrarUsuario(self):
        self.dic[self.name] = {"data_nasc":self.dtNasc, "qntFilhos": self.filhos}

    def ListarUsuario(self,name):
        try:
            nameEncontrado = self.dic[self.name]
        except ('KeyErro'):
            print("Nome não existente")
        else:
            return nameEncontrado
        finally:
            print("Operação concluída") 

