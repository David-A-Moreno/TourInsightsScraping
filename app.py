from flask import Flask, jsonify, request
from flask_cors import CORS
from googleinfo import scrape_google_info
from tripadvisorinfo import scrape_tripadvisor_info
from minubeinfo import scrape_minube_info

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Hola'

@app.route('/google-info')
def get_google_info():
    city_name = request.args.get('city')
    google_info = scrape_google_info(city_name)
    return jsonify(google_info)

@app.route('/tripadvisor-info')
def get_tripadvisor_info():
    city_name = request.args.get('city')
    tripadvisor_info = scrape_tripadvisor_info(city_name)
    return jsonify(tripadvisor_info)

@app.route('/minube-info')
def get_minube_info():
    city_name = request.args.get('city')
    minube_info = scrape_minube_info(city_name)
    return jsonify(minube_info)

if __name__ == '__main__':
    app.run(debug=True)
