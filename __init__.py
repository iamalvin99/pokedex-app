from flask import Flask
# from flask_mongoengine import MongoEngine, Document


def create_app():
    app = Flask(__name__)

    # app.config['MONGODB_SETTINGS'] = {
    #     'db':'portfolio',
    #     'host':'localhost'
    # }

    app.static_folder = 'assets'
    # db = MongoEngine(app)
 
    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    return app
#     return app, db

# app, db = create_app()
app = create_app()
