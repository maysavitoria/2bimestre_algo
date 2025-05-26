compras = []
while True:
    print("\n escolha uma opção:")
    print("\n 1 - Adicionar item")
    print("\n 2 - Remover item")
    print("\n 3 - Listar itens")
    print("\n 4 - Encerra")
    
    opcao = input("Digite a opção:")
    if opcao == "1":
        item = input("Digite o item a ser adicionado: ")
        compras.append(item)
        print(f"{item} adicionado à lista de compras.")
    elif opcao == "2":
        item = input("Digite o item a ser removido: ")
        if item in compras:
            compras.remove(item)
            print(f"{item} removido da lista de compras.")
            print(f"Lista de compras atualizada: {compras}")
        else:
            print(f"{item} não encontrado na lista de compras.")
    elif opcao == "3":
        comprass = (compras) 
        for compras in comprass:
            print("-", compras)
    elif opcao == "4":
        print("lista de compras encerrada.")
        print(f"Lista final de compras: {compras}")
        break
    else:
        print("Opção inválida. Tente novamente.")
