from flask import Flask ,jsonify

#let's create a Flask instance
app = Flask(__name__)

#let's create a route(event point)
@app.route('/')
def sample():
    return jsonify({'message': 'This is sample Flask app'})   #this will return a JSON response

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=8080)  #run the Flask app in debug mode