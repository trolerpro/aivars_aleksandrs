from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
import sqlite3
import os
from datetime import datetime

# Use database next to this module so paths work regardless of current working dir
BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, 'database.db')

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
            conn = sqlite3.connect(DB_PATH)
            conn.execute( "INSERT INTO preiksmeti (prieksmets) VALUES (?)", (prieksmets,) )
            conn.commit()
            conn.close()

@app.route('/submit_videjas', methods=['POST'])
def submit_videjas():
    if request.method == 'POST':
        prieksmets = request.form['pr']
        if prieksmets:
            conn = sqlite3.connect(DB_PATH)
            conn.execute("INSERT INTO videjas (prieksmets) VALUES (?)", (prieksmets,))
            conn.commit()
            conn.close()
    return render_template("videjas.html")

@app.route('/dzest')
def dzest():
    conn = sqlite3.connect(DB_PATH)
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

# Task API Routes
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks ORDER BY due_date")
    tasks = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(tasks)

@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.json
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO tasks (title, description, due_date, priority, status, progress)
                      VALUES (?, ?, ?, ?, ?, ?)""",
                   (data['title'], data.get('description', ''), data['due_date'], 
                    data.get('priority', 'normal'), data.get('status', 'pending'), data.get('progress', 0)))
    conn.commit()
    conn.close()
    return jsonify({'success': True})

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""UPDATE tasks SET title=?, description=?, due_date=?, priority=?, status=?, progress=?, updated_at=CURRENT_TIMESTAMP
                      WHERE id=?""",
                   (data['title'], data.get('description', ''), data['due_date'], 
                    data.get('priority', 'normal'), data.get('status', 'pending'), data.get('progress', 0), task_id))
    conn.commit()
    conn.close()
    return jsonify({'success': True})

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    return jsonify({'success': True})

if __name__ == '__main__':  
   app.run(debug=True)