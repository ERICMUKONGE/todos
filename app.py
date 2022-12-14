from flask import Flask
from todos import todo_bp
from exts import db
from config import Config


app=Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(todo_bp)
db.init_app(app)


# if __name__ == "__main__":
#     app.run(debug=True)