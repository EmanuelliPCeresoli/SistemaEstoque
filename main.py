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

    elif opcao == 11:
        produtos = service.listar_produtos_ordenados_por_id()

        if len(produtos) == 0:
            print("Nenhum produto cadastrado.")
        else:
            for produto in produtos:
                print(produto)

    elif opcao == 12:
        codigo = ler_inteiro("Código do produto: ")
        produto = service.buscar_produto_binario(codigo)

        if produto is None:
            print("Produto não encontrado.")
        else:
            print("\nProduto encontrado:")
            print(produto)

    elif opcao == 13:
        codigo_cliente = ler_inteiro("Código do cliente: ")
        codigo_produto = ler_inteiro("Código do produto: ")
        quantidade = ler_inteiro("Quantidade: ")
        venda = service.realizar_venda_exemplo(codigo_cliente, codigo_produto, quantidade)
        print("\nVenda realizada com sucesso!")
        print(venda)

    elif opcao == 14:
        vendas = service.listar_vendas()

        if len(vendas) == 0:
            print("Nenhuma venda realizada.")
        else:
            for venda in vendas:
                print(venda)

    elif opcao == 15:
        venda = service.primeira_venda()

        if venda is None:
            print("A fila de vendas está vazia.")
        else:
            print("\nPrimeira venda da fila:")
            print(venda)

    elif opcao == 16:
        total = service.valor_total_estoque()
        print(f"\nValor total do estoque: R$ {total:.2f}")

    elif opcao == 17:
        total = service.valor_total_vendas()
        print(f"\nValor total das vendas: R$ {total:.2f}")

    elif opcao == 18:
        dados = service.clientes_e_valores_totais_gastos()

        if len(dados) == 0:
            print("Nenhuma venda realizada.")
        else:
            print("\nClientes e valores totais gastos:")

            for cliente, total in dados:
                print(f"{cliente} - " f"Total gasto: R$ {total:.2f}")

    elif opcao == 19:
        resultado = service.cliente_que_mais_gastou()

        if resultado is None:
            print("Nenhuma venda realizada.")
        else:
            cliente, total = resultado
            print("\nCliente que mais gastou:")
            print(cliente)
            print(f"Total gasto: R$ {total:.2f}")

    elif opcao == 20:
        resultado = service.produto_mais_vendido()

        if resultado is None:
            print("Nenhuma venda realizada.")
        else:
            produto, quantidade = resultado
            print("\nProduto mais vendido:")
            print(produto)
            print(f"Quantidade vendida: {quantidade}")

    elif opcao == 21:
        resultado = service.desfazer_ultima_operacao()

        if resultado is None:
            print("Não há operações para desfazer.")
        else:
            print(resultado)

    else:
        print("Opção inválida. Tente novamente.")   


def main():
    service = EstoqueService()

    while True:
        mostrar_menu()

        try:
            opcao = ler_inteiro("Escolha uma opcao: ")

            if opcao == 0:
                print("Sistema encerrado.")
                break

            executar_opcao(opcao, service)

        except ValueError as erro:
            print(f"Erro: {erro}")
        except IndexError as erro:
            print(f"Erro: {erro}")
        except NotImplementedError as erro:
            print(f"Funcionalidade para completar: {erro}")

        pausar()

if __name__ == "__main__":
    main() 
