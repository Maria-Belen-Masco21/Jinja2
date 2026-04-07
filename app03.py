from flask import Flask, render_template, request

app= Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/login", methods["POST"])
def verificar_login():
    usuario=request.form["usuario"]
    password=request.form["password"]
    
    if usuario=="admin"and password=="1234":
        return render_template("dashboard.html",usuario=usuario)
    else:
        return render_template("login.html")

if __name__=="__main__":
    app.run(debug=True)