from flask import Blueprint, jsonify

# Le nom 'prediction_app' doit correspondre à celui importé dans app.py
prediction_app = Blueprint('prediction_app', __name__)

@prediction_app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200