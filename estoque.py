
estoque = {}

def cadastrar_produto():
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade inicial: "))
    estoque[nome] = quantidade
    print("Produto cadastrado com sucesso!")

def consultar_estoque():
    if not estoque:
        print("Estoque vazio.")
    else:
        for nome, quantidade in estoque.items():
            print(f"{nome}: {quantidade} unidades")

def menu():
    while True:
        print("\n=== SISTEMA DE ESTOQUE ===")
        print("1 - Cadastrar produto")
        print("2 - Consultar estoque")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            consultar_estoque()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
