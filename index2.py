import Usuarios as us

name = input("Nome: ")
dataNasc = input("Data de nascimento: ").strip()
dd = dataNasc[0:2]
mm = dataNasc [3:5]
aaaa = dataNasc [6:10]

data_formatada = "/".join([dd,mm,aaaa])
qntFilhos = int(input("Qnt de filhos: "))

if (qntFilhos <0):
            raise Exception("Qnt de filhos não valido")

user01 = us.Usuario(name, data_formatada, qntFilhos)

# CHAMO OS MÉTODOS 
user01.CadastrarUsuario()
# user01.ListarUsuario()
user01.apresentar()

nomeBuscado = input("Qual nome você busca?").strip()
dadosEncontrados = user01.ListarUsuario(nomeBuscado)

print(dadosEncontrados)