from classes import Estoque, usuario
estoque = Estoque()
usuario_cadastrado = usuario("joao", '1234')
usuario_input = input("Digite o Nome de Usuario: ")
senha_input = input("Digite sua senha: ")
if usuario_cadastrado.autenticar(usuario_input, senha_input):
            print("acesso liberado")
            while True:
                    digito_usuario = input("=== menu ===\n1 - cadastro de itens\n2 - estoque\n3 - sair\nDigite uma Opcao: ")
    
                    if digito_usuario == "1":
                        estoque.cadastro_itens()
                    elif digito_usuario == "2":
                        estoque.consultar_estoque()
                    elif digito_usuario == "3":
                            break        
else:
        print ("acesso negado")


