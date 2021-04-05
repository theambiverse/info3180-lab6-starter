from flask import Flask
#from flask_cors import CORS


#cors = CORS()

app = Flask(__name__)
#CORS(app)

#cors.init_app(app)
from app import views
