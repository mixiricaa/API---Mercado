Este projeto é uma API RESTful construída com Flask para gerenciar clientes, produtos e vendas. Os dados são armazenados em arquivos CSV. A API permite adicionar, atualizar, listar e excluir registros de clientes, produtos e ordens.

---

Requisitos

Para rodar esta aplicação, você precisa ter os seguintes itens instalados:

- Python 3.x (recomenda-se a versão 3.7 ou superior)

- pip (gerenciador de pacotes do Python)

Além disso, a aplicação usa o framework Flask, que pode ser instalado com o seguinte comando:

pip install Flask

----

Endpoints da API

Gerenciamento de Clientes:

GET /clientes
- Retorna todos os clientes cadastrados no arquivo cliente.csv.

POST /add_clientes
- Adiciona um novo cliente. O corpo da requisição deve ser um JSON com os seguintes dados:

  {
  
    "nome": "Nome do Cliente",
  
    "sobrenome": "Sobrenome do Cliente",
  
    "data de nascimento": "DD/MM/AAAA",
  
    "cpf": "000.000.000-00"
  
  }


PUT /atualizar_clientes
- Atualiza as informações de um cliente. O corpo da requisição deve ser um JSON com o nome do cliente e os campos a serem atualizados:
  
  {
  
    "nome": "Nome do Cliente",
  
    "sobrenome": "Novo Sobrenome",
  
    "data de nascimento": "Novo Data de Nascimento",
  
    "cpf": "Novo CPF"
  
  }

DELETE /deletar_clientes
- Deleta um cliente com base no id. O corpo da requisição deve ser um JSON com o id do cliente:

  {
  
    "id": 1

  }

---


Gerenciamento de Produtos


GET /produtos
- Retorna todos os produtos cadastrados no arquivo produto.csv.
  

POST /add_produtos
- Adiciona um novo produto. O corpo da requisição deve ser um JSON com os seguintes dados:


  {
  
    "nome": "Nome do Produto",
  
    "fornecedor": "Fornecedor do Produto",
  
    "quantidade": 10
  
  }

PUT /atualizar_produtos
- Atualiza as informações de um produto. O corpo da requisição deve ser um JSON com o id do produto e os campos a serem atualizados:

  {
  
    "id": 1,
  
    "nome": "Novo Nome do Produto",
  
    "fornecedor": "Novo Fornecedor",
  
    "quantidade": 20
  
  }

DELETE /deletar_produtos
- Deleta um produto com base no id. O corpo da requisição deve ser um JSON com o id do produto:

  {
  
    "id": 1
  
  }

---

Gerenciamento de Vendas

GET /ordens
- Retorna todas as ordens cadastradas no arquivo ordens.csv.

POST /nova_ordem
- Cria uma nova ordem. O corpo da requisição deve ser um JSON com os seguintes dados:

  {
  
    "id": 1,
  
    "Cliente": "Nome do Cliente",
  
    "Produto": "Nome do Produto"
  
  }

PUT /atualizar_ordens
- Atualiza as informações de uma ordem. O corpo da requisição deve ser um JSON com o id da ordem e os campos a serem atualizados:
  
  {
  
    "id": 1,
  
    "Cliente": "Novo Cliente",
  
    "Produto": "Novo Produto"
  
  }

---

Executar o servidor

No terminal, execute o seguinte comando para rodar o servidor Flask:

python app.py




