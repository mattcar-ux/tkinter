from mysql.connector import Error, connect

def delete_DATABASE(database_nome):
    query_delete_db = f"DROP DATABASE {database_nome}"
    try: 
        with connect(
            host = "localhost",
            user = "phpmyadmin",
            password = "ENAIP"
        ) as connection:

            #DELETE DATABASE
            with connection.cursor() as cursor:
                cursor.execute(query_delete_db)
    except Error as e:
        print(e)