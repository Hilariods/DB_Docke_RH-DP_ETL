## Projeto Básico de Banco de Dados para RH e DP com ETL usando Docker

### Descrição

Este projeto configura um pipeline de ETL (Extração, Transformação e Carga) para disponibilizar dados de uma aplicação Sankhya W para análise por cientistas de dados. Utilizaremos PostgreSQL para armazenar os dados extraídos e Python para realizar o processo ETL.

## Ferramentas Utilizadas

- **Docker**: Para criar e gerenciar contêineres.
- **Docker Compose**: Para definir e executar aplicativos multi-contêiner Docker.
- **PostgreSQL**: Banco de dados relacional para armazenar os dados.
- **Python**: Linguagem de programação usada para o processo ETL.
  - **psycopg2**: Biblioteca Python para conectar ao PostgreSQL.
  - **pandas**: Biblioteca Python para manipulação de dados.
  - **sqlalchemy**: Toolkit SQL e ORM para Python.

## Estrutura do Banco de Dados

### Tabelas

- **departments**: tabela de departamentos, com colunas `id`, `nome`.
- **employees**: tabela de funcionários, com colunas `id`, `nome`, `email`, `cargo`, `department_id`.
- **salaries**: tabela de salários, com colunas `employee_id`, `salario`, `data_inicio`.

## Configuração

### Pré-requisitos

- Docker e Docker Compose instalados no sistema.
- Python 3.7+ instalado no sistema.

### Passos

1. Clone este repositório e navegue até a pasta raiz.
   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
