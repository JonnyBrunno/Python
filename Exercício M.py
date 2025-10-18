# Lista para armazenar pacientes
pacientes = []

# Função para cadastrar um paciente
def cadastrar_paciente():
    print("\n--- Cadastro de Paciente ---")
    nome = input("Nome do paciente: ")
    idade = input("Idade do paciente: ")
    medico = input("Nome do médico responsável: ")
    quarto = input("Número do quarto: ")
    acompanhante = input("Nome do acompanhante: ")
    restrições = input("Restrições (se houver): ")

    paciente = {
        "nome": nome,
        "idade": idade,
        "medico": medico,
        "quarto": quarto,
        "acompanhante": acompanhante,
        "restrições": restrições,
    }

    pacientes.append(paciente)
    print(f"\n Paciente '{nome}' cadastrado com sucesso!\n")

# Função para listar os pacientes
def listar_pacientes():
    print("\n--- Lista de Pacientes ---")
    if not pacientes:
        print(" Nenhum paciente cadastrado.\n")
        return

    for i, paciente in enumerate(pacientes, start=1):
        print(f"{i}. Nome: {paciente['nome']}")
        print(f"   Idade: {paciente['idade']}")
        print(f"   Médico: {paciente['medico']}")
        print(f"   Quarto: {paciente['quarto']}")
        print(f"   Acompanhante: {paciente['acompanhante']}")
        print(f"   Restrições: {paciente['restrições']}")

    print()

# Função principal com menu
def menu():
    while True:
        print(" MENU - SISTEMA HOSPITALAR ")
        print("1. Cadastrar Paciente")
        print("2. Listar Pacientes")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_paciente()
        elif opcao == "2":
            listar_pacientes()
        elif opcao == "3":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.\n")

# Execução do programa
menu()