from flask import Flask, jsonify, request
from db import obter_conexao

app = Flask(__name__)

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    conn = obter_conexao()
    cur = conn.cursor()
    cur.execute("SELECT id, descricao, estado FROM produtos")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    produtos = [{'id': row[0], 'descricao': row[1], 'estado': row[2]} for row in rows]
    return jsonify(produtos)

@app.route('/produtos/<int:id>', methods=['GET'])
def buscar_produto_por_id(id):
    conn = obter_conexao()
    cur = conn.cursor()
    cur.execute("SELECT id, descricao, estado FROM produtos WHERE id = %s", (id,))
    row = cur.fetchone()
    cur.close()
    conn.close()

    if row:
        produto = {'id': row[0], 'descricao': row[1], 'estado': row[2]}
        return jsonify(produto)
    else:
        return jsonify({'Erro': 'Produto não encontrado'}), 404

@app.route('/produtos', methods=['POST'])
def adicionar_produto():
    dados = request.get_json()
    descricao = dados.get('descricao')
    estado = dados.get('estado')

    conn = obter_conexao()
    cur = conn.cursor()
    cur.execute("INSERT INTO produtos (descricao, estado) VALUES (%s, %s) RETURNING id", (descricao, estado))
    novo_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({'id': novo_id, 'descricao': descricao, 'estado': estado}), 201

@app.route('/produtos/<int:id>', methods=['PUT'])
def editar_produto(id):
    dados = request.get_json()
    descricao = dados.get('descricao')
    estado = dados.get('estado')

    conn = obter_conexao()
    cur = conn.cursor()
    cur.execute("UPDATE produtos SET descricao = %s, estado = %s WHERE id = %s", (descricao, estado, id))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({'Mensagem': 'Produto atualizado com sucesso!'})

@app.route('/produtos/<int:id>', methods=['DELETE'])
def remover_produto(id):
    conn = obter_conexao()
    cur = conn.cursor()
    cur.execute("DELETE FROM produtos WHERE id = %s", (id,))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({'Mensagem': 'Produto deletado com sucesso!'})

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
