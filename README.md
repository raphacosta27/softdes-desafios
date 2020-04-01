# softdes-desafios
Documentação Servidor de Desafios

# Rodando os testes

## UX tests
Para o testes de UX, é utilizada a biblioteca selenium. Instale-a via pip.

```bash
$ pip install selenium
```

Os drivers de browsers disponíveis são para computadores Mac nas seguintes versões:
* Chrome v80
* Firefox v≥60

Antes de executar o arquivo é necessário alterar as 4 variáveis do início do arquivo main.py.
A variável <code>username</code> e <code>passwd</code> correspondem ao seu usuário e senha cadastrados,
respectivamente. As váriaveis <code>path_to_desafio1</code> e <code>path_to_desafio2</code> são para 
os arquivos desafio1.py e desafio2.py localizadados na pasta /test. O selenium exige o path completo para 
esses arquivos.

Após modificar estas variáveis, para executar:
```bash
$ python3 main.py --browser chrome
```
ou 
```bash
$ python3 main.py --browser firefox
```

## Unit tests
Para realizar os testes da função lambda_handler, utilize o pytest. Para instalar: 
```bash
$ pip install pytest
```
Para executar: 
```bash
$ pytest lambda_tests.py
```