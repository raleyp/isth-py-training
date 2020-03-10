from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')

def sumar ():
    v1 = int(request.args.get("v1", "v1")) 
    v2 = int(request.args.get("v2", "v2")) 
    suma = v1 + v2
    return f'La suma es: {escape(suma)}'