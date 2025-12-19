from flask import Blueprint, request, jsonify
from regression_model.predict import make_prediction
from regression_model import __version__ as _version

from api.config import get_logger
from api.validation import validate_inputs
from api import __version__ as api_version

_logger = get_logger(logger_name=__name__)


prediction_app = Blueprint('prediction_app', __name__)


@prediction_app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        _logger.info('health status OK')
        return 'ok'


@prediction_app.route('/version', methods=['GET'])
def version():
    if request.method == 'GET':
        return jsonify({'model_version': _version,
                        'api_version': api_version})


@prediction_app.route('/v1/predict/regression', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Step 1: Extract JSON
        json_data = request.get_json()
        _logger.debug(f'Inputs: {json_data}')

        # Step 2: Validate
        input_data, errors = validate_inputs(input_data=json_data)

        # Step 3: Model prediction (renvoie déjà une liste !)
        result = make_prediction(input_data=input_data)
        _logger.debug(f'Outputs: {result}')

        # Step 4 & 5: On combine et on renvoie directement
        return jsonify({
            'predictions': result.get('predictions'),
            'version': result.get('version'),
            'errors': errors  # Utilisez 'errors' venant de l'étape 2
        })
