idUsuario = 0 #acumulador
funcionarios = {} #dicionário

def cabecalho(): #Função 1
    print("Seja bem-vindo ao Controle de Funcionários da Giulia Silveira Chagas")
    print()

def menuPrincipal(): #Função 2
    global idUsuario #Acessa a variável fora do escopo
    while True:
        print("----------------- Menu Principal -----------------")
        print("Escolha a opção desejada: ")
        print("1 - Cadastrar Funcionário")
        print("2 - Consultar Funcionário(s)")
        print("3 - Remover Funcionário")
        print("4 - Finalizar o sistema")

        try:
            menu_principal = int(input()) #Se o usuário não digitar um número, cai no except
        except:
            print("Por favor, utilize somente números. Tente novamente:")
            continue

        if menu_principal == 1:
            idUsuario += 1 #Adiciona mais 1 na variável acumuladora
            cadastrar_funcionario(idUsuario) #Cai na função 'cadastrar_funcionário(id)'
            continue #Começa o laço de repetição novamente
        elif menu_principal == 2:
            consultar_funcionarios() 
            continue
        elif menu_principal == 3:
            remover_funcionario()
            continue
        elif menu_principal == 4:
            break #Cai na função 'finalizando()' e finaliza o sistema
        else:
            print("Valor inválido, tente novamente")
            continue

def cadastrar_funcionario(id): #Função 3
    global funcionarios #Acessa a variável fora do escopo
    while True:
        print("-------------- Menu de Cadastrar Funcionário --------------")
        print("Código do funcionário: " + str(id))

        funcionarios[id] = {} #Acessa o dicionário e inclui o idUsuario
        funcionarios[id]['Nome']= input("Digite o nome do funcionário: ") #Adiciona a chave e o valor dentro do dicionário
        funcionarios[id]['Setor']= input("Digite o setor: ")
        funcionarios[id]['Salario']= float(input("Insira o salário: R$ "))

        print("Funcionário adicionado")
        break #Volta para a função 'menuPrincipal()'


def consultar_funcionarios(): #Função 4
    global funcionarios #Acessa a variável fora do escopo
    while True:
        print("-------------- Menu Consultar Funcionários --------------")
        print("Escolha a opção desejada: ")
        print("1 - Consultar todos os funcionários")
        print("2 - Consultar funcionários por ID")
        print("3 - Consultar funcionários por Setor")
        print("4 - Sair")

        try:
            consultaFuncionario = int(input())
        except:
            print("Por favor, utilize somente números. Tente novamente:")
            continue

        if consultaFuncionario == 1:
            for id in funcionarios:
                consulta_funcionario(id) #Consulta as chaves e os valores dentro do dicionário
            continue #Retorna para o inicio da estrutura de repetição
        elif consultaFuncionario == 2:
            try:
                id = int(input("Digite o ID do funcionário: "))
            except:
                print("Por favor, utilize somente números. Tente novamente:")
                continue
            consulta_funcionario(id) #Consulta o dicionário com base no id digitado
            continue
        elif consultaFuncionario == 3:
            #faz a busca por setor do funcionario 
            setor = input("Digite o Setor: ")
            for id in funcionarios: 
                if funcionarios[id]["Setor"] == setor:
                    consulta_funcionario(id) 
            continue
        elif consultaFuncionario == 4:
            break
        else:
            print("Valor inválido, tente novamente")
            continue

def consulta_funcionario(id): #Função 5
    global funcionarios #Acessa a variável fora do escopo
    funcionario = funcionarios[id]
    #monta uma apresentação baseada no funcionario encontrado
    print('id: ' + str(id))
    print('nome: ' + funcionario["Nome"])
    print('setor: ' + funcionario['Setor'])
    print('salário: ' + str(funcionario["Salario"]))

def remover_funcionario(): #Função 6
    global funcionarios #Acessa a variável fora do escopo
    while True:
        print("--------------- Menu Remover Funcionário ---------------")

        try:
            funcionarioRemover = int(input("Digite o ID do funcionário a ser removido: "))
        except:
            print("Por favor, digite apenas números. Tente novamente!")
            continue

        del funcionarios[funcionarioRemover]
        break

def finalizando(): #Função 7
    print("Encerrando o sistema...")

#Chamando as funções
cabecalho()
menuPrincipal()
finalizando()