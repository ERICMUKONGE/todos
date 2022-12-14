from flask import Blueprint,render_template,request,redirect
from models import Todo
from exts import db

todo_bp =Blueprint('todos',__name__)

@todo_bp.route('/',methods=['GET','POST'])
def get_todos():
    todos = Todo.query.all()
    if request.method == "POST":
        item = request.form['item']

        new_todo = Todo(item=item)

        db.session.add(new_todo)
        db.session.commit()

        return redirect('/')

    return render_template('index.html',todos=todos)

@todo_bp.route('/todo/update/<int:todo_id>',methods=['GET','POST'])
def update_todo(todo_id):
    todo_to_update = Todo.query.get_or_404(todo_id)

    if request.method =="POST":
        todo_to_update.item = request.form['title']

        if request.method =="GET":
            todo_to_update.is_done =request.form['is_done']



    return render_template('edit.html',todo=todo_to_update)

@todo_bp.route('/todo/delete/<int:todo_id>',methods=['GET'])
def delete_todo(todo_id):
    todo_to_delete = Todo.query.get_or_404(todo_id)

    db.session.delete(todo_to_delete)

    db.session.commit()

    return redirect('/')


