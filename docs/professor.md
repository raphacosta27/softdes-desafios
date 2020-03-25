# Guia do professor


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


## Adicionar um novo desafio

1) Execute o sqlite3 com o arquivo do database

```bash
$ sqlite3 quiz.db
```

2) Execute a query para inserir o Quiz no banco de dados

Lembre-se de substituir as informações do Quiz abaixo pelas informações reais

```bash
sqlite> Insert into QUIZ(numb, release, expire, problem, tests, results, diagnosis) values (1, '2018-08-01','2020-12-31 23:59:59','Exemplo de problema','[[1],[2],[3]]','[0, 0, 0]','["a","b","c"]');
```
Onde,


* numb: Número de identificação do desafio

* release: Data de início 

* expire: Data limite para resolução do desafio

* problem: Descrição do problema

* tests: Testes aplicados as soluçõs enviados

* results: Resultado esperado para a solução

* diagnosis: Diagnóstico dado a tentativa

## Página Inicial
Veja a página [inicial](index.md) para mais detalhes.

## Guia do aluno
Veja a página [guia do aluno](aluno.md) para mais detalhes. 

## Guia de desenvolvimento
Veja a página [guia do desenvolvimento](desenvolvimento.md) para mais detalhes.

## Documentação da API
Veja a página [API](api.md) para mais detalhes.