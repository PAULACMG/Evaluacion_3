from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/formulariodenotas')
def formulariodenotas():
    return render_template('ejercicio1.html')

@app.route('/largodecaracteres')
def largodecaracteres():
    return render_template('ejercicio2.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        not1 = int(request.form['nota1'])
        not2 = int(request.form['nota2'])
        not3 = int(request.form['nota3'])
        asist = int(request.form['asistencia'])
        promedio = (not1 + not2 + not3) / 3
        estado = 'APROBADO' if promedio >= 40 and asist >= 75 else 'REPROBADO'
        return render_template('ejercicio1.html', promedio=promedio, estado=estado)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nom1 = request.form['nombre1']
        nom2 = request.form['nombre2']
        nom3 = request.form['nombre3']
        noms = [nom1, nom2, nom3]
        nom_largo = max(noms, key=len)
        cant_caracteres = len(nom_largo)
        return render_template('ejercicio2.html', nombre_largo=nom_largo, cantidad_caracteres=cant_caracteres)


if __name__ == '__main__':
    app.run(debug=True)

