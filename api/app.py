from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)


def ConnectorMysql():

    config = {
            'user': 'root',
            'password': 'root',
            'host': os.environ["HOST"],
            'port': '3306',
            'database': 'employees'
        }

    mydb = mysql.connector.connect(**config)
    return mydb


def read_users():
    connection = ConnectorMysql()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM USERS')
    results = cursor.fetchall()
    cursor.close()
    connection.close()

    return results

def read_user(name):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM USERS WHERE name='{}'; ".format(name)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    if len(myresult) > 0: 
        for x in myresult:
            arr = {
                "uid" : x[0],
                "name" : x[1],
                "age" : int(x[2])
                }
    return arr
    
def insert_data(name  , age):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "INSERT INTO USERS (uid, name,age) VALUES (0, %s , %s)"
    val = (name , age)
    mycursor.execute(sql,val)
    mydb.commit()
    mycursor.close()
    mydb.close()

@app.route('/')
def index():
    return "Index!"

@app.route('/read/all', methods=['GET'])
def readall():
    return jsonify({'User Data': read_users()})

@app.route('/read/<name>', methods=['GET'])
def read(name):
    jsonData = read_user(name)
    return jsonify(jsonData)

@app.route('/insert/<name>/<age>' , methods=['GET'])
def insert(name, age):

    insert_data(name, age)
    return jsonify({'message' : "success"})


if __name__ == '__main__':
    app.run()