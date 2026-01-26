# 📚 BookFlow API

Uma API RESTful moderna, robusta e escalável desenvolvida com **FastAPI** e **Python**. O projeto tem como objetivo o gerenciamento de livros, usuários e autenticação, utilizando as melhores práticas de desenvolvimento, tipagem estática e arquitetura limpa.

---

## 🚀 Tecnologias e Ferramentas

O projeto foi construído utilizando uma stack moderna focada em performance e segurança:

- **[FastAPI](https://fastapi.tiangolo.com/)**: Framework web moderno e de alta performance para construção de APIs.
- **[SQLModel](https://sqlmodel.tiangolo.com/)**: ORM intuitivo que combina SQLAlchemy e Pydantic para interações com o banco de dados.
- **[PostgreSQL](https://www.postgresql.org/)**: Banco de dados relacional robusto (via `asyncpg` para acesso assíncrono).
- **[Alembic](https://alembic.sqlalchemy.org/)**: Ferramenta de migração de banco de dados.
- **[Pydantic](https://docs.pydantic.dev/)**: Validação de dados e gerenciamento de configurações.
- **[Argon2](https://github.com/p-h-c/phc-winner-argon2)**: Algoritmo seguro para hash de senhas.
- **[Ruff](https://docs.astral.sh/ruff/)**: Linter e formatador de código extremamente rápido.
- **[Taskipy](https://github.com/taskipy/taskipy)**: Automação de tarefas e comandos do projeto.

---

## ✨ Funcionalidades (Até o momento)

### 🔐 Autenticação e Usuários
- **Registro de Usuários**: Endpoint seguro para criação de novas contas (`/auth/register`).
- **Segurança**: Senhas criptografadas utilizando Argon2.

### 📖 Gerenciamento de Livros
CRUD completo para recursos bibliográficos:
- **Listar Livros**: Recuperação de todos os livros com suporte a **paginação** (`GET /books`).
- **Detalhes do Livro**: Busca de livro específico por ID (`GET /books/{id}`).
- **Criar Livro**: Adição de novos títulos ao catálogo (`POST /books`).
- **Atualizar Livro**: Atualização parcial de dados do livro (`PATCH /books/{id}`).
- **Remover Livro**: Exclusão de registros (`DELETE /books/{id}`).

---

## 🛠️ Como Executar o Projeto

### Pré-requisitos
- **Python 3.14+**
- **[uv](https://github.com/astral-sh/uv)** (Gerenciador de pacotes recomendado) ou `pip`
- **PostgreSQL** (Rodando localmente ou via Docker)

### 1. Clonar o repositório

```bash
git clone https://github.com/EvandroCalado/BookFlow_API.git
cd BookFlow_API
```

### 2. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com base no exemplo abaixo:

```ini
DATABASE_URL=postgresql+asyncpg://usuario:senha@localhost:5432/bookflow_db
```

### 3. Instalar Dependências

Utilizando o **uv** (recomendado):
```bash
uv sync
```

Ou utilizando `pip` tradicional:
```bash
pip install -e .
```

### 4. Executar Migrações do Banco de Dados

Aplique as migrações para criar as tabelas necessárias no banco:

```bash
alembic upgrade head
```

### 5. Rodar a Aplicação

Utilize o comando configurado via `taskipy`:

```bash
task dev
```

> 💡 Alternativamente, você pode rodar diretamente com o FastAPI CLI:
> `fastapi dev src/main.py --reload-dir src`

A API estará disponível em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📚 Documentação da API

O FastAPI gera automaticamente documentação interativa. Após rodar o projeto, acesse:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) - Teste os endpoints diretamente pelo navegador.
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) - Documentação alternativa e elegante.

---

## 📂 Estrutura do Projeto

```
BookFlow_API/
├── src/
│   ├── auth/          # Módulo de Autenticação (Rotas, Schemas, Serviços)
│   ├── books/         # Módulo de Livros (CRUD completo)
│   ├── db/            # Configurações do Banco de Dados
│   └── main.py        # Entrypoint da aplicação
├── migrations/        # Scripts de migração do Alembic
├── alembic.ini        # Configuração do Alembic
├── pyproject.toml     # Dependências e Configurações de Ferramentas
└── README.md          # Documentação do Projeto
```

---

*Desenvolvido com 💙 por [Evandro Calado]*
