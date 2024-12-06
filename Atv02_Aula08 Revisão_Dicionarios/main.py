from modulo_produtos import modulos_produtos

def main():
    dados_produto = [
        {"nome": "Produto 1", "preco": 10.99, "quantidade": 5},
        {"nome": "Produto 2", "preco": 20.50, "quantidade": 3},
        {"nome": "Produto 3", "preco": 15.75, "quantidade": 2},
    ]

    while True:
        modulos_produtos.exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            modulos_produtos.adicionar_produto(dados_produto)
        elif opcao == "2":
            modulos_produtos.remover_produto(dados_produto)
        elif opcao == "3":
            modulos_produtos.atualizar_produto(dados_produto)
        elif opcao == "4":
            modulos_produtos.listar_produtos(dados_produto)
        elif opcao == "0":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()