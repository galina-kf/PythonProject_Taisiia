from flask_migrate import Migrate
from Taisiia_project.run import app
from .database import db

db.init_app(app)
Migrate(app, db)


if __name__=="__main__":
   app.run(debug=True)