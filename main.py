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

def visualizar_tarefas():
    limpar_tela()
  
    print(f"{'Índice'.ljust(1)}|{'Nome'.ljust(40)}|Completada")

    for indice, tarefa in enumerate(lista_de_tarefas, start=1):
        nome = tarefa["nome"]
        completada = tarefa["completada"]

        print(f"{str(indice).ljust(5)} |{nome.ljust(40)}|{'✅' if completada else ''}")

    sair = input("\nPressiona 'enter' para sair ")  

    limpar_tela()  

def atualizar_tarefa():
    limpar_tela()
  
    if len(lista_de_tarefas) == 0:
        print("Lista de tarefas vazia")
    
        sair = input("\nPressiona 'enter' para sair ")

        limpar_tela()
    else:
        print(f"{'Índice'.ljust(1)}|{'Nome'.ljust(40)}|Completada")

        for indice, tarefa in enumerate(lista_de_tarefas, start=1):
            nome = tarefa["nome"]
            completada = tarefa["completada"]

            print(f"{str(indice).ljust(5)} |{nome.ljust(40)}|{'✅' if completada else ''}")
        
        indice = int(input("\nDigite o indice da tarefa que deseja editar: "))
        
        """
        Em Python, listas usam índice base 0, mas como você está mostrando as tarefas para o usuário começando do 1, precisa ajustar o índice informado subtraindo 1.
        """
        indice_ajustado = indice - 1

        if 0 <= indice_ajustado < len(lista_de_tarefas):
            novo_nome = input("Digite o novo nome da tarefa: ")
            lista_de_tarefas[indice_ajustado]["nome"] = novo_nome
            print("Tarefa atualizada com sucesso!")
        else:
            print("Índice inválido!")

    input("\nPressione 'enter' para continuar...")
    limpar_tela()

while True:
    exibir_titulo()
    exibir_menu()
    opcao_selecionada = selecionando_opcao()

    if opcao_selecionada == 1:
        adicionar_tarefa()
    elif opcao_selecionada == 2:
        visualizar_tarefas()
    elif opcao_selecionada == 3:
        atualizar_tarefa()
    elif opcao_selecionada == 4:
        ...
    elif opcao_selecionada == 5:
        ...
    else:
        break

limpar_tela()
print("Pytask encerrado com sucesso")