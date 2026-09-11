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
        pasta_raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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
                self.produtos.inserir_fim(produto)

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

    def listar_clientes(self):
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

    def remover_produto(self, codigo):
        codigo = int(codigo)

        produto = self.produtos.remover(codigo)

        if self.produtos is None:
            raise ValueError("Produto não encontrado.")

        self.historico.push({
            "tipo": "remover_produto",
            "produto": produto
        })

        self.salvar_produtos()
        return produto

    def listar_produtos_inverso(self):
        return self.produtos.listar_inverso()

    def listar_produtos_ordenados_por_id(self):
        produtos = self.produtos.listar()
        return ordenar_produtos_por_codigo(produtos)

    def buscar_produto_binario(self, codigo):
        produtos = self.listar_produtos_ordenados_por_id()
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

    def realizar_venda(self, codigo_cliente, itens):
        codigo_cliente = int(codigo_cliente)
        cliente = self.buscar_cliente(codigo_cliente)

        if cliente is None:
            raise ValueError("Cliente não encontrado.")

        if not itens:
            raise ValueError("A venda precisa ter pelo menos um produto.")

        itens_venda = []

        for codigo_produto, quantidade in itens:
            codigo_produto = int(codigo_produto)
            quantidade = int(quantidade)

            if quantidade <= 0:
                raise ValueError("A quantidade deve ser maior que zero.")

            produto = self.buscar_produto(codigo_produto)
            if produto is None:
                raise ValueError(f"Produto {codigo_produto} não encontrado.")

            if produto.quantidade < quantidade:
                raise ValueError(f"Estoque insuficiente para "f"{produto.nome}.")

            itens_venda.append({"codigo_produto": produto.codigo, "quantidade": quantidade, "preco_unitario": produto.preco})

        valor_total = 0 

        for item in itens_venda:
            valor_total += (item["quantidade"] * item["preco_unitario"])

        quantidades_anteriores = {}

        for item in itens_venda:
            produto = self.buscar_produto(item["codigo_produto"])

            quantidades_anteriores[produto.codigo] = produto.quantidade

        for item in itens_venda:
            produto = self.buscar_produto(item["codigo_produto"])

            produto.quantidade -= (item["quantidade"])

        venda = Venda(self.gerar_proximo_codigo_venda(), codigo_cliente, itens_venda, valor_total)

        self.vendas.enfileirar(venda)
        self.historico.push({"tipo": "realizar_venda", "venda": venda, "quantidades_anteriores": quantidades_anteriores})
        self.salvar_produtos()
        self.salvar_vendas()

        return venda

    def realizar_venda_exemplo(self, codigo_cliente, codigo_produto, quantidade):
        itens = [(codigo_produto, quantidade)]

        return self.realizar_venda(codigo_cliente, itens)

    def listar_vendas(self):
        return self.vendas.listar()

    def primeira_venda(self):
        if self.vendas.esta_vazia():
            return None

        return self.vendas.primeiro()

    def valor_total_estoque(self):
        total = 0
        for produto in self.produtos.listar():
            total += (produto.preco * produto.quantidade)

        return total

    def valor_total_vendas(self):
        total = 0
        for venda in self.vendas.listar():
            total += venda.valor_total

        return total

    def clientes_e_valores_totais_gastos(self):
        resultado = []
        clientes = self.clientes.listar()
        vendas = self.vendas.listar()

        for cliente in clientes:
            total = 0

            for venda in vendas:
                if(venda.codigo_cliente == cliente.codigo):
                    total += venda.valor_total

            resultado.append((cliente, total))

        return resultado

    def cliente_que_mais_gastou(self):
        dados = (self.clientes_e_valores_totais_gastos())

        if not dados:
            return None

        maior = dados[0]

        for item in dados:
            if item[1] > maior[1]:
                maior = item

        return maior

    def produto_mais_vendido(self):
        vendas = self.vendas.listar()

        if not vendas:
            return None

        quantidades = {}

        for venda in vendas:
            for item in venda.itens:
                codigo = item["codigo_produto"]
                quantidade = item["quantidade"]

                if codigo not in quantidades:
                    quantidades[codigo] = 0

                quantidades[codigo] += quantidade

        if not quantidades:
            return None

        codigo_maior = None
        quantidade_maior = 0

        for codigo, quantidade in quantidades.items():
            if quantidade > quantidade_maior:
                quantidade_maior = quantidade
                codigo_maior = codigo

        produto = self.buscar_produto(codigo_maior)

        return (produto, quantidade_maior)

    def desfazer_ultima_operacao(self):
        if self.historico.esta_vazia():
            return None
        operacao = self.historico.pop()
        tipo = operacao["tipo"]

        if tipo == "cadastrar_cliente":
            cliente = operacao["cliente"]
            self.clientes.remover(cliente.codigo)
            self.salvar_clientes()

            return "Cadastro de cliente desfeito."

        if tipo == "remover_cliente":
            cliente = operacao["cliente"]
            self.clientes.inserir_fim(cliente)
            self.salvar_clientes()

            return "Remoção de cliente desfeita."

        if tipo == "cadastrar_produto":
            produto = operacao["produto"]
            self.produtos.remover(produto.codigo)
            self.salvar_produtos()

            return "Cadastro de produtos desfeito."

        if tipo == "remover_produto":
            produto = operacao["produto"]
            self.produtos.inserir_fim(produto)
            self.salvar_produtos()

            return "Remoção de produto desfeita."

        if tipo == "atualizar_estoque":
            produto = operacao["produto"]
            produto.atualizar_estoque(operacao["quantidade_anterior"])
            self.salvar_produtos()

            return "Alterações de estoque desfeitas."

        if tipo == "realizar_venda":
            venda = operacao["venda"]
            for codigo, quantidade in (operacao["quantidades_anteriores"].items()):
                produto = self.buscar_produto(codigo)
                if produto is not None:
                    produto.quantidade = quantidade

            vendas = self.vendas.listar()
            nova_fila = Fila()
            for item in vendas:
                if item.codigo != venda.codigo:
                    nova_fila.enfileirar(item)

            self.vendas = nova_fila
            self.salvar_produtos()
            self.salvar_vendas()

            return "Venda desfeita"

    def salvar_clientes(self):
        self.persistencia.salvar_clientes(self.clientes.listar())

    def salvar_produtos(self):
        self.persistencia.salvar_produtos(self.produtos.listar())

    def salvar_vendas(self):
        self.persistencia.salvar_vendas(self.vendas.listar())