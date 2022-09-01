from flask import Flask , jsonify , request
from classifier125 import get_prediction

app = Flask(__name__) 

@app.route("/predict" , methods=["POST"])

def predictdata():
    image = request.files.get("alphabet")
    
    predictedValue = get_prediction(image)

    return jsonify({
        "prediction" : predictedValue
    })


if __name__== "__main__":
    app.run(debug=True)
























