CREATE TABLE departments (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50)
);

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50),
    email VARCHAR(100),
    cargo VARCHAR(50),
    department_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES departments (id)
);

CREATE TABLE salaries (
    employee_id INTEGER,
    salario DECIMAL(10, 2),
    data_inicio DATE,
    PRIMARY KEY (employee_id, data_inicio),
    FOREIGN KEY (employee_id) REFERENCES employees (id)
);
