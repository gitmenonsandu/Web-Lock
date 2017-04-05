import os
import sys
import re
import time
import json
import tensorflow as tf
sys.path.insert(0,'./tensorbox')

from prediction import predict
from resize import resize_and_crop


from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template
from flask import jsonify
from werkzeug.utils import secure_filename
from train import build_forward
from flaskrun import flaskrun
app=Flask(__name__)

from flask import render_template

UPLOAD_FOLDER = './temp/'
ALLOWED_EXTENSIONS = set(['png'])

    
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
		os.system("rm ./images/*.png")
		os.system("rm ./static/annoted/*.png")
		os.system("rm ./temp/*.png")
		

		# Uncomment when internet comes
		try:
			print "getting image"
			if file.filename=='':
				print "No file uploaded"
				return redirect(request.url)
			if file and allowed_file(file.filename):
				filename=secure_filename(file.filename)
				file.save(os.path.join(app.config['UPLOAD_FOLDER'],'picture.png'))
				print file.filename

			print "Picture uploaded" 

			
			resize_and_crop(UPLOAD_FOLDER+'picture.png')
			print "Image resized and cropped"
		except:
			print "No such file"
	
		
	predicted_images=predict("./images/")
	print "prediction done"
	
	print predicted_images
		
	return jsonify({'images':predicted_images.values()})
	#return render_template('index.html',images=predicted_images.values())
		
@app.route('/geturl/')
def second_page():
	return render_template('getUrl.html')

@app.route('/geturl/',methods=['GET','POST'])
def get_url():
	if request.method=='POST':
		if 'url' not in request.form:
			print "No url"
			return redirect(request.url)
		url=request.form['url']
		os.system("rm ./images/*.png")
		os.system("rm ./static/annoted/*.png")
		os.system("rm ./temp/*.png")
		
		s=Screenshot()
		s.capture(url, './temp/picture.png')
		print "Image taken"
		resize_and_crop('./temp/picture.png')
		print "Image resized and cropped"

		predicted_images=predict("./images/")
		print "prediction done"
	
		print predicted_images
	
		return render_template('getUrl.html',images=predicted_images.values())

flaskrun(app,default_host="0.0.0.0",default_port="8000")