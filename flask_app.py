# libraries
from flask import Flask, request, jsonify # Flask libraries
from load_model import preprocessing # Funtion to invoke model
import base64 # 
import os # lib for interacting with the operating system

app = Flask(__name__)
app.config["DEBUG"] = True

# Decorator, allow GET Method
@app.route('/Image', methods = ['POST'])
def getPrediction():
  # Cross checking whether GET request
  if request.method == 'POST': 
    # accepting base64 from application
    imgstring = request.json['image'] 
    # checking whether request body contains data
    if len(imgstring) != 0: 
      # Converting base64 into byte
      imgdata = base64.b64decode(imgstring) 
      filename = 'predict_image.jpeg' 
      with open(filename, 'wb') as f: 
        # Creating Image out of byte
        f.write(imgdata) 
      # calling function for prediction
      returnClass = preprocessing(filename) 
      # removing generated image
      os.remove(filename) 
      # sending response to app with status code
      return jsonify({"prediction": returnClass}), 200 
    else:
      # If not contained data sending error stating 'Select the Image'
      return jsonify({"Error": "Please select the Image"}), 400 

if __name__ == '__main__':
  # running application on host 'localhost' and port '9000'
  app.run() 