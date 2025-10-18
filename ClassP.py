class Pacientes:    
    dic = {}
    def __init__(self, nome, CPF, idade, medico, quarto, acompanhante, restrições):
   
        self.nome = nome
        self.CPF = CPF
        self.idade = idade
        self.medico =medico
        self.quarto = quarto
        self.acompanhante = acompanhante 
        self.restrições = restrições

    def CadastrarUsuario(self):
        self.dic[self.CPF] = {"Nome":self.nome, "Idade":self.idade, "Medico":self.medico, "Quarto":self.acompanhante, "Restrições":self.restrições}

    def ListarUsuario(self,CPF):
        try:
            nameEncontrado = self.dic[self.CPF]
        except ('KeyErro'):
            print("Paciente não encontrado")
        else:
            return nameEncontrado
        finally:
            print("Operação concluída")
        
class Medicos:
    pass 