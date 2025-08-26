from Models.User import User
from Models.Response import Response

class UserRepository():
    def __init__(self):
        self.users:list[User] = []    
    
    def add_user(self, user: User):
        self.users.append(user)
        
        return Response(True, user.to_dict(), 201)
    
    def update_user(self, userId, user: User):
        for i, u in enumerate(self.users):
            if u.Id == userId:
                if user.Nome is not None:
                    self.users[i].Nome = user.Nome
                
                if user.Email is not None:
                    self.users[i].Email = user.Email
                
                return Response(True, self.users[i].to_dict(), 200)
            
        return Response(False, "Usuario não encontrado", 404)
    
    def delete_user(self, user_id):
        for i, u in enumerate(self.users):
            if u.Id == user_id:
                del self.users[i]
                return Response(True, "Usuario deletado", 200)
            
        return Response(False, "Usuario não encontrado", 404)
    
    def get_all_users(self):
        if len(self.users) == 0:
            return Response(False, "Nenhum usuario encontrado", 204)
        
        return Response(True, [user.to_dict() for user in self.users], 200)
    
    def get_user(self, user_id):
        for user in self.users:
            if user.Id == user_id:
                return Response(True, user.to_dict(), 200)
            
        return Response(False, "Usuario não encontrado", 404)