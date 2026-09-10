import os

from Estruturas.LSE import LSE
from Estruturas.LDE import LDE
from Estruturas.Fila import Fila
from Estruturas.Pilha import Pilha

from Models.cliente import Cliente
from Models.produto import Produto
from Models.venda import Venda

from Algoritmos.ordenacao import ordenar_produtos_por_codigo
from Algoritmos.busca_binaria import buscar_produto_por_codigo

from Services.persistencia_service import PersistenciaService

class EstoqueService:
    def __init__(self):
        pasta_raiz = os.path.dirname(os.path.abspath(__file__))
        pasta_data = os.path.join(pasta_raiz, "data")

        self.clientes = LSE()
        self.produtos = LDE()
        self.vendas = Fila()
        self.historico = Pilha()
        self.persistencia = PersistenciaService(pasta_data)

        self.carregar_dados()

    def carregar_dados(self):
        clientes = self.persistencia.carregar_clientes()
        for cliente in clientes:
            if self.clientes.buscar(cliente.codigo) is None:
                self.clientes.inserir_fim(cliente)

        produtos = self.persistencia.carregar_produtos()
        for produto in produtos:
            if self.produtos.buscar(produto.codigo) is None:
                self.produtos. inserir_fim(produto)

        vendas = self.persistencia.carregar_vendas()
        for venda in vendas:
            self.vendas.enfileirar(venda)

    def gerar_proximo_codigo_cliente(self):
        return self._gerar_proximo_codigo(self.clientes.listar())

    def gerar_proximo_codigo_produto(self):
        return self._gerar_proximo_codigo(self.produtos.listar())

    def gerar_proximo_codigo_venda(self):
        return self._gerar_proximo_codigo(self.vendas.listar())

    def _gerar_proximo_codigo(self, registros):
        maior_codigo = 0

        for registro in registros:
            if registro.codigo > maior_codigo:
                maior_codigo = registro.codigo

        return maior_codigo + 1

    def cadastrar_cliente(self, nome):
        nome = nome.strip()

        if nome == "":
            raise ValueError("O nome do cliente é obrigatório.")

        codigo = self.gerar_proximo_codigo_cliente()
        cliente = Cliente(codigo, nome)

        self.clientes.inserir_fim(cliente)
        self.historico.push({"tipo": "cadastrar_cliente", "cliente": cliente})

        self.salvar_clientes()
        return cliente

    def listar_cliente(self):
        return self.clientes.listar()

    def buscar_cliente(self, codigo):
        codigo = int(codigo)
        return self.clientes.buscar(codigo)

    def remover_cliente(self, codigo):
        codigo = int(codigo)
        cliente = self.buscar_cliente(codigo)
        if cliente is None:
            raise ValueError("Cliente não encontrado.")

        removido = self.clientes.remover(codigo)
        if removido is None:
            raise ValueError("Não foi possível remover o cliente.")

        self.historico.push({"tipo": "remover_cliente", "cliente": cliente})
        self.salvar_clientes()

        return cliente

    def cadastrar_produto(self, nome, preco, quantidade):
        nome = nome.strip()
        preco = float(preco)
        quantidade = int(quantidade)

        if nome == "":
            raise ValueError("O nome do produto é obrigatório.")

        if preco <= 0:
            raise ValueError("O preço deve ser maior que zero.")

        if quantidade < 0:
            raise ValueError("A quantidade não pode ser negativa.")

        codigo = self.gerar_proximo_codigo_produto()
        produto = Produto(codigo, nome, preco, quantidade)

        self.produtos.inserir_fim(produto)
        self.historico.push({"tipo": "cadastrar_produto", "produto": produto})
        self.salvar_produtos()

        return produto

    def listar_produtos(self):
        return self.produtos.listar()

    def buscar_produto(self, codigo):
        codigo = int(codigo)
        return self.produtos.buscar(codigo)

    def listar_produtos_inverso(self):
        return self.produtos.listar_inverso()

    def listar_produtos_ordenados_por_id(self):
        produtos = self.produtos.listar()
        return ordenar_produtos_por_codigo(produtos)

    def buscar_produto_binario(self, codigo):
        produtos = (self.listar_produtos_ordenados_por_id())
        codigo = int(codigo)
        return buscar_produto_por_codigo(produtos, codigo)

    def atualizar_estoque(self, codigo, nova_quantidade):
        codigo = int(codigo)
        nova_quantidade = int(nova_quantidade)

        produto = self.buscar_produto(codigo)
        if produto is None:
            raise ValueError("Produto não encontrado.")

        if nova_quantidade < 0:
            raise ValueError("A quantidade não pode ser negativa.")

        quantidade_anterior = produto.quantidade
        produto.atualizar_estoque(nova_quantidade)

        self.historico.push({"tipo": "atualizar_estoque", "produto": produto, "quantidade_anterior": quantidade_anterior})
        self.salvar_produtos()

        return produto
    