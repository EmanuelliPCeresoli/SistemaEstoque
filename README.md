# Sistema de Estoque e Vendas

Projeto desenvolvido para o trabalho avaliativo de Estrutura de Dados, com o objetivo de aplicar na prática conceitos de estruturas de dados, algoritmos, orientação a objetos e persistência de dados.

## Informações acadêmicas

- **Disciplina:** Organização e Abstração na Programação
- **Trabalho:** Sistema de Estoque de Vendas
- **Linguagem:** Python

## Integrantes

- Emanuelli
- 1139246 - Isadora Severo Sacomori 
- 1139405 - Maria Eduarda Radin

## Sobre o projeto

O Sistema de Estoque e Vendas é um sistema desenvolvido em Python para realizar o gerenciamento de clientes, produtos, estoque e vendas.

O sistema permite cadastrar, consultar, atualizar e remover clientes e produtos, além de realizar vendas e consultar informações relacionadas ao estoque e às vendas realizadas.

O projeto utiliza diferentes estruturas de dados para organizar as informações e algoritmos para realizar operações de busca e ordenção.

Os dados também são armazenados em arquivos CSV, permitindo que as informações sejam mantidas mesmo após o encerramento do programa.

## Como executar
1. Clone o repositório;
2. Entre na pasta do projeto;
3. Execute o programa no "main.py".

## Funcionalidades

O sistema possui as seguintes funcionalidades:

### Clientes

- Cadastrar cliente;
- Listar clientes;
- Buscar cliente pelo código;
- Remover cliente.

### Produtos

- Cadastrar produto;
- Listar produtos;
- Buscar produto pelo código;
- Atualizar quantidade do estoque;
- Remover produto;
- Listar produtos em ordem inversa;
- Listar produtos ordenados por ID;
- Buscar produto por ID utilizando busca binária.

### Vendas

- Realizar venda;
- Visualizar as vendas realizadas;
- Visualizar a primeira venda da fila;
- Calcular o valor total das vendas;
- Exibir os clientes e seus valores totais gastos;
- Identificar o cliente que mais gastou;
- Identificar o produto mais vendido.

### Outras Funcionalidades

- Calcular o valor do estoque;
- Desfazer a última operação realizada;
- Salvar os dados em arquivos CSV;
- Carregar os dados salvos ao iniciar o sistema.

## Estruturas de Dados

O projeto utiliza diferentes estruturas de dados para realizar as operações do sistema.

### Lista Simplesmente Encadeada (LSE)

Utilizada para armazenar e manipular os clientes cadastrados.

### Lista Duplamente Encadeada (LDE)

Utilizada para armazenar os produtos. A estrutura permite percorrer os elementos tanto do início para o fim quanto do fim para o início.

### Fila

Utilizada para armazenar as vendas realizadas, seguindo o princípio FIFO (First In, First Out).

### Pilha

Utilizada para armazenar o histórico das operações realizadas, permitindo desfazer a última operação utilizando o princípio LIFO (Last In, First Out).

## Algoritmos

O projeto utiliza algoritmos para realizar operações sobre os dados armazenados.

Entre as operações implementadas estão:

- Insertion Sort para ordenação de produtos por código;
- Busca binária de produtos por código;
- Buscas sequenciais utilizadas nas operações que não exigem Busca Binária;
- Cálculo do valor total do estoque;
- Cálculo do valor total das vendas;
- Identificação do cliente que mais gastou;
- Identificação do produto mais vendido.

### Insertion Sort
A ordenação dos produtos por código é realizada utilizando o algoritmo Insertion Sort, implementado manualmente. 
O algoritmo percorre os produtos e insere cada elemento na posição correta em relação aos anteriores.

Complexidade:
- Melhor caso: O(n)
- Caso médio: O(n²)
- Pior caso: O(n²)
- Espaço adicional: O(n)

### Busca Binária
A Busca Binária é utilizada para localizar produtos pelo código.
Antes da busca, os produtos são organizados em ordem crescente de código.
A partir disso, o algoritmo compara o código procurado com o elemento central da coleção e elimina metade dos elementos a cada etapa.

Complexidade:
- Melhor caso: O(1)
- Caso médio: O(log n)
- Pior caso: O(log n)
- Espaço adicional: O(1)

## Persistência de dados

A persistência dos dados é realizada por meio de arquivos CSV.

O sistema utiliza três arquivos principais:

data/ 
├── clientes.csv 
├── produtos.csv 
└── vendas.csv

Os arquivos são criados automaticamente pelo sistema quando necessário.

Ao iniciar o programa, os dados armazenados nos arquivos são carregados para as estruturas de dados utilizadas pelo sistema.

Durante as operações de cadastro, alteração, remoção e venda, os dados são atualizados nos arquivos correspondentes.

### Formato das vendas

As vendas são armazenadas no arquivo "vendas.csv"

Cada venda possui:
- código da venda;
- código do cliente;
- produtos vendidos;
- quantidade de cada produto;
- preço unitário;
- valor total.

## Organização do projeto

SistemaEstoque/
│ 
├── Algoritmos/ 
│ ├── busca_binaria.py 
│ └── ordenacao.py 
│ 
├── Estruturas/ 
│ ├── Fila.py 
│ ├── LDE.py 
│ ├── LSE.py 
│ ├── Nodo.py 
│ └── Pilha.py
│ 
├── Models/ 
│ ├── cliente.py 
│ ├── produto.py 
│ └── venda.py
│ 
├── Services/ 
│ ├── estoque_service.py 
│ └── persistencia_service.py 
│
├── data/ 
│ ├── clientes.csv 
│ ├── produtos.csv 
│ └── vendas.csv 
│ 
├── main.py 
└── README.md

## Tecnologias utilizadas

- Python
- Git
- GitHub
- Estruturas de Dados
- Programação Orientada a Objetos
- Arquivos CSV

## Menu do sistema

============================== 
SISTEMA DE ESTOQUE E VENDAS ============================== 
1 - Cadastrar cliente 
2 - Listar clientes 
3 - Buscar cliente 
4 - Remover cliente 
5 - Cadastrar produto 
6 - Listar produtos 
7 - Buscar produto 
8 - Atualizar estoque 
9 - Remover produto 
10 - Listar produtos em ordem inversa 
11 - Listar produtos ordenados por ID 
12 - Buscar produto por ID usando Busca Binaria 
13 - Realizar venda simples de exemplo 
14 - Visualizar fila de vendas 
15 - Visualizar primeira venda da fila 
16 - Exibir valor total do estoque 
17 - Exibir valor total das vendas 
18 - Exibir clientes e valores totais gastos 
19 - Exibir cliente que mais gastou 
20 - Exibir produto mais vendido 
21 - Desfazer ultima operacao 
0 - Sair

## Objetivo acadêmico

O projeto tem como objetivo aplicar os conteúdos estudados na disciplina de Organização e Abstração na Programação, utilizando estruturas como listas encadeadas, fila, pilha, além de algoritmos de busca e ordenação.

Também são aplicados conceitos de organização do código, programação orientada a objetos e persistência de informações.