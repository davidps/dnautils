from flask import Flask, session
from .config import Config
from flask_dropzone import Dropzone
from werkzeug.utils import secure_filename
import os 
# from pathlib import Path

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or \
    '8e46e820-2b47-446c-be2c-b3816425ea85'

dropzone = Dropzone(app)
# create the folders when setting up your app
os.makedirs(os.path.join(app.instance_path, 'files'), exist_ok=True)
from app import routes