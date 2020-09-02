from werkzeug.wrappers import Request, Response
from flask import Flask, request, jsonify
from load_model import getModel, getClass, preprocessing
import numpy as np
import uuid
import os


app = Flask(__name__)

@app.route('/Image', methods = ['GET'])
def getPrediction():
  if request.method == 'GET':
    if (len(request.files)) == 0:
      return jsonify({"Error": "Please select the Image"}), 400
    else:
      file = request.files['image']
      if len(file.mimetype.split()) == 0:
        return jsonify({"Error": "Please select the Image"}), 400
      else:
        returnClass = preprocessing(file)
        return jsonify({"prediction": returnClass}), 200

if __name__ == '__main__':
  from werkzeug.serving import run_simple
  run_simple('localhost', 9000, app)  