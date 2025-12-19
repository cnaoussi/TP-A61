from flask import Flask

def create_app(config_object=None):
    # 1. On crée l'instance unique de l'application
    flask_app = Flask('ml_api')
    
    # 2. On applique la configuration si elle est fournie
    if config_object:
        flask_app.config.from_object(config_object)

    # 3. On importe et on enregistre les blueprints sur CETTE instance
    from api.controller import prediction_app
    flask_app.register_blueprint(prediction_app)

    # 4. On retourne l'instance configurée
    return flask_app