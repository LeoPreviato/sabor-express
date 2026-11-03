# Sabor Express - Sistema de Gerenciamento de Restaurantes
 
## 📖 Sobre
Este programa é um sistema de linha de comando (CLI) para gerenciamento de restaurantes. A ideia parte de um cenário prático: um sistema que permite cadastrar, listar, ativar/desativar e excluir restaurantes, com os dados persistidos em um banco de dados SQLite e uma interface de terminal estilizada.

O projeto começou usando MySQL e depois foi migrado para SQLite, o que eliminou a necessidade de instalar e configurar um servidor de banco de dados: o banco agora é um arquivo local criado automaticamente na primeira execução.
 
## 🚀 Funcionalidades
- Cadastra um novo restaurante (nome e categoria).
- Lista todos os restaurantes cadastrados em uma tabela estilizada.
- Alterna o estado de um restaurante entre ativado e desativado.
- Exclui um restaurante, com etapa de confirmação antes da remoção.
- Persiste todos os dados em um banco de dados SQLite, criado automaticamente ao iniciar o programa.
- Exibe menus, tabelas e mensagens com cores e painéis no terminal.
## 🛠️ Tecnologias utilizadas
- Python 3
- SQLite (módulo nativo `sqlite3`)
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
5. Execute o programa:
```bash
python main.py
```

Na primeira execução, o arquivo `sabor_express.db` é criado automaticamente na raiz do projeto, junto com as tabelas. Não é preciso configurar nenhum banco de dados.
 
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
 
## 🔜 Próximos passos
- Desenvolver um bot para os pratos dos restaurantes, usando a tabela `pratos` que já existe no banco de dados (cada prato ligado a um restaurante, com nome, preço e descrição).

## 📚 Aprendizados
Neste projeto pratiquei:
- Organização de um projeto Python em módulos com responsabilidades separadas.
- Resolução de imports circulares entre arquivos.
- Conexão e persistência de dados com SQLite usando o módulo nativo `sqlite3`.
- Migração de um banco MySQL para SQLite, adaptando tipos de dados e queries.
- Criação automática das tabelas com `CREATE TABLE IF NOT EXISTS`.
- Relacionamento entre tabelas com chave estrangeira e `ON DELETE CASCADE` (ativado com `PRAGMA foreign_keys = ON`).
- Prevenção de SQL Injection com queries parametrizadas (placeholders).
- Controle de transações no banco de dados com `commit()`.
- Estilização de interface de terminal com a biblioteca `rich` (painéis, tabelas e texto colorido).
- Boas práticas de commits atômicos seguindo Conventional Commits.
---