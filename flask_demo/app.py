# utf-8

import json
from flask import Flask, jsonify
from flask_cors import CORS
from flask import request
from sklearn.externals import joblib
import numpy as np

application = Flask(__name__)
CORS(application)

model1 = joblib.load('model_1.pkl') 
model2 = joblib.load('model_2.pkl') 

@application.route('/health', methods=['GET'])
def pong():
    return jsonify({
        'health': 'awesome'
    })

def get_output(model,query):
    pred = model.predict_proba([query])
    classes = [str(x) for x in range(0,len(pred[0]))] # classes as int, can be replaced with strings of classes ['a','b', 'c']
    
    probs = list(reversed(sorted(pred[0])))
    cats = [classes[z] for z in list(reversed(np.argsort(pred)[::-1][0]))]
    return cats,probs


@application.route('/signals_mltool/predict', methods=['POST'])
def predict():
    query = json.loads(request.data)['text']


    pred_1 = get_output(model1,query)

    pred_2 = get_output(model2,query)

    return jsonify({'hoofdrubriek': list(pred_1),
                    'subrubriek': list(pred_2)})


if __name__ == '__main__':
    application.run(port=8000)
