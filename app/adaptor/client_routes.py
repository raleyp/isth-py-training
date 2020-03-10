from app.application import client_service
from app.domain.model import Client
from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource


class clientRoutes(Resource):

    def get(self, cif):
        print('client_routes.get')
        result = client_service.get(id=cif)

    def post(self, cif):
        print('client_routes.post')
        json_data = request.get_json(force=True)
        client = Client()
        # TODO: populate the client instance with my data like this json_data['username']
        result = client_service.post(client)
        return jsonify(result)
