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