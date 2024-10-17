from flask import request
from flask import (
    jsonify,
    make_response
)
from src.___init__ import app
from src.utils.db_function import get_cursor,get_object, create_object, update_object
import json
from src.utils import constant as settings



@app.route("/home",methods = ['GET'])
def home_detail():
    cursor, connection = get_cursor()
    print("Inside fetch detail function.")
    try:
        if request.method == 'GET':
            query = """ select * from data.home_page_articles """
            home_page_data = get_object(
                query=query,
                cursor=cursor
            )
            # home_page_data = settings.HOME_PAGE_DATA

            return make_response(jsonify(home_page_data))
    except Exception as e:
        print(e)

@app.route("/sports",methods = ['GET'])
def sport_detail():
    cursor, connection = get_cursor()
    print("Inside sport detail function.")
    try:
        if request.method == 'GET':
            query = """ select * from data.sport_page_articles """
            sport_page_data = get_object(
                query=query,
                cursor=cursor
            )
            # sport_page_data = settings.SPORT_PAGE_DATA

            return make_response(jsonify(sport_page_data))
    except Exception as e:
        print(e)


@app.route("/political",methods = ['GET'])
def political_detail():
    cursor, connection = get_cursor()
    print("Inside political detail function.")
    try:
        if request.method == 'GET':
            query = """ select * from data.political_page_articles """
            political_page_data = get_object(
                query=query,
                cursor=cursor
            )
            # political_page_data = settings.POLITICAL_PAGE_DATA

            return make_response(jsonify(political_page_data))
    except Exception as e:
        print(e)

@app.route("/api/get-records",methods = ['GET'])
def get_records_data():
    cursor, connection = get_cursor()
    print("Inside political detail function.")
    try:
        if request.method == 'GET':
            query = """ select * from data.postdata """
            political_page_data = get_object(
                query=query,
                cursor=cursor
            )
            # political_page_data = settings.POLITICAL_PAGE_DATA

            return make_response(jsonify(political_page_data))
    except Exception as e:
        print(e)

@app.route("/api/post-records", methods=['POST'])
def post_records_data():
    cursor, connection = get_cursor()
    print("Inside political detail function.")
    try:
        if request.method == 'POST':
            post_data = request.get_data()
            post_data = json.loads(post_data)  # Decode and parse JSON
            author_data = post_data.get('req')
            author = author_data["author"]
            name = author_data["name"]

            query = """ 
                INSERT INTO data.postdata (name, author)
                VALUES (%s, %s)
            """.format(name,author)
            # params = [name, author]

            obj_object = create_object(query=query, param=[name,author], cursor=cursor)

            political_page_data = {"message": "Data inserted successfully"}
            connection.commit()
            return make_response(jsonify(political_page_data))
    except Exception as e:
        print(e)
        return make_response(jsonify({"error": str(e)}), 500)



@app.route("/api/put-records/<int:id>", methods=['PUT'])
def put_records_data(id):
    cursor, connection = get_cursor()
    try:
        if request.method == 'PUT':
            post_data = request.get_data()
            post_data = json.loads(post_data)  # Decode and parse JSON
            author_data = post_data.get('req')
            author = author_data["author"]
            name = author_data["name"]

            query = """ 
                UPDATE data.postdata
                SET name = %s,
                    author = %s
                WHERE id = %s
            """
            cursor.execute(query, [name, author, id])
            connection.commit()

            response_data = {"message": "Data updated successfully"}
            return make_response(jsonify(response_data))
    except Exception as e:
        print(e)
        return make_response(jsonify({"error": str(e)}), 500)


@app.route("/api/delete-records/<int:id>", methods=['DELETE'])
def delete_records_data(id):
    cursor, connection = get_cursor()
    try:
        if request.method == 'DELETE':
            query = "DELETE FROM data.postdata WHERE id = %s"
            cursor.execute(query, [id])
            connection.commit()

            response_data = {"message": "Data deleted successfully"}
            return make_response(jsonify(response_data))
    except Exception as e:
        print(e)
        return make_response(jsonify({"error": str(e)}), 500)
