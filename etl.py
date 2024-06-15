import psycopg2
import pandas as pd
from sqlalchemy import create_engine

# Conexão com o banco de dados PostgreSQL
engine = create_engine('postgresql://seu_usuario:sua_senha@db:5432/seu_banco_de_dados')
conn = engine.connect()

# Extração de dados de Sankhya W (exemplo fictício)
# Aqui você substituiria por uma chamada à API do Sankhya W ou leitura de arquivos exportados do Sankhya W
data = {
    'departments': [
        {'id': 1, 'nome': 'Recursos Humanos'},
        {'id': 2, 'nome': 'Desenvolvimento'},
        {'id': 3, 'nome': 'Marketing'},
        {'id': 4, 'nome': 'Vendas'},
        {'id': 5, 'nome': 'Financeiro'}
    ],
    'employees': [
        {'id': 1, 'nome': 'John Doe', 'email': 'john.doe@example.com', 'cargo': 'Software Engineer', 'department_id': 2},
        {'id': 2, 'nome': 'Jane Smith', 'email': 'jane.smith@example.com', 'cargo': 'Product Manager', 'department_id': 2},
        {'id': 3, 'nome': 'Alice Johnson', 'email': 'alice.johnson@example.com', 'cargo': 'Designer', 'department_id': 3},
        {'id': 4, 'nome': 'Bob Brown', 'email': 'bob.brown@example.com', 'cargo': 'Developer', 'department_id': 2},
        {'id': 5, 'nome': 'Carol White', 'email': 'carol.white@example.com', 'cargo': 'HR Manager', 'department_id': 1},
        {'id': 6, 'nome': 'Dave Black', 'email': 'dave.black@example.com', 'cargo': 'Sales Manager', 'department_id': 4},
        {'id': 7, 'nome': 'Eva Green', 'email': 'eva.green@example.com', 'cargo': 'Finance Analyst', 'department_id': 5},
        {'id': 8, 'nome': 'Frank Blue', 'email': 'frank.blue@example.com', 'cargo': 'Marketing Specialist', 'department_id': 3},
        {'id': 9, 'nome': 'Grace Yellow', 'email': 'grace.yellow@example.com', 'cargo': 'HR Assistant', 'department_id': 1},
        {'id': 10, 'nome': 'Hank Red', 'email': 'hank.red@example.com', 'cargo': 'Accountant', 'department_id': 5}
    ],
    'salaries': [
        {'employee_id': 1, 'salario': 6000.00, 'data_inicio': '2023-01-01'},
        {'employee_id': 2, 'salario': 7000.00, 'data_inicio': '2023-01-01'},
        {'employee_id': 3, 'salario': 5000.00, 'data_inicio': '2023-01-01'},
        {'employee_id': 4, 'salario': 6500.00, 'data_inicio': '2023-01-01'},
        {'employee_id': 5, 'salario': 8000.00, 'data_inicio': '2023-01-01'},
        {'employee_id': 6, 'salario': 5500.00, 'data_inicio': '2023-01-01'},
        {'employee_id': 7, 'salario': 7200.00, 'data_inicio': '2023-01-01'},
        {'employee_id': 8, 'salario': 4800.00, 'data_inicio': '2023-01-01'},
        {'employee_id': 9, 'salario': 4500.00, 'data_inicio': '2023-01-01'},
        {'employee_id': 10, 'salario': 6500.00, 'data_inicio': '2023-01-01'}
    ]
}

# Transformação dos dados (exemplo fictício)
df_departments = pd.DataFrame(data['departments'])
df_employees = pd.DataFrame(data['employees'])
df_salaries = pd.DataFrame(data['salaries'])

# Carga dos dados no banco de dados PostgreSQL
df_departments.to_sql('departments', con=conn, if_exists='append', index=False)
df_employees.to_sql('employees', con=conn, if_exists='append', index=False)
df_salaries.to_sql('salaries', con=conn, if_exists='append', index=False)

conn.close()