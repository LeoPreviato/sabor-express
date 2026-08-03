# Sabor Express - Sistema de Gerenciamento de Restaurantes
 
## 📖 Sobre
Este programa é um sistema de linha de comando (CLI) para gerenciamento de restaurantes. A ideia parte de um cenário prático: um sistema que permite cadastrar, listar, ativar/desativar e excluir restaurantes, com os dados persistidos em um banco de dados MySQL e uma interface de terminal estilizada.
 
## 🚀 Funcionalidades
- Cadastra um novo restaurante (nome e categoria).
- Lista todos os restaurantes cadastrados em uma tabela estilizada.
- Alterna o estado de um restaurante entre ativado e desativado.
- Exclui um restaurante, com etapa de confirmação antes da remoção.
- Persiste todos os dados em um banco de dados MySQL.
- Exibe menus, tabelas e mensagens com cores e painéis no terminal.
## 🛠️ Tecnologias utilizadas
- Python 3
- MySQL
- `mysql-connector-python`
- `python-dotenv`
- `rich`
## 📂 Estrutura do projeto
```text
sabor-express
├── main.py
├── restaurantes.py
├── utils.py
├── database.py
├── requirements.txt
├── .gitignore
└── README.md
```
 
## ▶️ Como executar
1. Clone este repositório:
```bash
git clone <URL_DO_REPOSITORIO>
```
2. Acesse a pasta do projeto:
```bash
cd sabor-express
```
3. Crie e ative um ambiente virtual:
```bash
python -m venv .venv
source .venv/bin/activate
```
4. Instale as dependências:
```bash
pip install -r requirements.txt
```
5. Crie o banco de dados e a tabela no MySQL:
```sql
CREATE DATABASE sabor_express;
 
USE sabor_express;
 
CREATE TABLE restaurantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) UNIQUE NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    ativo BOOLEAN DEFAULT FALSE
);
```
6. Crie um arquivo `.env` na raiz do projeto com suas credenciais:
```text
DB_HOST=localhost
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_DATABASE=sabor_express
```
7. Execute o programa:
```bash
python main.py
```
 
## 💻 Exemplo de uso
**Menu principal**
```text
1 - Cadastrar Restaurantes
2 - Listar Restaurantes
3 - Alternar estado do Restaurante
4 - Excluir Restaurante
5 - Sair do programa
```
 
**Listagem de restaurantes**
```text
┌────────────────┬────────────┬────────────┐
│ Nome           │ Categoria  │ Status     │
├────────────────┼────────────┼────────────┤
│ Madeiro        │ Lanches    │ Desativado │
│ Pizza Suprema  │ Italiana   │ Ativado    │
└────────────────┴────────────┴────────────┘
```
 
## 📚 Aprendizados
Neste projeto pratiquei:
- Organização de um projeto Python em módulos com responsabilidades separadas.
- Resolução de imports circulares entre arquivos.
- Conexão e persistência de dados com MySQL usando `mysql-connector-python`.
- Uso de variáveis de ambiente (`.env`) para proteger credenciais sensíveis.
- Prevenção de SQL Injection com queries parametrizadas (placeholders).
- Controle de transações no banco de dados com `commit()`.
- Estilização de interface de terminal com a biblioteca `rich` (painéis, tabelas e texto colorido).
- Boas práticas de commits atômicos seguindo Conventional Commits.
---