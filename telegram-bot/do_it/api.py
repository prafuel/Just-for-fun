from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/",methods=['get','post'])
def main():
    if request.method == "POST":
        user = request.json["username"]
        passwd = request.json["password"]
        return f"username : {user} , password : {passwd}"
    
    return render_template("index.html")


if __name__ == "__main__" :
    app.run(port=8000,debug=True)