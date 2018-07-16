from flask import Flask, request
from flask_cors import CORS

import base64
import requests
import util
import json
import os

app = Flask(__name__)
CORS(app)

hbase_base_url = os.environ.get('HBASE_BASE_URL','http://localhost:4200')
app_port = int(os.environ.get('APP_PORT',3004))

@app.route("/ping", methods=['GET'])
def ping():
    return "pong"

@app.route("/<tablename>/<row>", methods=['GET'])
def table_rows(tablename, row):
    response = requests.get(hbase_base_url + request.full_path, headers={"Accept" : "application/json"})
    
    rows = list()
    if not util.is_successful(response):
        print("not successful\n")
        return json.dumps(rows)
    
    response_text = json.loads(response.text)
    for row in response_text['Row']:        
        row_key = base64.b64decode(row['key'])
        dataset = dict()
        dataset["key"]=row_key
        for cell in row['Cell']:
            columnname = base64.b64decode(cell['column'])
            value = cell['$']
            if value == None:
                continue            
            dataset[columnname]=base64.b64decode(value)
        rows.append(dataset)
    
    return json.dumps(rows)    


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=app_port)