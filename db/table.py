import psycopg2



def create_users_table(conn_params):

    command = (
        """
        CREATE TABLE IF NOT EXISTS tb_users (
            id SERIAL NOT NULL PRIMARY KEY,
            first_name VARCHAR(60) NOT NULL,
            last_name VARCHAR(60) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            active boolean NOT NULL DEFAULT TRUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )


    conn = None

    try:
        conn = psycopg2.connect(**conn_params)

        with conn.cursor() as cursor:
            cursor.execute(command)

            conn.commit()

    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
        

