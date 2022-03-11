from flask import Flask, jsonify, request, make_response
import json
import platform
import sys
from flask_cors import CORS
from annotation import annotation

cors_config = {
    "origins": ["http://localhost:5000"],
    "methods": ["OPTIONS", "GET", "POST"],
    "allow_headers": ["Authorization"]
}

app = Flask(__name__)
CORS(app)


# ROUTING

@app.route('/keywords', methods=['GET', 'POST'])
def getKeywords():
    data = request.get_json()

    link = data["link"]
    language = data["lang"]

    annotation_service = annotation()
    result = annotation_service.annotate(link, language)

    response = make_response(jsonify(result), 200)

    return response


# RUN APPLICATION
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
