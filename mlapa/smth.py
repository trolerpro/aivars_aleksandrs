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
            conn.execute( "INSERT INTO preiksmeti (prieksmets) VALUES (?)", (prieksmets) )
            conn.commit()
            conn.close()

@app.route('/submit_videjas', methods=['POST'])
def submit_videjas():
    if request.method == 'POST':
        prieksmets = request.form['pr']
        if prieksmets:
            conn = sqlite3.connect('c:/Users/AT2312/Desktop/program/4tema/mlapa/database.db')
            conn.execute("INSERT INTO videjas (prieksmets) VALUES (?)", (prieksmets,))
            conn.commit()
            conn.close()
    return render_template("videjas.html")

@app.route('/dzest')
def dzest():
    conn = sqlite3.connect('c:/Users/AT2312/Desktop/program/4tema/mlapa/database.db')
    conn.execute( "DELETE FROM preiksmeti")
    conn.commit()
    conn.close()
    return render_template("videjas.html")

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        ir = request.form.get('ir')
        max = request.form.get('max')
        if ir and max:
            try:
                ir = float(ir)
                max = float(max)
            except ValueError:
                return "Ievades nav derīgi skaitļi."
            if ir != 0:
                dalijums = ir / max
                procenti = dalijums * 100
                p = procenti
                if p >= 96:
                    atzime = 10
                elif p >= 87:
                    atzime = 9
                elif p >= 76:
                    atzime = 8
                elif p >= 67:
                    atzime = 7
                elif p >= 56:
                    atzime = 6
                elif p >= 41:
                    atzime = 5
                elif p >= 31:
                    atzime = 4
                elif p >= 21:
                    atzime = 3
                elif p >= 11:
                    atzime = 2
                else:
                    atzime = 1
                return render_template('atzime.html', procenti=procenti, dalijums=dalijums, atzime=atzime)
            else:
                return "Dalīšana nevar notikt ar nulli (ir)."

if __name__ == '__main__':  
   app.run(debug=True)