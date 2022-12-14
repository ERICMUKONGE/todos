from exts import db
"""
class Todo:
    item = string(255)
    is_done = Boolean(default=False)
"""
class Todo(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    item = db.Column(db.String(255))
    is_done = db.Column(db.Boolean(),default=False)

    def __repr__(self) -> str:
        return f"<Todo {self.item}>"