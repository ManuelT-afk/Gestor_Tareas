from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista en memoria para almacenar las tareas
tareas = []
contador_id = 1

@app.route('/')
def index():
    return render_template('index.html', tareas=tareas)

@app.route('/agregar', methods=['POST'])
def agregar_tarea():
    global contador_id
    texto = request.form.get('texto')
    if texto and texto.strip():
        nueva_tarea = {
            'id': contador_id,
            'texto': texto.strip(),
            'hecho': False
        }
        tareas.append(nueva_tarea)
        contador_id += 1
    return redirect(url_for('index'))

@app.route('/completar/<int:tarea_id>')
def completar_tarea(tarea_id):
    for tarea in tareas:
        if tarea['id'] == tarea_id:
            tarea['hecho'] = True
            break
    return redirect(url_for('index'))

@app.route('/eliminar/<int:tarea_id>')
def eliminar_tarea(tarea_id):
    global tareas
    tareas = [tarea for tarea in tareas if tarea['id'] != tarea_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
