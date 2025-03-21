import os

opcoes_menu = ["Adicionar tarefa", "Visualizar tarefas", "Atualizat tarefa", "Completar tarefa", "Deletar tarefas completadas", "Sair"]

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

while True:
    exibir_titulo()
    exibir_menu()

    opcao_selecionada = int(input("\nO que você deseja fazer? "))

    if opcao_selecionada == 6:
        break

limpar_tela()
print("Pytask encerrado com sucesso")