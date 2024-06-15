## Documentação para GitHub

### Projeto Básico de Banco de Dados para RH e DP com ETL usando Docker

#### Descrição

Este projeto configura um pipeline de ETL (Extração, Transformação e Carga) para disponibilizar dados de uma aplicação Sankhya W para análise por cientistas de dados. Utilizaremos PostgreSQL para armazenar os dados extraídos e Python para realizar o processo ETL.

#### Ferramentas Utilizadas

- **Docker**: Para criar e gerenciar contêineres.
- **Docker Compose**: Para definir e executar aplicativos multi-contêiner Docker.
- **PostgreSQL**: Banco de dados relacional para armazenar os dados.
- **Python**: Linguagem de programação usada para o processo ETL.
  - **psycopg2**: Biblioteca Python para conectar ao PostgreSQL.
  - **pandas**: Biblioteca Python para manipulação de dados.
  - **sqlalchemy**: Toolkit SQL e ORM para Python.

### Estrutura do Banco de Dados

#### Tabelas

- **departments**: tabela de departamentos, com colunas `id`, `nome`.
- **employees**: tabela de funcionários, com colunas `id`, `nome`, `email`, `cargo`, `department_id`.
- **salaries**: tabela de salários, com colunas `employee_id`, `salario`, `data_inicio`.

### Configuração

#### Pré-requisitos

- Docker e Docker Compose instalados no sistema.
- Python 3.7+ instalado no sistema.

#### Passos

1. Clone este repositório e navegue até a pasta raiz.
   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Crie os seguintes arquivos na pasta raiz do projeto:
   - `Dockerfile`
   - `docker-compose.yml`
   - `init.sql`
   - `etl.py`

#### Arquivo Dockerfile

```dockerfile
FROM postgres:13

ENV POSTGRES_USER=igor_hilario
ENV POSTGRES_PASSWORD=123
ENV POSTGRES_DB=seu_banco_de_dados

EXPOSE 5432

CMD ["postgres"]
```

#### Arquivo docker-compose.yml

```yaml
version: '3'

services:
  db:
    build: .
    environment:
      - POSTGRES_USER=igor_hilario
      - POSTGRES_PASSWORD=123
      - POSTGRES_DB=seu_banco_de_dados
    ports:
      - "5432:5432"
    volumes:
      - db-data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD", "pg_isready", "-U", "igor_hilario"]
      interval: 30s
      timeout: 30s
      retries: 3

volumes:
  db-data:
```

#### Arquivo init.sql

```sql
CREATE TABLE departments (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    cargo VARCHAR(50) NOT NULL,
    department_id INTEGER REFERENCES departments (id)
);

CREATE TABLE salaries (
    employee_id INTEGER REFERENCES employees (id),
    salario DECIMAL(10, 2) NOT NULL,
    data_inicio DATE NOT NULL,
    PRIMARY KEY (employee_id, data_inicio)
);
```

#### Arquivo etl.py

```python
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

# Conectar ao PostgreSQL
connection = psycopg2.connect(
    user="igor_hilario",
    password="123",
    host="localhost",
    port="5432",
    database="seu_banco_de_dados"
)

# Função para carregar dados
def load_data():
    # Exemplo de extração de dados
    query = "SELECT * FROM employees;"
    df = pd.read_sql(query, connection)

    # Transformações (se necessário)
    df['nome'] = df['nome'].str.upper()

    # Salvar os dados transformados em um novo local (exemplo)
    df.to_csv('employees_transformed.csv', index=False)

    print("ETL process completed successfully.")

if __name__ == "__main__":
    load_data()

# Fechar a conexão
connection.close()
```

#### Arquivo test_connection.py

```python
import psycopg2

connection = None

try:
    connection = psycopg2.connect(
        user="igor_hilario",
        password="123",
        host="localhost",
        port="5432",
        database="seu_banco_de_dados"
    )
    print("Conexão bem-sucedida!")
except psycopg2.Error as e:
    print("Erro ao conectar:", e)
finally:
    if connection:
        connection.close()
```

### Deploy

Para iniciar o banco de dados e configurar o ambiente

1. Construa e inicie os contêineres com Docker Compose:
   ```sh
   docker-compose up -d
   ```

2. Execute o script de conexão para testar a conexão com o banco de dados:
   ```sh
   python test_connection.py
   ```

3. Execute o script ETL para realizar a extração, transformação e carga dos dados:
   ```sh
   python etl.py
   ```

### Observações

- Certifique-se de que o Docker esteja instalado e configurado corretamente em seu sistema.
- Certifique-se de que as bibliotecas Python necessárias estão instaladas:
  ```sh
  pip install psycopg2 pandas sqlalchemy
  ```

### Licença

Licenciado para Igor Hilário. Este projeto é de código aberto e pode ser utilizado conforme os termos da licença MIT.