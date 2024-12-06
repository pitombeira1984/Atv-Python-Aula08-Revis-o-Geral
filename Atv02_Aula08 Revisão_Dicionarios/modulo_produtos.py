
class modulos_produtos:

    def adicionar_produto(dados_produto):
        produto = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade do produto: "))
        dados_produto.append({"nome": produto, "preco": preco, "quantidade": quantidade})
        print("Produto adicionado com sucesso!")

    def remover_produto(dados_produto):
        produto = input("Digite o nome do produto para remover: ")
        for i in dados_produto:
            if i["nome"] == produto:
                dados_produto.remove(i)
                print("Produto removido com sucesso!")
                return
        print("Produto não encontrado.")

    def atualizar_produto(dados_produto):
        produto = input("Digite o nome do produto para atualizar: ")
        for i in dados_produto:
            if i["nome"] == produto:
                preco = float(input("Digite o novo preço do produto: "))
                quantidade = int(input("Digite a nova quantidade do produto: "))
                i["preco"] = preco
                i["quantidade"] = quantidade
                print("Produto atualizado com sucesso!")
                return
        print("Produto não encontrado.")

    def listar_produtos(dados_produto):
        print("Lista de Produtos:")
        for i in dados_produto:
            print(f"Nome: {i['nome']}, Preço: {i['preco']}, Quantidade: {i['quantidade']}")

    def exibir_menu():
        print("\nMenu:")
        print("1. Adicionar Produto")
        print("2. Remover Produto")
        print("3. Atualizar Produto")
        print("4. Listar Produtos")
        print("0. Sair")
        
            
        