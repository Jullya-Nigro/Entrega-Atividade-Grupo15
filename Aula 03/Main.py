from flask import Flask, make_response, request, jsonify

class UserRepository():
    _users_id = 2

    def __init__(self):
        self.users = {
            1: {"id": 1, "nome": "teste da silva", "email": "teste@gmail.com"}
        }

    def add_user(self, user):
        """
        Cria um novo usuario
        ---
        Tags:
          - Users
        description: Cria um novo usuario com nome e email
        consumes:
          - application/json
        produces:
          - application/json
        parameters:
          - in: body
            name: user
            description: Dados do usuario
            required: true
            schema:
              type: object
              required:
                - nome
                - email
              properties:
                nome:
                  type: string
                  exemple: teste da silva
                email:
                  type: string
                  exemple: teste@gmail.com.br
                  
        responses:
          201:
            description: Usuario criado com sucesso
            schema:
              type: object
              properties:
                status:
                  type: integer
                  example: 201
                mensagem:
                  type: string
                  example: Usuario criado com sucesso
                data:
                  type: object
                  properties:
                    id:
                      type: integer
                      example: 1
                    nome:
                      type: string
                      example: teste da silva
                    email:
                      type: string
                      example: test@gmail.com.br
            400:
                description: Requisição inválida
                schema:
                    type: object
                    properties:
                    status:
                        type: integer
                        example: 400
                    mensagem:
                        type: string
                        example: Requisição inválida
        """
        user["id"] = UserRepository._users_id
        self.users[UserRepository._users_id] = user
        
        UserRepository._users_id += 1

        return {"status": 201, "mensagem": "Usuario criado com sucesso", "data": user}
    
    def update_user(self, userId, user):
        """
        Atualiza um usuario existente
        ---
        Tags:
          - Users
        description: Atualiza os dados de um usuario existente
        consumes:
          - application/json
        produces:
          - application/json
        parameters:
          - in: path
            name: userId
            type: integer
            required: true
            description: ID do usuario a ser atualizado
          - in: body
            name: user
            description: Dados do usuario para atualização
            required: true
            schema:
              type: object
              properties:
                nome:
                  type: string
                  exemple: teste da silva
                email:
                  type: string
                  exemple: teste@gmail.com.br
        responses:
          200:
            description: Usuario atualizado com sucesso
            schema:
              type: object
              properties:
                status:
                  type: integer
                  example: 200
                mensagem:
                  type: string
                  example: Usuario atualizado com sucesso
                data:
                  type: object
                  properties:
                    id:
                      type: integer
                      example: 1
                    nome:
                      type: string
                      example: teste da silva
                    email:
                      type: string
                      example: teste@gmail.com.br
          404:
            description: Usuario não encontrado
            schema:
              type: object
              properties:
                status:
                  type: integer
                  example: 404
                mensagem:
                  type: string
                  example: Usuario não encontrado
        """
        if userId not in self.users:        
            return {"status": 404, "mensagem": "Usuario não encontrado"}

        if user.get("nome") is not None:
            self.users[userId]["nome"] = user["nome"]
        
        if user.get("email") is not None:
            self.users[userId]["email"] = user["email"]
        
        return {"status": 200, "mensagem": "Usuario atualizado com sucesso", "data": self.users[userId]}
    
    def delete_user(self, user_id):
        """
        Remove um usuario
        ---
        Tags:
          - Users
        description: Remove um usuario pelo ID
        produces:
          - application/json
        parameters:
          - in: path
            name: user_id
            type: integer
            required: true
            description: ID do usuario a ser removido
        responses:
          200:
            description: Usuario deletado com sucesso
            schema:
              type: object
              properties:
                status:
                  type: integer
                  example: 200
                mensagem:
                  type: string
                  example: Usuario deletado com sucesso
          404:
            description: Usuario não encontrado
            schema:
              type: object
              properties:
                status:
                  type: integer
                  example: 404
                mensagem:
                  type: string
                  example: Usuario não encontrado
        """
        if user_id not in self.users:
            return {"status": 404, "mensagem": "Usuario não encontrado"}

        del self.users[user_id]
        
        return {"status": 200, "mensagem": "Usuario deletado com sucesso"}
    
    def get_all_users(self):
        """
        Lista todos os usuarios
        ---
        Tags:
          - Users
        description: Retorna a lista de todos os usuarios cadastrados
        produces:
          - application/json
        responses:
          200:
            description: Lista de usuarios retornada com sucesso
            schema:
              type: object
              properties:
                status:
                  type: integer
                  example: 200
                mensagem:
                  type: string
                  example: Usuarios encontrados com sucesso
                data:
                  type: array
                  items:
                    type: object
                    properties:
                      id:
                        type: integer
                        example: 1
                      nome:
                        type: string
                        example: teste da silva
                      email:
                        type: string
                        example: teste@gmail.com.br
          204:
            description: Nenhum usuario encontrado
            schema:
              type: object
              properties:
                status:
                  type: integer
                  example: 204
                mensagem:
                  type: string
                  example: Nenhum usuario encontrado
        """
        if len(self.users) == 0:
            return {"status": 204, "mensagem": "Nenhum usuario encontrado"}
        
        return {"status": 200, "mensagem": "Usuarios encontrados com sucesso", "data": list(self.users.values())}
    
    def get_user(self, user_id):
        """
        Busca um usuario especifico
        ---
        Tags:
          - Users
        description: Retorna os dados de um usuario especifico pelo ID
        produces:
          - application/json
        parameters:
          - in: path
            name: user_id
            type: integer
            required: true
            description: ID do usuario a ser buscado
        responses:
          200:
            description: Usuario encontrado com sucesso
            schema:
              type: object
              properties:
                status:
                  type: integer
                  example: 200
                mensagem:
                  type: string
                  example: Usuario encontrado com sucesso
                data:
                  type: object
                  properties:
                    id:
                      type: integer
                      example: 1
                    nome:
                      type: string
                      example: teste da silva
                    email:
                      type: string
                      example: teste@gmail.com.br
          404:
            description: Usuario não encontrado
            schema:
              type: object
              properties:
                status:
                  type: integer
                  example: 404
                mensagem:
                  type: string
                  example: Usuario não encontrado
        """
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