import os
import sys
import re
import time
import json
import csv

from FaceRecognition import *

from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template
from flask import jsonify
from werkzeug.utils import secure_filename
from flaskrun import flaskrun
app=Flask(__name__)

from flask import render_template

UPLOAD_FOLDER = './images/'
ALLOWED_EXTENSIONS = set(['png','jpg'])

    
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

userlist={}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods=['GET','POST'])
def train():

	if request.method=='POST':
		result=request.form
		name=str(result['name'])
		if name=="predict":
			return render_template('recognise.html',Name='')
		
		userlist=make_dataset(name)
		train_dataset()
		return render_template('recognise.html') 	
				
	return render_template('index.html')


@app.route('/dataset',methods=['GET','POST'])
def predict():

	if request.method=='POST':
		result=request.form

		userlist={}
		i=0
    	with open('userdata.csv') as csvfile:
	        reader=csv.reader(csvfile)
	        for row in reader:
	            if i==0:
	                i=1
	                continue
	            print row
	            userlist[row[0]]=row[1]
		print userlist
		name=predict_face(userlist)
		if name==-1:
			name="Not detected"
		else:
			name="Detected"
		return render_template('recognise.html',Name=name) 	
				
	return render_template('index.html')

flaskrun(app,default_host="0.0.0.0",default_port="8000")