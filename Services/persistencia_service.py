import csv
import os

from Models.cliente import Cliente
from Models.produto import Produto
from Models.venda import Venda

class PersistenciaService:
    def __init__(self, pasta_data):
        self.pasta_data = pasta_data
        self.arquivo_clientes = os.path.join(pasta_data, "clientes.csv")
        self.arquivo_produtos = os.path.join(pasta_data, "produtos.csv")
        self.arquivo_vendas = os.path.join(pasta_data, "vendas.csv")
        self.garantir_arquivos()

    def garantir_arquivos(self):
        os.makedirs(self.pasta_data, exist_ok=True)
        self._garantir_csv(self.arquivo_clientes, ["codigo", "nome"])
        self._garantir_csv(self.arquivo_produtos, ["codigo", "nome", "preco", "quantidade"])
        self._garantir_csv(self.arquivo_vendas, ["codigo", "codigo_cliente", "itens", "valor_total"])

    def _garantir_csv(self, caminho, cabecalho):
        if os.path.exists(caminho) and os.path.getsize(caminho) > 0:
            return

        with open(caminho, "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv. writer(arquivo)
            escritor.writerow(cabecalho)

    def carregar_clientes(self):
        return self._carregar(self.arquivo_clientes, Cliente.cliente_from_csv_row)

    def carregar_produtos(self):
        return self._carregar(self.arquivo_produtos, Produto.produto_from_csv_row)

    def carregar_vendas(self):    
        return self._carregar(self.arquivo_vendas, Venda.venda_from_csv_row)

    def _carregar(self, caminho, construtor):
        registros = []

        try:
            with open(caminho, "r", newline="", encoding="utf-8") as arquivo:
                leitor = csv.DictReader(arquivo)

                for row in leitor:
                    try:
                        registros.append(construtor(row))
                    except (KeyError, TypeError, ValueError, IndexError):
                        print(f"Aviso: linha inválida ignorada em {caminho}.")

        except FileNotFoundError:
            self.garantir_arquivos()

        except OSError:
            print(f"Aviso: não foi possível ler {caminho}.")

        return registros
