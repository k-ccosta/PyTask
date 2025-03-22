import os

opcoes_menu = ["Adicionar tarefa", "Visualizar tarefas", "Atualizar tarefa", "Completar tarefa", "Deletar tarefas completadas", "Sair"]
lista_de_tarefas = []

# funções

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def exibir_titulo():
    titulo = "Bem-vindo ao PyTask"
    borda = "*"*(len(titulo))

    print(borda)
    print(titulo.center(len(borda)))
    print(f"{borda}\n")
def exibir_menu():
    for indice, opcao in enumerate(opcoes_menu, start=1):
        print(f"[{indice}] > {opcao}")
def selecionando_opcao():
    while True:
        try:
            opcao = int(input("\nO que você deseja fazer? "))
            if 0 < opcao <= len(opcoes_menu):
                break
            else:
                print("ERROR! Por favor, selecione uma opção valida!")                
        except ValueError:
            print("ERROR! Por favor, selecione uma opção valida!")

    return opcao

def adicionar_tarefa():
    limpar_tela()

    tarefa = {
        "nome":input("Digite o nome da tarefa: "),
        "completada":False 
    }

    lista_de_tarefas.append(tarefa)

    limpar_tela()

while True:
    exibir_titulo()
    exibir_menu()
    opcao_selecionada = selecionando_opcao()

    if opcao_selecionada == 1:
        adicionar_tarefa()
    elif opcao_selecionada == 2:
        ...
    elif opcao_selecionada == 3:
        ...
    elif opcao_selecionada == 4:
        ...
    elif opcao_selecionada == 5:
        ...
    else:
        break

limpar_tela()
print("Pytask encerrado com sucesso")