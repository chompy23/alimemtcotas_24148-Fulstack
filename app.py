from flask import Flask, requests, jsonify
from flask_cors import CORS
import mysql.connector 
from werkzeug.utils import secure_filename
from app_mascota import Mascota

import os
import time


app = Flask(__name__)
CORS(app) #habilita las referencias a otros servidores
