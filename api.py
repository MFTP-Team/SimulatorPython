from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import sendUtil

import sendUtil

app = Flask(__name__)
api = Api(app)

class AlertReceive(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        id = json_data['id']
        lat = json_data['latitude']
        long = json_data['longitude']
        intensity = json_data['intensity']
        sendUtil.sendUARTMessage(json_data)
        return jsonify(id=id, latitude=lat, longitude=long, intensity=intensity)

api.add_resource(AlertReceive, '/alert')

def startAPI():
    app.run(debug=True)