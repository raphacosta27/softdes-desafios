# Guia de desenvolvimento

## Instalação de dependências

1) Dependências do Python
```bash
$ pip install flask
$ pip install flask_httpauth
```

2) sqlite3
Ubuntu:
```bash
$ sudo apt-get install sqlite3 libsqlite3-dev
```
Mac:

O pacote já vem instalado no sistema por padrão.

Windows:

Faça o download do executável nesse link: https://www.sqlite.org/download.html

## Configuração do banco de dados:

```bash
$ sqlite3 quiz.db < quiz.sql
```

## Criar um usuário

1) Criar arquivo _users.csv_.

```bash
$ touch users.csv
```
O arquivo users.csv é o responsável por controlar quais usuários estão cadastrados
na plataforma. Assim, todos os usuários que adicionar neste arquivo, serão logins
possíveis.

2) Adicionar o(s) usuário(s) no arquivo.

```text
usuário1, senha
usuário2, senha
.
.
.
```

3) Executar o arquivo _add_user.py_.

```bash
$ python3 add_user.py
```
O programa add_users é responsável por efetivamente adicionar ao database de login os usuários
do arquivo users.csv.


## Executando o arquivo principal
```bash
$ python softdes.py
```

## Estrutura do código em alto nível
* É um sistema web desenvolvido em python com a biblioteca flask.
* Usa banco de dados sql com o framework do sqlite3
* Possui autenticação feita com HTTPBasicAuth (do próprio flask)

Endpoints
* / (endpoint que mostra a página principal da aplicação)
* /pass  (endpoint para trocar a senha)
* /logout (endpoint para sair da conta)