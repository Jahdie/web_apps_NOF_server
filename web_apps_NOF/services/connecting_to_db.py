import pypyodbc
import datetime

def db_connector(server, user, password, db_table_name, db_field_name, date_selected, database, hour_start,
                 hour_end, request_to_db):

    value = ''

    server = server
    user = user
    password = password
    database = database
    request_to_db = request_to_db

    connection = pypyodbc.connect(driver='{Sql Server}', server=server, uid=user, pwd=password,
                                  database=database)
    # print(request_to_db)

    # print(request_to_db)
    # request_to_db = "{call GetWorkShiftHourData('Ni5_5', '08-12-2021', '1')}"
    # print(request_to_db)
    # print(server, user, password, database)
    cursor = connection.cursor()
    cursor.execute(request_to_db)

    while 1:
        row = cursor.fetchone()
        if not row:
            break
        # print(row)
        value = row[0]
        if isinstance(value, float):
            value = round(value, 2)
            if value % 1 == 0:
                # print(value)
                value = int(value)
    cursor.close()
    connection.close()
    # print(value, request_to_db)
    return value
