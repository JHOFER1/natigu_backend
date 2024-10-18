from flask import Blueprint

main = Blueprint('main', __name__)

def register_routes(app):
    from app.routes.your_routes import main
    app.register_blueprint(main)
