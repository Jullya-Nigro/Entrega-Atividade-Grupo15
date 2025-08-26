from flask import Flask
from Models.UserRepository import UserRepository
from UserController import build_user_routes

def create_app():
    app = Flask(__name__)
    
    user_repository = UserRepository()
    
    app.register_blueprint(build_user_routes(user_repository))

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)