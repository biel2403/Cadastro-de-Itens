estoque = {}
#CADASTRO DE ITENS
def cadastro_itens():
    produto = input("Digite o nome do produto: ")
    if produto in estoque:
        print("Produto ja cadastrado")
        return
    quantidade = int(input("Digite a Quantidade: "))
    estoque[produto] = {'quantidade':quantidade}
#CONSULTA DE ITENS
def consultar_estoque():
    print(estoque)
#ENTRADAS E SAIDAS
def entradas_saidas():
    entrada = input("Digite o nome do produto: ")
    if entrada in estoque:
        adicionar = int(input("Digite a Quantidade"))
        estoque[produto]+["quantidade"] =adicionar
     

while True:
    print ("---OLHA O SISTEMA AÍ")
    usuario = input("insira seu usuario: ")
    senha = int(input("insira sua senha: "))
    if usuario == "joao" and senha == 1234:
            print("acesso liberado")
            while True:
                    digito_usuario = input("=== menu ===\n1 - cadastro de itens\n2 - estoque\n3 - entradas e saídas\n4 - sair\nDigite uma Opcao: ")
    
                    if digito_usuario == "1":
                            cadastro_itens()
                    elif digito_usuario == "2":
                           consultar_estoque()

                    elif digito_usuario == "3":
                            entradas_saidas()

                    elif digito_usuario == "4":
                            break        
    else:
        print ("acesso negado")
