
from flask import Flask
from flask_cors import CORS
from modelo.modeloProducto import modeloProducto

app = Flask(__name__)	

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/productos',methods=['GET'])
def listar_productos():
        emp=modeloProducto.listar_producto()
        return emp
# RUTA paar peticiones GET  usuario especifico
@app.route('/productos/:<codigo>', methods=['GET'])
def lista_producto(codigo):
    x= modeloProducto.lista_producto(codigo)
    return x

# RUTA PARA PETICION POST insertar usuario
@app.route('/productos', methods=['POST'])
def registrar_productos():
    x= modeloProducto.registrar_producto()
    return x

# RUTA PARA PETICION DELETE borrar  usuario
@app.route('/productos/:<codigo>', methods=['DELETE'])
def eliminar_productos(codigo):
    x=modeloProducto.eliminar_producto(codigo)
    return x

# RUTA PARA PETICION PUT actualiza usuario
@app.route('/productos/:<codigo>', methods=['PUT'])
def actulalizar_productos(codigo):
    x= modeloProducto.actualizar_producto(codigo)
    return x

#PREGUNTA TERCER PARCIAL  
@app.route('/productos/contarproductos',methods=['GET'])
def contar_productos():
      prod=modeloProducto.contar_producto()
      return prod 


if __name__ == '__main__':
   		app.run(debug=True,host='0.0.0.0')