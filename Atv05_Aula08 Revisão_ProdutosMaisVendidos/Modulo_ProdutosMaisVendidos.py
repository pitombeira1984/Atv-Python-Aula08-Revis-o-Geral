
def ProdutosMaisVendidos():
    produtos = [
        {"nome": "Camiseta", "quantidade": 100},
        {"nome": "Calça", "quantidade": 50},
        {"nome": "Sapato", "quantidade": 75},
        {"nome": "Meia", "quantidade": 200},
        {"nome": "Tênis", "quantidade": 30}
    ]
    ProdutosMaisVendidos = max(produtos, key=lambda x: x["quantidade"])
    print(f"O produto mais vendido é {ProdutosMaisVendidos['nome']} com {ProdutosMaisVendidos['quantidade']} vendas.")

