from flask_sqlalchemy import SQLAlchemy

from src.utils.helper_funtions import load_db_config

db = SQLAlchemy()

def create_db_connection():
    content = load_db_config()
    # print("This is db connection function----------",content)

    db_user = content['db_user']
    db_pwd = content["db_pwd"]
    db_host = content['db_host']
    db_port = content['db_port']
    db_name = content['db_name']
    db_connection_string = (
        f"postgresql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}?sslmode=require"
    )

    return db_connection_string


def get_cursor():
    """Return cursor and connection object."""
    print("****************************************Inside: get_cursor***********************.")
    try:
        connection = db.engine.raw_connection()
        cursor = connection.cursor()
        return cursor, connection
    except Exception as e:
        print("Error from get_cursor- db_function", e)


def dict_fetch_all(cursor):
    """Return all rows from a cursor as a dict.

    :param cursor: cursor object
    :return: all rows in a dict format enclosed in a list
    """
    print("Inside dictfetchall.")
    columns = [col[0] for col in cursor.description]

    print("***********************************************",columns)

    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def get_object(query, cursor, param: list = None):
    """Get object based on param list."""
    print("Inside db function: get_object.")
    try:
        if param:
            cursor.execute(query, param)
        else:
            cursor.execute(query)
        obj_dict = dict_fetch_all(cursor)
    except Exception as e:
        print("Error in executing query from get_object-", e)
        obj_dict = []
    print("get_object:{}".format(obj_dict))
    return obj_dict

def dict_fetch_one(cursor):
    """Return single rows from a cursor as a dict.
    :param cursor: cursor object
    :return: single row in a dict format
    """
    print("Inside dict_fetch_one.")
    columns = [col[0] for col in cursor.description]
    data_values = cursor.fetchone()
    if not data_values:
        return {}
    return dict(zip(columns, data_values))
def create_object(query, param: list, cursor):
    """"Create object based on param list."""
    print("Inside db function: create_object.")
    obj_dict = {}
    try:
        cursor.execute(query, param)
        if cursor.description:
            obj_dict = dict_fetch_one(cursor)
        is_created = True
    except Exception as e:
        print("Error in create query-", e)
        is_created = False
    print("create_object:{}".format(is_created))
    return obj_dict, is_created

def update_object(query, param: list, cursor):
    """Update object based on given param."""
    obj_dict = {}
    try:
        print("Inside db function: update_object.")
        cursor.execute(query, param)
        if cursor.description is not None:
            obj_dict = dict_fetch_one(cursor)
        is_updated = True
    except Exception as e:
        print("Error in update query:", e)
        is_updated = False
    print("outside update_object:{}".format(is_updated))
    return obj_dict, is_updated
