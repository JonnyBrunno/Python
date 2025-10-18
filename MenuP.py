import ClassP as Pc

name = input("Nome: ") 

age = input("Data de nascimento: ").strip()
dd = age [0:2]
mm = age [3:5]
aaaa = age [6:10]

data_formatada =  "/".join([dd,mm,aaaa])

room = int(input("Digite o número do quarto: "))