# main.py
from flask import Flask, jsonify, request
from bd import base_datos

app = Flask(__name__)

# GET: Obtener todos los registros
@app.route('/api/recursos', methods=['GET'])
def obtener_todos():
    return jsonify({"datos": base_datos, "total": len(base_datos)}), 200

# GET: Obtener un registro por ID
@app.route('/api/recursos/<int:id>', methods=['GET'])
def obtener_por_id(id):
    recurso = base_datos.get(id)
    if recurso:
        return jsonify({"dato": recurso}), 200
    return jsonify({"error": "Recurso no encontrado"}), 404

# POST: Crear nuevo registro
@app.route('/api/recursos', methods=['POST'])
def crear():
    if not request.is_json:
        return jsonify({"error": "El contenido debe ser JSON"}), 400
    
    data = request.get_json()
    if not all(k in data for k in ("nombre", "email", "rol")):
        return jsonify({"error": "Faltan campos obligatorios: nombre, email, rol"}), 400

    nuevo_id = max(base_datos.keys()) + 1 if base_datos else 1
    base_datos[nuevo_id] = data
    return jsonify({"mensaje": "Recurso creado", "id": nuevo_id, "dato": base_datos[nuevo_id]}), 201

# PUT: Actualizar registro
@app.route('/api/recursos/<int:id>', methods=['PUT'])
def actualizar(id):
    if id not in base_datos:
        return jsonify({"error": "Recurso no encontrado"}), 404
    
    if not request.is_json:
        return jsonify({"error": "El contenido debe ser JSON"}), 400
    
    data = request.get_json()
    base_datos[id].update(data)
    return jsonify({"mensaje": "Recurso actualizado", "dato": base_datos[id]}), 200

# DELETE: Eliminar registro
@app.route('/api/recursos/<int:id>', methods=['DELETE'])
def eliminar(id):
    if id not in base_datos:
        return jsonify({"error": "Recurso no encontrado"}), 404
    
    eliminado = base_datos.pop(id)
    return jsonify({"mensaje": "Recurso eliminado", "dato": eliminado}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)