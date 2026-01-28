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
- **[PyJWT](https://pyjwt.readthedocs.io/)**: Implementação de tokens JWT para autenticação segura.
- **[Ruff](https://docs.astral.sh/ruff/)**: Linter e formatador de código extremamente rápido.
- **[Taskipy](https://github.com/taskipy/taskipy)**: Automação de tarefas e comandos do projeto.

---

## ✨ Funcionalidades (Até o momento)

### 🔐 Autenticação e Usuários
- **Registro de Usuários**: Endpoint seguro para criação de novas contas (`POST /auth/register`).
- **Login com OAuth2**: Autenticação de usuários utilizando **OAuth2 Password Flow** com JWT (JSON Web Tokens) (`POST /auth/login`).
  - Suporte ao padrão OAuth2 com `username` e `password` via formulário
  - Retorna `access_token` e `token_type` para autenticação subsequente
- **Perfil do Usuário**: Endpoint protegido para recuperar informações do usuário autenticado (`GET /auth/me`).
- **Segurança Avançada**: 
  - Senhas criptografadas utilizando **Argon2** (algoritmo vencedor do Password Hashing Competition)
  - Tokens JWT com expiração configurável e validação robusta
  - Rotas protegidas por autenticação Bearer Token
  - Tratamento de tokens expirados e inválidos com mensagens de erro apropriadas

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
# Database
DATABASE_URL=postgresql+asyncpg://usuario:senha@localhost:5432/bookflow_db

# JWT Authentication
JWT_SECRET_KEY=sua_chave_secreta_super_segura_aqui_mude_em_producao
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=15
REFRESH_TOKEN_EXPIRE_DAYS=30
```

> ⚠️ **Importante**: Em produção, use uma chave secreta forte e única. Você pode gerar uma com:
> ```bash
> python -c "import secrets; print(secrets.token_urlsafe(32))"
> ```

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

### 🔑 Como Testar a Autenticação

#### 1. Registrar um novo usuário
```bash
curl -X POST "http://127.0.0.1:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "João Silva",
    "email": "joao@example.com",
    "password": "senha_segura123"
  }'
```

#### 2. Fazer Login (OAuth2 Password Flow)
```bash
curl -X POST "http://127.0.0.1:8000/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=joao@example.com&password=senha_segura123"
```

Resposta:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

#### 3. Acessar Rota Protegida (Perfil do Usuário)
```bash
curl -X GET "http://127.0.0.1:8000/auth/me" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI"
```

> 💡 **Dica**: No Swagger UI ([/docs](http://127.0.0.1:8000/docs)), clique no botão **"Authorize"** 🔓 no topo da página, insira suas credenciais e todos os endpoints protegidos serão automaticamente autenticados!

---

## 📂 Estrutura do Projeto

```
BookFlow_API/
├── src/
│   ├── auth/          # Módulo de Autenticação
│   │   ├── routers.py     # Endpoints (register, login, me)
│   │   ├── schemas.py     # Modelos Pydantic para validação
│   │   ├── services.py    # Lógica de negócio de autenticação
│   │   ├── models.py      # Modelo SQLModel do usuário
│   │   ├── utils.py       # Funções auxiliares (hash, JWT, OAuth2)
│   │   └── deps.py        # Dependências do FastAPI
│   ├── books/         # Módulo de Livros (CRUD completo)
│   ├── db/            # Configurações do Banco de Dados
│   │   ├── config.py      # Configurações e variáveis de ambiente
│   │   └── session.py     # Gerenciamento de sessões do banco
│   └── main.py        # Entrypoint da aplicação
├── migrations/        # Scripts de migração do Alembic
├── alembic.ini        # Configuração do Alembic
├── pyproject.toml     # Dependências e Configurações de Ferramentas
└── README.md          # Documentação do Projeto
```

---

*Desenvolvido com 💙 por [Evandro Calado]*
