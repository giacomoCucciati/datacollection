from flask import Blueprint, jsonify, current_app
from flask import request
from . import socketio

api_router = Blueprint("api_router", __name__)

@api_router.route('/hello',methods=['POST'])
def hello():
  print("params", request.get_json(force=True))
  return jsonify({"msg":"Hello from backend!"})

