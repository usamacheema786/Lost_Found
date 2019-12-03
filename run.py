# from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask import Flask
from config_default import ProductionConfig



def create_app(config_object=ProductionConfig):
    app = Flask(__name__)
    app.config.from_object(ProductionConfig)
    return app



app = create_app(ProductionConfig)
mail = Mail(app)

db = SQLAlchemy(app)

if __name__ == "__main__":
    from user.api import user
    app.register_blueprint(user)
    from item.api import item
    app.register_blueprint(item)

    app.run(host='0.0.0.0', debug=True)
