# Wedding Pass 💍

(Projeto em desenvolvimento)

Sistema de gestão de convidados para casamentos, desenvolvido em **Python/Flask** com arquitetura em camadas, como projeto de estudo em Full Stack Development.

## ✨ Funcionalidades

- Cadastro e gerenciamento de convidados
- Controle de mesas com validação de capacidade
- Check-in e checkout de convidados no evento (com timestamps)
- Autenticação de usuários (login por sessão)
- Controle de acesso baseado em papéis (admin / cerimonialista)
- Filtro de status na listagem de convidados

## 🛠️ Tecnologias

- **Python 3** + **Flask**
- **MySQL** (via `mysql-connector-python`, dictionary cursors)
- **Jinja2** (templates)
- **Bootstrap** (interface)
- **bcrypt** (hash de senhas)


## 🏗️ Arquitetura

O projeto segue uma arquitetura em camadas, cada uma com responsabilidade única:

```
Database → Config → Validators → Repositories → Services → Routes
```

- **Validators**: validação de dados de entrada
- **Repositories**: acesso e persistência de dados
- **Services**: regras de negócio (retorno padronizado `data, errors, status_code`)
- **Routes**: endpoints HTTP e renderização de templates

## 🚀 Como executar

```bash
# Clone o repositório
git clone <url-do-repositorio>
cd wedding-pass

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente (banco de dados, secret key, etc.)
cp .env.example .env

# Execute a aplicação
flask run
```

## 📌 Status do projeto

Em desenvolvimento — projeto acadêmico com foco em backend robusto e integração full-stack.

## 📄 Licença

Projeto de estudo, sem licença comercial definida.
