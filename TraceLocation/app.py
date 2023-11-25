from flask import Flask,jsonify
from datetime import datetime


# local imports
from send import getData,reader
app = Flask(__name__)

@app.route("/",methods=['get'])
def main():
    date = datetime.now()
    host_info = getData()
    data = [
        date,
        host_info
    ]
    return data

@app.route("/personal_id/<str>",methods=['get'])
def personal_id(str):
    if str == "version":
        return jsonify(reader())
    return "Path Not Found"

# if __name__ == "__main__":
#     app.run(debug=True, port=8000)