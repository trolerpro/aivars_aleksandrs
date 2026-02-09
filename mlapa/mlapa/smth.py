from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def anketa():

    return render_template("sakums.html")
 
@app.route("/videjas")
def attels():
    return render_template("videjas.html")
@app.route("/atzimes")
def sakums():
    return render_template("atzime.html")


if __name__ == '__main__':  
   app.run(debug=True)  