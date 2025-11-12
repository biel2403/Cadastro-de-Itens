class usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
    def autenticar(self, usuario_input, senha_input):
        return self.nome == usuario_input and self.senha == senha_input
    
class Estoque:
    def __init__(self):
        self.estoque = {}

    def cadastro_itens(self):
        produto = input("Digite o Nome do Produto: ")
        if produto in self.estoque:
           print("Produto ja Cadastrado")
           return
        quantidade = int(input("Digite a Quantidade: "))
        self.estoque[produto] = quantidade
        
    def consultar_estoque(self):
        if not self.estoque:
            print('Estoque Vazio')
        else:
            for key, value in self.estoque.items():
                print(f"Produto = {key}\nQuantidade = {value}")
