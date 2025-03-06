from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)

file_path = 'arquivo.csv'


@app.route("/clientes", methods=["GET"])
def cliente():
    try:
       file_path = 'cliente.csv'
       clientes = []
       with open(file_path, 'r', encoding='utf-8', newline='') as arquivo:
           reader = csv.reader(arquivo)
           for linha in reader:
               clientes.append(linha)
       return jsonify(clientes), 200
    except Exception as e:
       return jsonify(f"Error {e}"), 404
    

@app.route("/add_clientes", methods=["post"])
def add_cliente():
    try:
       data = request.get_json()
       global id
       id += 1
       clientes = [id, data["nome"], data["sobrenome"], data["data de nascimento"], data["cpf"]]
       file_path = 'cliente.csv'
       with open(file_path, mode='a', newline='', encoding='utf-8') as arquivo:
           writer = csv.writer(arquivo)
           writer.writerow(clientes)
       return jsonify({"": "Cliente adicionado!", "cliente": clientes}), 200
    except Exception as e:
        return jsonify(f"Error {e}"), 404
    
       
@app.route("/atualizar_clientes" , methods=["PUT"])
def atualizar():
    try:
        data = request.get_json()
        file_path = 'cliente.csv'
        clientes = []
        cliente_nome = data["nome"]
        print(cliente_nome)
        with open(file_path, 'r', encoding='utf-8', newline='') as arquivo:
            reader = csv.reader(arquivo)
            for linha in reader:
                if linha[1] == cliente_nome:
                    linha[2] = data.get("sobrenome", linha[2])
                    linha[3] = data.get("data de nascimento", linha[3])
                    linha[4] = data.get("cpf", linha[4])
                clientes.append(linha)
        with open(file_path, mode='w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(clientes)
        return jsonify({"": "Cliente atualizado!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

    

@app.route("/deletar_clientes", methods=["DELETE"])
def delete_cliente():
    try:
        file_path = 'cliente.csv'
        clientes = []
        data = request.get_json()
        cliente_id = data["id"]
        cliente_encontrado = False

        if not data or "id" not in data:
            return jsonify({"error": "ID do cliente é obrigatório"}), 400
        

        with open(file_path, mode='r', newline='', encoding='utf-8') as arquivo:
            reader = csv.reader(arquivo)
            for linha in reader:
                if linha[0] == cliente_id:
                    cliente_encontrado = True 
                else:
                    clientes.append(linha)

                if not cliente_encontrado:
                 return jsonify({"error": "Cliente não encontrado"}), 404
        
        with open(file_path, mode='w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(cliente)
            return jsonify({"Cliente deletado!"}), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500




@app.route("/produtos", methods=["GET"])
def produto():
    try:
       file_path = "produto.csv"
       produtos = []

       with open(file_path, 'r', encoding='utf-8', newline='') as arquivo:
           reader = csv.reader(arquivo)

           for linha in reader:
               produtos.append(linha)
       return jsonify(produtos), 200
       
    except Exception as e:
       return jsonify("Error"), 404
    

@app.route("/add_produtos", methods=["post"])
def add_produto():
    try:
       data = request.get_json()
       global id
       id += 1
       produto = [id, data["nome"], data["fornecedor"],  data["quantidade"]]
       file_path = "produto.csv"
       with open(file_path, mode='a', newline='', encoding='utf-8') as arquivo:
           writer = csv.writer(arquivo)
           writer.writerow(produto)
       return jsonify({"": "Produto adicionado!"}), 200
    except Exception as e:
        return jsonify({"Error"}), 404
    
       
@app.route("/atualizar_produtos", methods=["PUT"])
def atualizar_produtos():
    try:
        data = request.get_json()
        file_path = "produto.csv"
        produto = []
        produto_id = data["id"]
        with open(file_path, 'r', encoding='utf-8', newline='') as arquivo:
            reader = csv.reader(arquivo)
            for linha in reader:
                if linha[0] == produto_id:
                    linha[1] = data.get("nome", linha[1])
                    linha[2] = data.get("fornecedor", linha[2])
                    linha[3] = data.get("quantidade", linha[3])
                produto.append(linha)
        with open(file_path, mode='w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(produto)
        return jsonify({"message": "Cliente atualizado!"}), 200
    except Exception as e:
        return jsonify({"Error"}), 404
    

@app.route("/deletar_produtos", methods=["DELETE"])
def delete_produto(id):
    try:
        file_path = "produto.csv"
        produto = []
        with open(file_path, mode='r', newline='', encoding='utf-8') as arquivo:
            reader = csv.reader(arquivo)
            for linha in reader:
                if (linha[0]) != id:
                    produto.append(linha)
        
        with open(file_path, mode='w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(produto)
            return jsonify({"": "Produto deletado!"}), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@app.route("/ordens", methods=["GET"])
def cliente():
    try:
       file_path = 'ordens.csv'
       ordens = []
       with open(file_path, 'r', encoding='utf-8', newline='') as arquivo:
           reader = csv.reader(arquivo)
           for linha in reader:
               ordens.append(linha)
       return jsonify(ordens), 200
    except Exception as e:
       return jsonify(f"Error {e}"), 404
    
@app.route("/nova_ordem", methods=["post"])
def nova_ordem():
    try:
       data = request.get_json()
       global id
       id += 1
       ordens = [data["id"], data["Cliente"], data["Produto"]]
       file_path = 'ordens.csv'
       with open(file_path, mode='a', newline='', encoding='utf-8') as arquivo:
           writer = csv.writer(arquivo)
           writer.writerow(ordens)
       return jsonify({"": "Ordem adicionada!", "Ordem": ordens}), 200
    except Exception as e:
        return jsonify(f"Error {e}"), 404

@app.route("/atualizar_ordens" , methods=["PUT"])
def atualizar_ordens():
    try:
        data = request.get_json()
        file_path = 'ordens.csv'
        ordens = []
        ordem_id = data["id"]
        print(ordens)
        with open(file_path, 'r', encoding='utf-8', newline='') as arquivo:
            for id in reader = csv.reader(arquivo)reader:
                if linha[0] == id:
                    linha[1] = data.get("Cliente", linha[1])
                    linha[2] = data.get("Produto", linha[3])
                ordens.append(linha)
        with open(file_path, mode='w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(clientes)
        return jsonify({"": "Cliente atualizado!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404






if __name__ == '_main_':
    app.run(debug=True, host='0.0.0.0')