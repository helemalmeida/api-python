from flask import jsonify

# 1xx - Informativas
def info_100_continue():
    return jsonify({'mensagem': '100 Continue'}), 100

def info_101_switching_protocols():
    return jsonify({'mensagem': '101 Switching Protocols'}), 101

def info_102_processing():
    return jsonify({'mensagem': '102 Processing'}), 102

# 2xx - Sucesso
def sucesso_200_ok(mensagem="200 OK"):
    return jsonify({'mensagem': mensagem}), 200

def sucesso_201_criado(mensagem="201 Created", dados=None):
    resposta = {'mensagem': mensagem}
    if dados:
        resposta.update(dados)
    return jsonify(resposta), 201

def sucesso_202_aceito():
    return jsonify({'mensagem': '202 Accepted'}), 202

def sucesso_203_nao_autoritativo():
    return jsonify({'mensagem': '203 Non-Authoritative Information'}), 203

def sucesso_204_sem_conteudo():
    return jsonify({'mensagem': '204 No Content'}), 204

def sucesso_205_reset_content():
    return jsonify({'mensagem': '205 Reset Content'}), 205

def sucesso_206_conteudo_parcial():
    return jsonify({'mensagem': '206 Partial Content'}), 206

# 3xx - Redirecionamento
def redirecionamento_300_multiplas_escolhas():
    return jsonify({'mensagem': '300 Multiple Choices'}), 300

def redirecionamento_301_movidopermanentemente():
    return jsonify({'mensagem': '301 Moved Permanently'}), 301

def redirecionamento_302_encontrado():
    return jsonify({'mensagem': '302 Found'}), 302

def redirecionamento_303_ver_outra():
    return jsonify({'mensagem': '303 See Other'}), 303

def redirecionamento_304_nao_modificado():
    return jsonify({'mensagem': '304 Not Modified'}), 304

def redirecionamento_307_redirecionamento_temporario():
    return jsonify({'mensagem': '307 Temporary Redirect'}), 307

def redirecionamento_308_redirecionamento_permanente():
    return jsonify({'mensagem': '308 Permanent Redirect'}), 308

# 4xx - Erros do Cliente
def erro_400_bad_request(mensagem="Requisição malformada."):
    return jsonify({'erro': '400 Bad Request', 'mensagem': mensagem}), 400

def erro_401_nao_autorizado(mensagem="Usuário não autorizado."):
    return jsonify({'erro': '401 Unauthorized', 'mensagem': mensagem}), 401

def erro_402_pagamento_necessario(mensagem="Pagamento requerido."):
    return jsonify({'erro': '402 Payment Required', 'mensagem': mensagem}), 402

def erro_403_proibido(mensagem="Acesso negado."):
    return jsonify({'erro': '403 Forbidden', 'mensagem': mensagem}), 403

def erro_404_nao_encontrado(mensagem="Recurso não encontrado."):
    return jsonify({'erro': '404 Not Found', 'mensagem': mensagem}), 404

def erro_405_metodo_nao_permitido(mensagem="Método não permitido."):
    return jsonify({'erro': '405 Method Not Allowed', 'mensagem': mensagem}), 405

def erro_406_nao_aceitavel(mensagem="Conteúdo não aceitável."):
    return jsonify({'erro': '406 Not Acceptable', 'mensagem': mensagem}), 406

def erro_407_autenticacao_proxy(mensagem="Autenticação de proxy necessária."):
    return jsonify({'erro': '407 Proxy Authentication Required', 'mensagem': mensagem}), 407

def erro_408_tempo_limite(mensagem="Tempo limite da requisição."):
    return jsonify({'erro': '408 Request Timeout', 'mensagem': mensagem}), 408

def erro_409_conflito(mensagem="Conflito de dados."):
    return jsonify({'erro': '409 Conflict', 'mensagem': mensagem}), 409

def erro_410_gone(mensagem="Recurso não está mais disponível."):
    return jsonify({'erro': '410 Gone', 'mensagem': mensagem}), 410

def erro_411_length_required(mensagem="Length requerido."):
    return jsonify({'erro': '411 Length Required', 'mensagem': mensagem}), 411

def erro_412_precondicao_falhou(mensagem="Pré-condição falhou."):
    return jsonify({'erro': '412 Precondition Failed', 'mensagem': mensagem}), 412

def erro_413_conteudo_grande(mensagem="Conteúdo muito grande."):
    return jsonify({'erro': '413 Payload Too Large', 'mensagem': mensagem}), 413

def erro_414_uri_grande(mensagem="URI muito longa."):
    return jsonify({'erro': '414 URI Too Long', 'mensagem': mensagem}), 414

def erro_415_tipo_midia(mensagem="Tipo de mídia não suportado."):
    return jsonify({'erro': '415 Unsupported Media Type', 'mensagem': mensagem}), 415

def erro_416_intervalo_nao_satisfaz(mensagem="Intervalo requisitado inválido."):
    return jsonify({'erro': '416 Range Not Satisfiable', 'mensagem': mensagem}), 416

def erro_417_expectativa_falhou(mensagem="Expectativa falhou."):
    return jsonify({'erro': '417 Expectation Failed', 'mensagem': mensagem}), 417

def erro_418_sou_uma_chaleira():
    return jsonify({'erro': '418 I\'m a teapot', 'mensagem': 'Sim, isso existe 😄'}), 418

def erro_422_entidade_invalida(mensagem="Entidade não processável."):
    return jsonify({'erro': '422 Unprocessable Entity', 'mensagem': mensagem}), 422

def erro_429_muitas_requisicoes(mensagem="Muitas requisições."):
    return jsonify({'erro': '429 Too Many Requests', 'mensagem': mensagem}), 429

# 5xx - Erros do Servidor
def erro_500_interno(mensagem="Erro interno no servidor."):
    return jsonify({'erro': '500 Internal Server Error', 'mensagem': mensagem}), 500

def erro_501_nao_implementado(mensagem="Funcionalidade não implementada."):
    return jsonify({'erro': '501 Not Implemented', 'mensagem': mensagem}), 501

def erro_502_bad_gateway(mensagem="Gateway inválido."):
    return jsonify({'erro': '502 Bad Gateway', 'mensagem': mensagem}), 502

def erro_503_servico_indisponivel(mensagem="Serviço temporariamente indisponível."):
    return jsonify({'erro': '503 Service Unavailable', 'mensagem': mensagem}), 503

def erro_504_gateway_timeout(mensagem="Tempo de resposta do gateway expirado."):
    return jsonify({'erro': '504 Gateway Timeout', 'mensagem': mensagem}), 504

def erro_505_http_nao_suportado(mensagem="Versão HTTP não suportada."):
    return jsonify({'erro': '505 HTTP Version Not Supported', 'mensagem': mensagem}), 505
