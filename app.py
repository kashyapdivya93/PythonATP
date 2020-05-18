import cx_Oracle
import flask
import json
from flask import render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True

password = 'ABKK_tt_33ABKG_tt_33'
username = 'admin'

connection = cx_Oracle.connect(username,password,'devops_high')
connection.autocommit = True
cur = connection.cursor()

@app.route('/test_flask', methods=['GET'])
def test_flask():
    result_array = []
    query_all = """select * from devops"""
    cur.execute(query_all)
    result = cur.fetchall()
    for i in result:
        dict_object = {'key':None}
        dict_object['key']=i
        result_array.append(dict_object)
        print i

    return json.dumps(dict_object)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
