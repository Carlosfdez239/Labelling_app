from flask import Flask

def create_app():
    app = Flask(__name__)

    # Registramos las rutas
    from src.routes import bp
    app.register_blueprint(bp)

    return app