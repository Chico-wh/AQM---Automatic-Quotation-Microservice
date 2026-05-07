# Fast Quote API

API backend desenvolvida com **FastAPI** para criação automática de cotações comerciais, com autenticação de usuários, cadastro de clientes, serviços, regras dinâmicas de preço e cálculo automático de valores.

O projeto tem como objetivo resolver um problema comum em pequenos negócios e prestadores de serviço: gerar orçamentos de forma rápida, organizada e padronizada, evitando cálculos manuais em planilhas ou mensagens soltas.

---

## Visão Geral

A **Fast Quote API** permite que um usuário autenticado cadastre seus próprios clientes, serviços e regras de preço para gerar cotações automaticamente.

Cada usuário acessa apenas os seus próprios dados, garantindo isolamento básico entre contas.

Exemplo de uso:

- Cadastrar um cliente
- Cadastrar serviços prestados
- Criar regras de preço, como margem, desconto ou taxa fixa
- Gerar uma cotação automática
- Atualizar o status da cotação

---

## Funcionalidades

### Autenticação

- Cadastro de usuário
- Login com e-mail e senha
- Autenticação via JWT
- Rotas protegidas
- Isolamento de dados por usuário

### Clientes

- Criar cliente
- Listar clientes
- Buscar cliente por ID
- Atualizar cliente
- Remover cliente

### Serviços

- Criar serviço
- Listar serviços
- Buscar serviço por ID
- Atualizar serviço
- Desativar serviço

### Regras de Preço

- Criar regras dinâmicas
- Aplicar taxas fixas
- Aplicar descontos
- Aplicar margem percentual
- Definir preço mínimo
- Desativar regras

### Cotações

- Criar cotação
- Adicionar múltiplos serviços à cotação
- Calcular subtotal, taxas, descontos, margem e total
- Listar cotações
- Buscar cotação por ID
- Atualizar status da cotação
- Recalcular cotação

---

## Tecnologias Utilizadas

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Pydantic
- JWT
- Passlib / Bcrypt
- Docker
- Pytest
- Uvicorn

---

## Estrutura do Projeto

```txt
Fast-quote/
│
├── api/
│   └── v1/
│       └── routes/
│           ├── auth.py
│           ├── clients.py
│           ├── services.py
│           ├── pricing_rules.py
│           └── quotes.py
│
├── core/
│   ├── config.py
│   ├── database.py
│   ├── security.py
│   └── create_db.py
│
├── models/
│   ├── user.py
│   ├── client.py
│   ├── service.py
│   ├── pricing_rule.py
│   ├── quote.py
│   └── quote_item.py
│
├── repositories/
│   ├── user_repository.py
│   ├── client_repository.py
│   ├── service_repository.py
│   ├── pricing_rule_repository.py
│   └── quote_repository.py
│
├── schemas/
│   ├── user.py
│   ├── auth.py
│   ├── token.py
│   ├── client.py
│   ├── service.py
│   ├── pricing_rule.py
│   └── quote.py
│
├── services/
│   ├── auth_service.py
│   ├── quote_calculator.py
│   └── quote_service.py
│
├── tests/
│   ├── test_auth.py
│   ├── test_clients.py
│   ├── test_services.py
│   └── test_quotes.py
│
├── utils/
│   └── money.py
│
├── main.py
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
Principais Conceitos do Projeto
Models

Os models representam as tabelas do banco de dados usando SQLAlchemy.

Exemplo:

class User(Base):
    __tablename__ = "users"
Schemas

Os schemas validam dados de entrada e saída da API usando Pydantic.

Exemplo:

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
Repositories

Os repositories concentram operações diretas no banco de dados.

Exemplo:

buscar usuário por e-mail
criar cliente
listar serviços
buscar cotação
Services

Os services concentram regras de negócio.

Exemplo:

autenticar usuário
calcular cotação
aplicar regras de preço
validar posse dos dados pelo usuário autenticado
Regras de Negócio
Isolamento por Usuário

Todos os dados principais pertencem a um usuário autenticado.

User 1:N Client
User 1:N Service
User 1:N PricingRule
User 1:N Quote

O usuário só pode acessar, editar ou excluir registros criados por ele mesmo.

Tipos de Serviço

A API permite diferentes formas de cálculo para serviços:

Tipo	Descrição
fixed	Valor fixo
per_unit	Valor por unidade
per_day	Valor por dia
per_unit_day	Valor por unidade e por dia
per_km	Valor por quilômetro

Exemplos:

fixed:
subtotal = base_price

per_unit:
subtotal = base_price * quantity

per_day:
subtotal = base_price * days

per_unit_day:
subtotal = base_price * quantity * days

per_km:
subtotal = base_price * distance_km
Tipos de Regras de Preço
Regra	Descrição
fixed_fee	Taxa fixa
delivery_fee	Taxa de entrega
discount	Desconto percentual
margin	Margem percentual
urgency_fee	Taxa de urgência
minimum_price	Preço mínimo
Fórmula de Cálculo

A cotação é calculada com base nos itens adicionados e nas regras aplicadas.

subtotal = soma dos subtotais dos itens

fees_total = soma das taxas fixas

margin_total = subtotal * margem_percentual

discount_total = subtotal * desconto_percentual

total = subtotal + fees_total + margin_total - discount_total

Caso exista preço mínimo:

if total < minimum_price:
    total = minimum_price
Exemplo de Cotação

Entrada:

{
  "client_id": 1,
  "items": [
    {
      "service_id": 1,
      "quantity": 20,
      "days": 2
    },
    {
      "service_id": 2,
      "distance_km": "12.00"
    }
  ],
  "pricing_rule_ids": [1, 2]
}

Resultado esperado:

{
  "subtotal": "230.00",
  "fees_total": "40.00",
  "margin_total": "34.50",
  "discount_total": "0.00",
  "total": "304.50"
}
Status da Cotação
Status	Descrição
draft	Cotação em rascunho
calculated	Cotação calculada
sent	Cotação enviada
approved	Cotação aprovada
rejected	Cotação recusada
expired	Cotação expirada

Fluxo sugerido:

draft -> calculated -> sent -> approved
draft -> calculated -> sent -> rejected
draft -> calculated -> sent -> expired
Como Rodar o Projeto
1. Clone o repositório
git clone https://github.com/seu-usuario/fast-quote-api.git
cd fast-quote-api
2. Crie o ambiente virtual
python -m venv .v

Ative o ambiente virtual:

Windows PowerShell
.\.v\Scripts\Activate.ps1
Linux / macOS
source .v/bin/activate
3. Instale as dependências
pip install -r requirements.txt
4. Configure as variáveis de ambiente

Crie um arquivo .env baseado no .env.example.

Exemplo:

APP_NAME=Fast Quote API
ENVIRONMENT=development
DEBUG=true

DATABASE_URL=postgresql://postgres:postgres@localhost:5432/fast_quote_db

SECRET_KEY=change-this-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
5. Suba o banco com Docker
docker compose up -d
6. Crie as tabelas

Enquanto o projeto estiver em fase inicial, é possível criar as tabelas com:

python -m core.create_db

Em uma versão mais avançada, o projeto deve usar Alembic para controlar migrations.

7. Rode a aplicação
uvicorn main:app --reload

A API ficará disponível em:

http://127.0.0.1:8000

Documentação Swagger:

http://127.0.0.1:8000/docs

Documentação ReDoc:

http://127.0.0.1:8000/redoc
Rotas Planejadas
Health Check
GET /api/v1/health
GET /api/v1/health/db
Auth
POST /api/v1/auth/register
POST /api/v1/auth/login
GET /api/v1/auth/me
POST /api/v1/auth/logout
Clients
POST /api/v1/clients
GET /api/v1/clients
GET /api/v1/clients/{client_id}
PUT /api/v1/clients/{client_id}
DELETE /api/v1/clients/{client_id}
Services
POST /api/v1/services
GET /api/v1/services
GET /api/v1/services/{service_id}
PUT /api/v1/services/{service_id}
PATCH /api/v1/services/{service_id}/deactivate
Pricing Rules
POST /api/v1/pricing-rules
GET /api/v1/pricing-rules
GET /api/v1/pricing-rules/{rule_id}
PUT /api/v1/pricing-rules/{rule_id}
PATCH /api/v1/pricing-rules/{rule_id}/deactivate
Quotes
POST /api/v1/quotes
GET /api/v1/quotes
GET /api/v1/quotes/{quote_id}
PATCH /api/v1/quotes/{quote_id}/status
POST /api/v1/quotes/{quote_id}/recalculate
DELETE /api/v1/quotes/{quote_id}
Testes

Para rodar os testes:

pytest

Testes planejados:

Cadastro de usuário
Login
Login com senha incorreta
Criação de cliente autenticado
Bloqueio de rota sem token
Criação de serviço
Criação de regra de preço
Cálculo de cotação
Usuário não pode acessar dados de outro usuário
Usuário não pode usar serviço pertencente a outro usuário
Segurança

Boas práticas aplicadas ou planejadas:

Senhas armazenadas com hash
Autenticação via JWT
Rotas protegidas
Dados isolados por usuário
Validação de entrada com Pydantic
Uso de Decimal para valores financeiros
Variáveis sensíveis fora do código fonte
Próximas Melhorias
Alembic para migrations
Refresh token
Recuperação de senha
Verificação de e-mail
Geração de PDF da cotação
Envio de cotação por e-mail
Link público para aprovação da cotação
Dashboard financeiro
Multiempresa
Controle de permissões por cargo
Histórico de versões da cotação
Objetivo do Projeto

Este projeto foi criado como estudo prático de backend com FastAPI, explorando autenticação, organização de arquitetura, modelagem de banco, regras de negócio, cálculo financeiro e construção de uma API com estrutura próxima de um produto real.

Mais do que apenas um CRUD, a proposta é construir uma API que resolva um problema concreto: automatizar a criação de orçamentos comerciais.

Licença

Este projeto está sob a licença MIT.