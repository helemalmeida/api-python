# 🐍 API de Produtos com Flask e PostgreSQL

Este projeto é uma API REST simples desenvolvida em Python utilizando o microframework Flask. Os dados são armazenados em um banco de dados PostgreSQL, e a API permite realizar operações CRUD (Create, Read, Update, Delete) sobre uma tabela de produtos.

---

## 📋 Requisitos

### 💾 Pré-requisitos instalados:

* [Python 3.10+](https://www.python.org/downloads/)
* [PostgreSQL](https://www.postgresql.org/download/)
* [Postman (para testar a API)](https://www.postman.com/downloads/)
* `pip` (gerenciador de pacotes do Python)

---

## 📦 Instalações necessárias

No terminal (dentro da pasta do projeto), execute:

```bash
pip install -r requirements.txt
```

Ou, se preferir, instale manualmente:

```bash
pip install flask psycopg2-binary python-dotenv
```

---

## 🛠️ Configuração

1. **Crie um arquivo `.env` na raiz do projeto**, com base no `exemplo.env` incluído:

```
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
DB_NAME=nome_do_banco
```

2. **Configure o banco de dados PostgreSQL:**

Você deve ter um banco chamado, por exemplo, `dados` com a seguinte tabela:

```sql
CREATE TABLE produtos (
  id SERIAL PRIMARY KEY,
  descricao VARCHAR(255),
  estado VARCHAR(50)
);
```

---

## 🚀 Como executar a API

No terminal:

```bash
python app.py
```

A API estará disponível em:

```
http://localhost:5000
```

---

## 🔍 Rotas disponíveis

| Método | Rota             | Descrição                     |
| ------ | ---------------- | ----------------------------- |
| GET    | `/produtos`      | Lista todos os produtos       |
| GET    | `/produtos/<id>` | Retorna produto pelo ID       |
| POST   | `/produtos`      | Adiciona um novo produto      |
| PUT    | `/produtos/<id>` | Atualiza um produto existente |
| DELETE | `/produtos/<id>` | Deleta um produto             |

---

## 💡 Testando no Postman

* Use o método desejado (GET, POST, PUT, DELETE).
* Para POST e PUT, use o **Body → raw → JSON**, com `Content-Type: application/json`.

Exemplo de JSON para POST/PUT:

```json
{
  "descricao": "Kiwi",
  "estado": "Bom"
}
```

---

## ✅ Boas práticas

* O arquivo `.env` **NÃO DEVE ser versionado** (adicione `.env` ao seu `.gitignore`).
* Versione apenas o `exemplo.env` para servir de modelo.

---

## 📄 

Este projeto foi desenvolvido para servir como base para algo mais complexo. 
