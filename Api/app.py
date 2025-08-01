from flask import Flask
from flask_cors import CORS
from Infra.db import init_db
from Controllers.tarefa_controller import tarefa_bp
import os

def create_app():

    app = Flask(__name__)

  
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://oben_wer7_user:4oUeIhuddAgFg4KRIrYc4CbldBVRzCB0@dpg-d260n5m3jp1c73cajs10-a.oregon-postgres.render.com/oben_wer7'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    init_db(app)

   
    app.register_blueprint(tarefa_bp, url_prefix='/tarefas')

    return app


app = create_app()

if __name__ == '__main__':
    
    app.run(debug=True)
