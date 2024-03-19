# from flask import Flask, request, jsonify
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', methods=['GET'])
def save_signature():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True,port=8080)