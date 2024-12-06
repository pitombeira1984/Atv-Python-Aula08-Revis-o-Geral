

def Manipulacao_Produtos():
    dados_produto = [
        {
            "nome": "Produto 1",
            "preco": 10.99,
            "quantidade": 5
        },
        {
            "nome": "Produto 2",
            "preco": 20.50,
            "quantidade": 3
        },
        {
            "nome": "Produto 3",
            "preco": 15.75,
            "quantidade": 2
        }
    ]
    while True:
        print("\nMenu:")
        print("1. Adicionar Produto")
        print("2. Remover Dados_Produtos")
        print("3. Atualizar Dados_Produto")
        print("4. Listar Dados_Produtos")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            produto = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            quantidade = int(input("Digite a quantidade do produto: "))
            dados_produto.append({"nome": produto, "preco": preco, "quantidade": quantidade})
            print("Produto adicionado com sucesso!")
        elif opcao == "2":
            produto = input("Digite o nome do produto para remover: ")
            for i in dados_produto:
                if i["nome"] == produto:
                    dados_produto.remove(i)
                    print("Produto removido com sucesso!")
                    break
                else:
                    print("Produto não encontrado.")
        elif opcao == "3":
            produto = input("Digite o nome do produto para atualizar: ")
            for i in dados_produto:
                if i["nome"] == produto:
                    preco = float(input("Digite o novo preço do produto: "))
                    quantidade = int(input("Digite a nova quantidade do produto: "))
                    i["preco"] = preco
                    i["quantidade"] = quantidade
                    print("Produto atualizado com sucesso!")
                    break
                else:
                    print("Produto não encontrado.")
        elif opcao == "4":
            print("Lista de Produtos:")
            for i in dados_produto:
                print(f"Nome: {i['nome']}, Preço: {i['preco']}, Quantidade: {i['quantidade']}")
        elif opcao == "0":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
Manipulacao_Produtos()