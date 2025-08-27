from flask import Flask, make_response, request, jsonify

class UserRepository():
    _users_id = 2

    def __init__(self):
        self.users = {
            1: {"id": 1, "nome": "teste da silva", "email": "teste@gmail.com"}
        }

    def add_user(self, user):
        user["id"] = UserRepository._users_id
        self.users[UserRepository._users_id] = user
        
        UserRepository._users_id += 1

        return {"status": 201, "mensagem": "Usuario criado com sucesso", "data": user}
    
    def update_user(self, userId, user):
        if userId not in self.users:        
            return {"status": 404, "mensagem": "Usuario não encontrado"}

        if user.get("nome") is not None:
            self.users[userId]["nome"] = user["nome"]
        
        if user.get("email") is not None:
            self.users[userId]["email"] = user["email"]
        
        return {"status": 200, "mensagem": "Usuario atualizado com sucesso", "data": self.users[userId]}
    
    def delete_user(self, user_id):
        if user_id not in self.users:
            return {"status": 404, "mensagem": "Usuario não encontrado"}

        del self.users[user_id]
        
        return {"status": 200, "mensagem": "Usuario deletado com sucesso"}
    
    def get_all_users(self):
        if len(self.users) == 0:
            return {"status": 204, "mensagem": "Nenhum usuario encontrado"}
        
        return {"status": 200, "mensagem": "Usuarios encontrados com sucesso", "data": list(self.users.values())}
    
    def get_user(self, user_id):
        if user_id not in self.users:
            return {"status": 404, "mensagem": "Usuario não encontrado"}

        return {"status": 200, "mensagem": "Usuario encontrado com sucesso", "data": self.users[user_id]}

def formata_response(response):
    if response["status"] == 200 or response["status"] == 201:
        return jsonify(response), response["status"]
    
    return jsonify(response), response["status"]

def create_app():
    app = Flask(__name__)

    app.config['JSON_SORT_KEYS'] = False
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

    
    user_repository = UserRepository()

    @app.route('/users/', methods=['POST'])
    def create_user():
        data = request.get_json()

        response = user_repository.add_user(data)
        
        return formata_response(response)
    
    @app.route('/users/', methods=['GET'])
    def get_users():
        response = user_repository.get_all_users()
        
        return formata_response(response)
    
    @app.route('/users/<int:userId>', methods=['GET'])
    def get_user(userId):
        response = user_repository.get_user(userId)
        
        return formata_response(response)

    @app.route('/users/<int:userId>', methods=['PUT'])
    def update_user(userId):
        data = request.get_json()

        response = user_repository.update_user(userId, data)
        
        return formata_response(response)

    @app.route('/users/<int:userId>', methods=['DELETE'])
    def delete_user(userId):
        response = user_repository.delete_user(userId)
        
        return formata_response(response)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)