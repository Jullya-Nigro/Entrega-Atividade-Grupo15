from .user import User, db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500))
    status = db.Column(db.String(50), default= 'Pendente')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Adiciona a relação com o modelo User
    user = db.relationship('User', backref=db.backref('tasks', lazy=True))

    __tablename__ = 'tasks'