from flask import Flask, jsonify, request
from db import obter_conexao
from erros import (
    info_100_continue, 
    sucesso_200_ok, sucesso_201_criado, 
    redirecionamento_301_movidopermanentemente, 
    erro_400_bad_request, erro_422_entidade_invalida,
    erro_404_nao_encontrado, erro_500_interno
)

app = Flask(__name__)

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    try:
        conn = obter_conexao()
        cur = conn.cursor()
        cur.execute("SELECT id, descricao, estado FROM produtos")
        rows = cur.fetchall()
        cur.close()
        conn.close()

        produtos = [{'id': row[0], 'descricao': row[1], 'estado': row[2]} for row in rows]
        return jsonify(produtos)

    except Exception as e:
        return erro_500_interno(str(e))

@app.route('/produtos/<int:id>', methods=['GET'])
def buscar_produto_por_id(id):
    try:
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
            return erro_404_nao_encontrado("Produto não encontrado.")

    except Exception as e:
        return erro_500_interno(str(e))

@app.route('/produtos', methods=['POST'])
def adicionar_produto():
    try:
        dados = request.get_json()

        if not dados:
            return erro_400_bad_request("Nenhum JSON foi enviado.")

        descricao = dados.get('descricao')
        estado = dados.get('estado')

        if not descricao or not estado:
            return erro_422_entidade_invalida("Campos 'descricao' e 'estado' são obrigatórios.")

        conn = obter_conexao()
        cur = conn.cursor()
        cur.execute("INSERT INTO produtos (descricao, estado) VALUES (%s, %s) RETURNING id", (descricao, estado))
        novo_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()

        return sucesso_201_criado(dados={'id': novo_id, 'descricao': descricao, 'estado': estado})

    except Exception as e:
        return erro_500_interno(str(e))

@app.route('/produtos/<int:id>', methods=['PUT'])
def editar_produto(id):
    try:
        dados = request.get_json()

        if not dados:
            return erro_400_bad_request("Nenhum JSON foi enviado.")

        descricao = dados.get('descricao')
        estado = dados.get('estado')

        if not descricao or not estado:
            return erro_422_entidade_invalida("Campos 'descricao' e 'estado' são obrigatórios.")

        conn = obter_conexao()
        cur = conn.cursor()
        cur.execute("UPDATE produtos SET descricao = %s, estado = %s WHERE id = %s", (descricao, estado, id))

        if cur.rowcount == 0:
            cur.close()
            conn.close()
            return erro_404_nao_encontrado("Produto não encontrado para atualização.")

        conn.commit()
        cur.close()
        conn.close()

        return jsonify({'mensagem': 'Produto atualizado com sucesso!'})

    except Exception as e:
        return erro_500_interno(str(e))

@app.route('/produtos/<int:id>', methods=['DELETE'])
def remover_produto(id):
    try:
        conn = obter_conexao()
        cur = conn.cursor()
        cur.execute("DELETE FROM produtos WHERE id = %s", (id,))

        if cur.rowcount == 0:
            cur.close()
            conn.close()
            return erro_404_nao_encontrado("Produto não encontrado para exclusão.")

        conn.commit()
        cur.close()
        conn.close()

        return jsonify({'mensagem': 'Produto deletado com sucesso!'})

    except Exception as e:
        return erro_500_interno(str(e))

@app.errorhandler(Exception)
def tratar_erro_global(e):
    return erro_500_interno(str(e))

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
