class User():
    _ids = 1
    
    def __init__(self, nome, email):
        self.Nome = nome
        self.Email = email
        
        self.Id = User._ids
        User._ids += 1

    def to_dict(self):
        return {
            "Id": self.Id,
            "Nome": self.Nome,
            "Email": self.Email
        }
    