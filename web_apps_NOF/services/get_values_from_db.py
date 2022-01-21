import pypyodbc
import disp_svodka.models
from services import connecting_to_db
import random


def get_values_from_db(server, user, password, database, db_table_name, db_field_name, date_selected,
                       tbody, column_start, fields_type_and_request_index_dict):
    # print(tbody)
    tbody_values = []
    i = column_start + 1
    # print(tbody)
    date_selected = date_selected.split('.')
    month_start_date = "'" + '1' + '-' + '-'.join(date_selected[1:]) + "'"
    date_selected = "'" + '-'.join(date_selected) + "'"

    for key, value in tbody.items():

        thead_field_type = key.split('-')[0]
        if disp_svodka.models.RequestsToDB.objects.filter(
                theadfieldtypes__thead_field_name=thead_field_type).exists():
            hour = key.split('-')[1]
            request_to_db = disp_svodka.models.RequestsToDB.objects.get(
                theadfieldtypes__thead_field_name=thead_field_type)
            # print(request_to_db.request_to_db)
            request_to_db_lists_index = fields_type_and_request_index_dict[thead_field_type]
            request_to_db = request_to_db.request_to_db[request_to_db_lists_index]

            if request_to_db.split()[0] == 'call':
                # print(request_to_db)
                db_field_name_temp = "'" + db_field_name + "'"
                hour_temp = "'" + hour + "'"

                request_to_db = request_to_db.format(field_name_of_table=db_field_name_temp,
                                                     current_date=date_selected,
                                                     hour=hour_temp, table_name_db=db_table_name,
                                                     month_start_date=month_start_date)
            else:
                request_to_db = request_to_db.format(field_name_of_table=db_field_name, current_date=date_selected,
                                                     hour=hour, table_name_db=db_table_name,
                                                     month_start_date=month_start_date)

            if request_to_db.split()[0] == 'call':
                request_to_db = "{" + request_to_db + "}"

            value = round(random.uniform(1, 10), 2)
            # print(request_to_db)
            # print(server, user, password, database, db_table_name)
            # print(request_to_db)
            # value = connecting_to_db.db_connector(server=server, user=user, password=password, database=database,
            #                                       db_table_name=db_table_name,
            #                                       db_field_name=db_field_name,
            #                                       date_selected=date_selected, hour_start=key, hour_end=key,
            #                                       request_to_db=request_to_db)

            tbody[key] = value


    # print(table_num, item)
    for key, value in tbody.items():
        tbody_values.append(
            {'field_value': '' if value is None else value, 'rowspan': 1, 'colspan': 1, 'row_start': '',
             'row_end': '',
             'column_start': i, 'column_end': i})
        i += 1


    return tbody_values
