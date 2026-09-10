from Services.estoque_service import EstoqueService

def ler_inteiro(mensagem):
    valor = input(mensagem)
    return int(valor)

def ler_float(mensagem):
    valor = input(mensagem).replace(",", ".")
    return float(valor)

def pausar():
    input("\nPressione ENTER para continuar...")

def imprimir_registros(registros, mensagem_vazia):
    if len(registros) == 0:
        print(mensagem_vazia)
        return

    for registro in registros:
        print(registro)

def mostrar_menu():
    print("\n==============================")
    print("SISTEMA DE ESTOQUE E VENDAS")
    print("==============================")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Buscar cliente")
    print("4 - Remover cliente")
    print("5 - Cadastrar produto")
    print("6 - Listar produtos")
    print("7 - Buscar produto")
    print("8 - Atualizar estoque")
    print("9 - Remover produto")
    print("10 - Listar produtos em ordem inversa")
    print("11 - Listar produtos ordenados por ID")
    print("12 - Buscar produto por ID usando Busca Binaria")
    print("13 - Realizar venda simples de exemplo")
    print("14 - Visualizar fila de vendas")
    print("15 - Visualizar primeira venda da fila")
    print("16 - Exibir valor total do estoque")
    print("17 - Exibir valor total das vendas")
    print("18 - Exibir clientes e valores totais gastos")
    print("19 - Exibir cliente que mais gastou")
    print("20 - Exibir produto mais vendido")
    print("21 - Desfazer ultima operacao")
    print("0 - Sair")

def executar_opcao(opcao, service):
    if opcao == 1:
        nome = input("Nome do cliente: ")
        cliente = service.cadastrar_cliente(nome)
        print("\nCliente cadastrado com sucesso!")
        print(cliente)

    elif opcao == 2:
        clientes = service.listar_clientes()

        if len(clientes) == 0:
            print("Nenhum cliente cadastrado.")
        else:
            for cliente in clientes:
                print(cliente)

    elif opcao == 3:
        codigo = ler_inteiro("Código do cliente: ")
        cliente = service.buscar_cliente(codigo)

        if cliente is None:
            print("Cliente não encontrado.")
        else:
            print("\nCliente encontrado:")
            print(cliente)

    elif opcao == 4:
        codigo = ler_inteiro("Código do cliente:")
        cliente = service.remover_cliente(codigo)
        print("\nCliente removido com sucesso!")
        print(cliente)

    elif opcao == 5:
        nome = input("Nome do produto: ")
        preco = ler_float("Preço do produto: ")
        quantidade = ler_inteiro("Quantidade inicial: ")
        produto = service.cadastrar_produto(nome, preco, quantidade)
        print("\nProduto cadastrado com sucesso!")
        print(produto)

    elif opcao == 6:
        produtos = service.listar_produtos()

        if len(produtos) == 0:
            print("Nenhum produto cadastrado.")
        else:
            for produto in produtos:
                print(produto)

    elif opcao == 7:
        codigo = ler_inteiro("Código do produto: ")
        produto = service.buscar_produto(codigo)

        if produto is None:
            print("Produto não encontrado.")
        else:
            print("\nProduto encontrado: ")
            print(produto)

    elif opcao == 8:
        codigo = ler_inteiro("Código do produto: ")
        quantidade = ler_inteiro("Nova quantidade: ")
        produto = service.atualizar_estoque(codigo, quantidade)
        print("\nEstoque atualizado com sucesso!")
        print(produto)

    elif opcao == 9:
        codigo = ler_inteiro("Código do produto: ")
        produto = service.remover_produto(codigo)
        print("\nProduto removido com sucesso!")
        print(produto)

    elif opcao == 10:
        produtos = service.listar_produtos_inverso()

        if len(produtos) == 0:
            print("Nenhum produto cadastrado.")
        else:
            for produto in produtos:
                print(produto)