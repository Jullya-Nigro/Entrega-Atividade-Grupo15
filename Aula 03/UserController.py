
from flask import Blueprint, request, jsonify

from Models.User import User
from Models.UserRepository import UserRepository

def build_user_routes(user_repository: UserRepository):
    user_bp = Blueprint('user', __name__, url_prefix='/users')

    @user_bp.route('/', methods=['POST'])
    def create_user():
        data = request.get_json()

        user = User(**data)
        response = user_repository.add_user(user)
        
        return jsonify(response.to_dict()), response.status_code
    
    @user_bp.route('/', methods=['GET'])
    def get_users():
        response = user_repository.get_all_users()
        
        return jsonify(response.to_dict()), response.status_code
    
    @user_bp.route('/<int:userId>', methods=['GET'])
    def get_user(userId):
        response = user_repository.get_user(userId)
        
        return jsonify(response.to_dict()), response.status_code

    @user_bp.route('/<int:userId>', methods=['PUT'])
    def update_user(userId):
        data = request.get_json()

        user = User(**data)
        response = user_repository.update_user(userId, user)
        
        return jsonify(response.to_dict()), response.status_code

    @user_bp.route('/<int:userId>', methods=['DELETE'])
    def delete_user(userId):
        response = user_repository.delete_user(userId)
        
        return jsonify(response.to_dict()), response.status_code

    return user_bp