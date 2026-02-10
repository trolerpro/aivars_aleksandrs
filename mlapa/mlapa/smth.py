from flask import Flask, render_template, request
app = Flask(__name__)
import sqlite3

@app.route("/")
def sakums():
    return render_template("sakums.html")
 
@app.route("/videjas")
def videjas():
    return render_template("videjas.html")
@app.route("/atzimes")
def atzimes():
    return render_template("atzime.html")
@app.route("/uzd_kalendars")
def kalendars():
    return render_template("uzd_kalendars.html")

@app.route('/submit', methods=['POST'])
def submit():
   if request.method == 'POST':
       prieksmets = request.form['pr']
       if prieksmets :
            conn = sqlite3.connect('c:/Users/AT2312/Desktop/program/4tema/mlapa/database.db')
            conn.execute( "INSERT INTO preiksmeti (prieksmets) VALUES (?)", (prieksmets,) )
            conn.commit()
            conn.close()



@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        ir = request.form['ir']
        max = request.form['max']
        if ir and max:
            ir = float(ir)
            max = float(max)
            if max != 0:
                procenti = (ir / max) * 100
                return render_template('atzime.html', procenti=procenti)
            else:
                return "Maksimālie nevar būt nulle."







if __name__ == '__main__':  
   app.run(debug=True)  