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
