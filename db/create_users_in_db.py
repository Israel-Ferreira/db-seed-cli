import psycopg2


def create_insert_query(user):
    return f"""
        INSERT INTO tb_users (first_name, last_name, email) 
        VALUES ('{user.first_name}', '{user.last_name}', '{user.email}') 
    """


def insert_users_in_db(users, db_conn_dict):
    conn =  psycopg2.connect(**db_conn_dict)

    try:
        for user in users:
            with conn.cursor() as cursor:
                query =  create_insert_query(user)
                cursor.execute(query)

                conn.commit()

    except Exception as e:
        print(e)

    finally:
        conn.close
