tarefas = []

def adicionar_tarefa(titulo):
    """
    Adicionar uma nova tarefa à lista de tarefas 

    Parâmetros: 
    - titulo (str): o título da tarefa a ser adicionada

    Retorno: 
    - Nenhum
    """
    tarefa = {"titulo": titulo, "concluida": False}  
    tarefas.append(tarefa)
    print(f"Tarefa: '{titulo}' adicionada com sucesso!")

def listar_tarefa():
    """"
    Exibir todas as tarefas pendentes e concluídas, enumeradas.

    Retorno:
    - Nenhum
    """
    if not tarefas:
        print(listar_tarefa.__doc__)
        print("Nenhuma tarefa encontrada.")
    else: 
        for i, tarefa in enumerate(tarefas, 1):
            status = "Concluída" if tarefa["concluida"] else "Pendente"  
            print(f"{i}. {tarefa['titulo']} - {status}")

def concluir_tarefa(id):
    """
    Marcar tarefa como conluida, utilizando como chave o numero da tarefa.
    
    Parametro:
    - Numero/Id (int): Número da tarefa na lista (1-indexed)

    Retorno:
    - Nenhum 
    """
    if 0< id <= len(tarefas):
        tarefas[id - 1]["concluida"] = True
        print(f"Tarefa '{tarefas[id - 1]['titulo']}' marcada como Concluida!!")
    else:
        print("Id de tarefa invalido")

def remover_tarefa(id):
    """
    Remove uma tarefa da lista, utilizando como chave o numero da tarefa.
    
    Parametro:
    - Numero/Id (int): Número da tarefa na lista (1-indexed)

    Retorno:
    - Nenhum 
    """
    if 0 < id <= len(tarefas):
        tarefa_removida = tarefas.pop(id - 1)
        print(f"Tarefa '{tarefa_removida['titulo']}' removida com sucesso!")
    else: 
        print(f"Numero/id invalido.")

def exibir_menu():
    """
    Exibe o menu de opções e retorna a escolha do usuário.

    Retorno: 
    - (str) Escolha do usuário
    """
    print("\nBem-vindo ao sistema de gestão de tarefas\nEscolha uma opção para continuar...\n")
    print("1. Adicionar Tarefa ")
    print("2. Listar Tarefa ")
    print("3. Marcar Tarefa como concluída ")
    print("4. Remover Tarefa ")
    print("5. Sair ")

    return input("\nEscolha uma opção: ")

# Loop principal do menu e operações
while True:
    opcao = exibir_menu()

    if opcao == "1":
        titulo = input("\nDigite o título da tarefa: ")
        adicionar_tarefa(titulo)
    elif opcao == "2":
        listar_tarefa()
    elif opcao =="3":
        try:
            id = int(input("Digite o id/numero da tarefa a ser concluida: "))
            concluir_tarefa(id)
        except ValueError:
            print("Por favor, insira um id valido.")
    elif opcao == "4":
        try:
            id = int(input("Digite o id/numero da tarefa a ser removida: "))
            remover_tarefa(id)
        except ValueError:
            print("Por favor, insira um id valido.")
    elif opcao == "5":
        print("Saindo do programa, até a proxima.... ")
        break
    else:
        print("Opção invalida. Insira uma opção valida.")

