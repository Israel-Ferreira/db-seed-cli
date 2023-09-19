from utils import create_fake_users
from db import create_users_table, insert_users_in_db, drop_users

def popular_banco(conn_dict):

    users = create_fake_users()

    create_users_table(conn_dict)
    insert_users_in_db(users, conn_dict)
    


if __name__ == "__main__":
    print("Teste Aplicação de Linha de comando")

    conn_dict =  {
        "dbname": "users",
        "port": "5432",
        "password": "admin",
        "user": "admin",
        "host": "localhost"
    }
    

    user_input = int(input("Selecione uma opção: \n1- Criar e Popular o banco de dados\n2- Deletar os dados e a tabela\n"))

    if user_input == 1:
        popular_banco(conn_dict)
    else:
        print("Deletando os dados")
        drop_users(conn_dict)
        
    
    