import psycopg2

def drop_users(conn_params: dict):

    try:
        with psycopg2.connect(**conn_params) as conn:
            delete_without_where_query = "DELETE FROM tb_users"

            with conn.cursor() as cursor:
                cursor.execute(delete_without_where_query)

            conn.commit()

    except Exception as e:
        print(e)

    
