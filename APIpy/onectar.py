from flask import Flask,  jsonify
from creador import lista

app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify(lista)

if __name__== '__main__':
    app.run(debug=True, port=4000)