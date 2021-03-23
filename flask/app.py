import os
import json
from flask import Flask, request, render_template, url_for, redirect
from werkzeug.utils import secure_filename
import pyrebase
from datetime import datetime

# from demo import get_video
import io
import random

import numpy as np
import cv2

app = Flask(__name__)
# firebase config
config = {
    "apiKey": "AIzaSyCgUIgDoR7tPBGjgxkMaGQxHcVhu2WSmUU",
    "authDomain": "capstone-af326.firebaseapp.com",
    "databaseURL": "https://capstone-af326-default-rtdb.firebaseio.com",
    "projectId": "capstone-af326",
    "storageBucket": "capstone-af326.appspot.com",
    "messagingSenderId": "851232030295",
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

# trying db
db.child("test").push("Hello world")

videos = []

# create route


@app.route('/', methods=['POST', 'GET'])
def home():
    videos = ['Osaka', 'Webcam']
    return render_template("home.html", videos=videos)


@app.route('/review/<vid_name>', methods=['POST', 'GET'])
def review(vid_name):
    vid_name = vid_name
    return render_template('review.html', vid_name=vid_name)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
