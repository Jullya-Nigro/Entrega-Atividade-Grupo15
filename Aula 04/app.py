import os
from flask import Flask
from config import Config # importa as 
from controllers.user_controller import UserController
from controllers.task_controller import TaskController
from models.user import User, db
from models.task import Task

app = Flask(__name__, template_folder=os.path.join('view', 'templates'))
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

app.add_url_rule('/', 'index',  UserController.index)
app.add_url_rule('/contact', 'contact', UserController.contact, methods=['GET', 'POST'])

app.add_url_rule('/tasks', 'tasks', TaskController.list_tasks, methods=['GET'])
app.add_url_rule('/tasks/new', 'create_task', TaskController.create_task, methods=['GET','POST'])
app.add_url_rule('/tasks/update/<int:task_id>', 'update_task', TaskController.update_task_status, methods=['POST'])
app.add_url_rule('/tasks/delete/<int:task_id>', 'delete_task', TaskController.delete_task, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True, port=5002)