from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

inventario = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agregar', methods=['POST'])
def agregar():
    equipo = request.json
    inventario.append(equipo)
    return jsonify({"status": "Equipo agregado con éxito."}), 200

@app.route('/listar', methods=['GET'])
def listar():
    return jsonify(inventario), 200

@app.route('/eliminar', methods=['POST'])
def eliminar():
    nombre = request.json['nombre']
    global inventario
    inventario = [equipo for equipo in inventario if equipo['nombre'] != nombre]
    return jsonify({"status": "Equipo eliminado con éxito."}), 200

if __name__ == '__main__':
    app.run(debug=True)
