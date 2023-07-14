from flask import jsonify,request
from modelo.coneccion import db_connection



def buscar_producto(codigo):
    try:
        conn = db_connection()
        cur = conn.cursor()
        cur.execute(""" select id,nombre,precio,descripcion,categoria from productos where id=%s
       """, (codigo,))
        datos = cur.fetchone()
        conn.close()
        if datos != None:
            producto = {'id': datos[0], 'nombre': datos[1],
                       'precio': datos[2], 'descripcion': datos[3],
                       'categoria': datos[4]}
            return producto
        else:
            return None
    except Exception as ex:
            raise ex
class modeloProducto():
    @classmethod
    def listar_producto(self):
        try:
            conn=db_connection()
            cur=conn.cursor()
            cur.execute("""select id,nombre,precio,descripcion,categoria from productos
                        """)
            datos=cur.fetchall()
            productos=[]
            for fila in datos:
                producto={'id':fila[0],
                         'nombre':fila[1],
                         'precio':fila[2],
                         'descripcion':fila[3],
                         'categoria':fila[4],
                        }
                productos.append(producto)
            conn.close()
            return jsonify({'produtos':productos,'mensaje':"productos listados","exito":True})
        except Exception as ex:
                return jsonify({'mensaje':"Error",'exito':False})
        
    @classmethod
    def lista_product(self,codigo):
        try:
            producto = buscar_producto(codigo)
            if producto != None:
                return jsonify({'productos': producto, 'mensaje': "producto encontrado.", 'exito': True})
            else:
                return jsonify({'mensaje': "producto no encontrado.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
        
    @classmethod
    def registrar_producto(self):
        try:
            producto = buscar_producto(request.json['id'])
            if producto != None:
                return jsonify({'mensaje': "Cedula de identidad  ya existe, no se puede duplicar.", 'exito': False})
            else:
                conn = db_connection()
                cur = conn.cursor()
                cur.execute('INSERT INTO productos values(%s,%s,%s,%s,%s)', (request.json['id'], request.json['nombre'], request.json['precio'],
                                                                            request.json['descripcion'], request.json['categoria']))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "Producto registrado.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})

    @classmethod
    def eliminar_producto(self,codigo):
        try:
            producto = buscar_producto(codigo)
            if producto != None:
                conn = db_connection()
                cur = conn.cursor()
                cur.execute("DELETE FROM productos WHERE id = %s", (codigo,))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "producto eliminado.", 'exito': True})
            else:
                return jsonify({'mensaje': "producto no encontrado.", 'exito': False})
        except Exception as ex:
                return jsonify({'mensaje': "Error", 'exito': False})
        
    @classmethod   
    def actualizar_producto(self,codigo):
        try:
            producto = buscar_producto(codigo)
            if producto != None:
                conn = db_connection()
                cur = conn.cursor()
                cur.execute("""UPDATE productos SET nombre=%s, precio=%s, descripcion=%s,categoria=%s
                 WHERE id=%s""",
                        (request.json['nombre'], request.json['precio'], request.json['descripcion'], request.json['categoria'], codigo))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "producto actualizado.", 'exito': True})
            else:
                return jsonify({'mensaje': "producto  no encontrado.", 'exito': False})
        except Exception as ex:
                return jsonify({'mensaje': "Error", 'exito': False})

        
    @classmethod
    def contar_producto(self):
        try:
            conn=db_connection()
            cur=conn.cursor()
            cur.execute("""SELECT productos.id, productos.nombre, COUNT(*) AS cantidad
                    FROM productos, compras
                    WHERE productos.id = compras.producto_id
                    GROUP BY productos.id,productos.nombre order by productos.id asc
                    """)
            datos = cur.fetchall()
            productos = []
            for fila in datos:
                 producto = {
                'productos.id': fila[0],
                'productos.nombre': fila[1],
                'cantidad': fila[2],
            }
                 productos.append(producto)
            conn.close()
            return jsonify({'produtos':productos,'mensaje':"productos listados","exito":True})
        except Exception as ex:
                return jsonify({'mensaje':"Error",'exito':False})
 
   
    
