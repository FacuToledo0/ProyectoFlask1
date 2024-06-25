import requests

from flask import (Flask, render_template, request, redirect)

app = Flask(__name__)

diccionario_productos = [
    dict(
        product = dict(
            producto = "Coca Cola",
            categoria = "Bebidas"
        )
    ),
    dict(
        product = dict(
            producto = "Pepsi",
            categoria = "Bebidas"
        )
    )
]

@app.route('/')
def index():
    return render_template(
        'index.html'
    )

@app.route('/productos')
def productos():
    lista = diccionario_productos
    return render_template(
        'productos.html',
        lista = lista
    )

@app.route('/add_producto', methods=['GET', 'POST'])
def agregar_productos():    
    if request.method == "POST":
        nombre_producto = request.form['producto']
        categoria_producto = request.form['categoria']

        productos = dict(
            product = dict(
                producto = nombre_producto,
                categoria = categoria_producto
            )
        )
        diccionario_productos.append(productos)
        return redirect("productos")

    return render_template('add_producto.html')

print("hola")
print("git")