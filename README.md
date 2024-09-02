TaskFlow
========

TaskFlow é uma aplicação de gerenciamento de tarefas que permite aos usuários criar, gerenciar e monitorar tarefas associadas a projetos. Este projeto foi desenvolvido utilizando Python, Poetry e Docker.

Pré-requisitos
--------------

Antes de começar, verifique se você tem os seguintes pré-requisitos instalados:

- [Python 3.10.7 >](https://www.python.org/downloads/)
- [Poetry 1.8.3 >](https://python-poetry.org/docs/#installation)
- [Docker 27.0.3 >](https://docs.docker.com/get-docker/)

Configuração do Ambiente de Desenvolvimento
-------------------------------------------
  O Poetry é usado para gerenciar as dependências do projeto. Instale as dependências executando:
  ```
  poetry install
  ```


Para executar localmente
-------------------------
- Para garantir as migrações mais recentes, utilize:
  ```
  poetry run python manage.py makemigrations
  ```

- Para aplicar as migrações ao banco de dados, utilize:
  ```
  poetry run python manage.py migrate
  ```

- Para iniciar um localhost, utilize:
  ```
  poetry run python manage.py runserver
  ```

Para executar com Docker
------------------------
- Na raiz do projeto, crie um arquivo .env com as variáveis:
  ```
  SQL_DATABASE=nome_do_banco_de_dados
  SQL_USER=user_do_banco_de_dados
  SQL_PASSWORD=senha_do_banco_de_dados
  ```
- Construa a imagem Docker e inicie os contêineres com:
  ```
  docker-compose up -d --build
  ```
  
  As migrações são aplicadas automaticamente e o servidor é iniciado. Mas você pode fazer manualmente com:
  ```
  docker-compose exec web python manage.py migrate
  ```

Comandos em server local e em Docker
------------------------------------
- Para criar um super usuário:
  ```
  poetry run python manage.py createsuperuser
  ```
  ou em Docker:
  ```
  docker-compose exec web python manage.py createsuperuser
  ```

Decisões tomadas
================

- Utilizei o framework Django para um backend mais robusto e já preparado para lidar com requisições e dados.
- No frontend, utilizei a biblioteca Bootstrap para garantir uma estilizição agradável e responsiva. O Django Template Language atuou para inserir uma lógica simples como variáveis, loops, condicionais, etc, combinando o HTML com o lado do servidor dinâmicamente.