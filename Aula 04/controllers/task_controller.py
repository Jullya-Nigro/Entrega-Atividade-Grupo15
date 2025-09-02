from flask import render_template, request, redirect, url_for
from models.task import Task, db
from models.user import User

class TaskController:
    @staticmethod
    def list_tasks():
        tasks = Task.query.all()
        return render_template('tasks.html', tasks=tasks)

    @staticmethod
    def create_task():
        if request.method == 'POST':
            title = request.form['title']
            description = request.form['description']
            user_id = request.form['user_id']
            
            new_task = Task(title=title, description=description, user_id=user_id)
            db.session.add(new_task)
            db.session.commit()
        
            return redirect(url_for('tasks'))

        users = User.query.all()
        return render_template('create_task.html', users=users)
    
    @staticmethod
    def update_task_status(task_id):
        task = Task.query.get_or_404(task_id)
        task.status = 'Concluido' if task.status == 'Pendente' else 'Pendente'
        db.session.commit()
        
        return redirect(url_for('tasks'))
    
    @staticmethod
    def delete_task(task_id):
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for('tasks'))
    