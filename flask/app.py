import os
import json
from flask import Flask, request, render_template, url_for, redirect
from werkzeug.utils import secure_filename
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# from demo import get_video
import io
import random

import numpy as np
import cv2

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///team7.db'

# # Initialize database
# db = SQLAlchemy(app)

videos = []

# create route
@app.route('/', methods=['POST','GET'])
def home():
	videos = ['Osaka','Webcam']
	return render_template("home.html", videos=videos) 


@app.route('/review/<vid_name>', methods=['POST','GET'])
def review(vid_name):
	vid_name = vid_name
	return render_template('review.html', vid_name=vid_name)

@app.route('/dashboard')
def dashboard():
	return render_template('dashboard.html')