from flask_restful import Resource, Api
from flask import Flask, request
from flask import jsonify
from app.adaptor.client_routes import clientRoutes

print('Iniciando un nuevo servicio')


app = Flask(__name__)
api = Api(app)
api.add_resource(clientRoutes, '/<string:cif>')


@app.errorhandler(404)
def not_found(*args):
    return (jsonify({"code": 404, "message": "Unknown resource was requested"}), 404)


if __name__ == '__main__':
    app.run(debug=True)
