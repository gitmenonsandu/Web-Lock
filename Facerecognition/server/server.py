import os
import sys
import re
import time
import json




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

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods=['GET','POST'])
def get_file():

	if request.method=='POST':
		if 'file' not in request.files:
			print request.files
			print 'No url given'
			return redirect(request.url)
		file=request.files['file']
		os.system("rm ./images/*")
		
		# Uncomment when internet comes
		try:
			print "getting image"
			if file.filename=='':
				print "No file uploaded"
				return redirect(request.url)
			if file and allowed_file(file.filename):
				filename=secure_filename(file.filename)
				filepath=os.path.join(app.config['UPLOAD_FOLDER'],filename)
				file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
				print file.filename+" uploaded"

		except:
			print "No such file"
	
				
	return render_template('index.html',imgName=filepath)

flaskrun(app,default_host="0.0.0.0",default_port="8000")