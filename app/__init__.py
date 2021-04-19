from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

# # initializing application
# app= Flask(__name__,instance_relative_config = True)

# # # Setting up configuration
# app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')

# INitializing Flask Extensions
bootstrap=Bootstrap()

def create_app(config_name):
    app=Flask(__name__,instance_relative_config = True)
    
    # creating the app configurations
    app.config.from_object(config_options[config_name])
    
    #initializing flask extensions
    bootstrap.init_app(app)
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .request import config_request
    config_request(app)
    # will add the views and forms
    
    return app
