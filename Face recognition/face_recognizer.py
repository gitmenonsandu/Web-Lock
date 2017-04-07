#!/usr/bin/python
# sureshsreeja.2015@gmail.com
# 8650287513   /8095764752[wa]
# Import the required modules
import cv2, os, fnmatch
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
 
arr = []


# For face detection we will use the Haar Cascade provided by OpenCV.

cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

# For face recognition we will the the LBPH Face Recognizer 
#recognizer = cv2.createFisherFaceRecognizer()
recognizer = cv2.createLBPHFaceRecognizer()

def get_images_and_labels(path):
    # Append all the absolute image paths in a list image_paths
    # We will not read the image with the .sad extension in the training set
    # Rather, we will use them to test our accuracy of the training
    image_paths = [os.path.join(path, f) for f in os.listdir(path) if not f.endswith('.jpg')]
    # images will contains face images
    images = []
    # labels will contains the label that is assigned to the image
    labels = []
    for image_path in image_paths:
        # Read the image and convert to grayscale
        image_pil = Image.open(image_path).convert('L')
        # Convert the image format into numpy array
        image = np.array(image_pil, 'uint8')
        # Get the label of the image
        nbr = int(os.path.split(image_path)[1].split(".")[0].replace("", ""))
        # Detect the face in the image
        faces = faceCascade.detectMultiScale(image)
        # If face is detected, append the face to images and the label to labels
        for (x, y, w, h) in faces:
            images.append(image[y: y + h, x: x + w])
            labels.append(nbr)
            cv2.imshow("Adding faces to traning set...", image[y: y + h, x: x + w])
            cv2.waitKey(50)
    # return the images list and labels list
    return images, labels

path = './dataset_final'
# Call the get_images_and_labels function and get the face images and the 
# corresponding labels
images, labels = get_images_and_labels(path)
cv2.destroyAllWindows()

# Perform the tranining
recognizer.train(images, np.array(labels))
c={} #for storing minimum confidence level for each person
d={} #for storing the emotion for each person
filename={} #for storing the images of faces recognized
for i in range(1,41):
	d[i]=""
for i in range(1,41):
	filename[i]=""
attendance=[]
for co in range(1,41):
	c[co]=1000000
npath='./c_final'
#nbr_emotion
# 1-happy
# 2 - interested
# 3 - sad
# 0 - sleepy
# Append the images with the extension .sad into image_paths
image_paths = [os.path.join(npath, f) for f in os.listdir(npath) if f.endswith('.jpg')]
for image_path in image_paths:
    predict_image_pil = Image.open(image_path).convert('L')
    predict_image = np.array(predict_image_pil, 'uint8')
    faces = faceCascade.detectMultiScale(predict_image)
    for (x, y, w, h) in faces:
        nbr_predicted, conf = recognizer.predict(predict_image[y: y + h, x: x + w])
        nbr_actual = int(os.path.split(image_path)[1].split(".")[0].replace("", ""))
	if(nbr_predicted>=1 and nbr_predicted<=160):
		if(conf<=38):
			nbr_emotion=nbr_predicted%4
			if nbr_predicted in range(1,5):
				nbr_predicted=1
			elif nbr_predicted in range(5,9):			# (2-1)*4+1	
				nbr_predicted=2
			elif nbr_predicted in range(9,13):
				nbr_predicted=3
			elif nbr_predicted in range(13,17):
				nbr_predicted=4
			elif nbr_predicted in range(17,21):
				nbr_predicted=5
			elif nbr_predicted in range(21,25):
				nbr_predicted=6
			elif nbr_predicted in range(25,29):
				nbr_predicted=7
			elif nbr_predicted in range(29,33):
				nbr_predicted=8
			elif nbr_predicted in range(33,37):
				nbr_predicted=9
			elif nbr_predicted in range(37,41):
				nbr_predicted=10
			elif nbr_predicted in range(41,45):
				nbr_predicted=11
			elif nbr_predicted in range(45,49):
				nbr_predicted=12
			elif nbr_predicted in range(49,53):
				nbr_predicted=13
			elif nbr_predicted in range(53,57):
				nbr_predicted=14
			elif nbr_predicted in range(57,61):
				nbr_predicted=15
			elif nbr_predicted in range(61,65):
				nbr_predicted=16
			elif nbr_predicted in range(65,69):
				nbr_predicted=17
			elif nbr_predicted in range(69,73):
				nbr_predicted=18
			elif nbr_predicted in range(73,77):
				nbr_predicted=19
			elif nbr_predicted in range(77,81):
				nbr_predicted=20
			elif nbr_predicted in range(81,85):
				nbr_predicted=21
			elif nbr_predicted in range(85,89):
				nbr_predicted=22
			elif nbr_predicted in range(89,93):
				nbr_predicted=23
			elif nbr_predicted in range(93,97):
				nbr_predicted=24
			elif nbr_predicted in range(97,101):
				nbr_predicted=25
			elif nbr_predicted in range(101,105):
				nbr_predicted=26
			elif nbr_predicted in range(105,109):
				nbr_predicted=27
			elif nbr_predicted in range(109,113):
				nbr_predicted=28
			elif nbr_predicted in range(113,117):
				nbr_predicted=29
			elif nbr_predicted in range(117,121):
				nbr_predicted=30
			elif nbr_predicted in range(121,125):
				nbr_predicted=31
			elif nbr_predicted in range(125,129):
				nbr_predicted=32
			elif nbr_predicted in range(129,133):
				nbr_predicted=33
			elif nbr_predicted in range(133,137):
				nbr_predicted=34
			elif nbr_predicted in range(137,141):
				nbr_predicted=35
			elif nbr_predicted in range(141,145):
				nbr_predicted=36
			elif nbr_predicted in range(145,149):
				nbr_predicted=37
			elif nbr_predicted in range(149,153):
				nbr_predicted=38
			elif nbr_predicted in range(153,157):
				nbr_predicted=39
			elif nbr_predicted in range(157,161):
				nbr_predicted=40
			if(attendance.count(nbr_predicted) == 0):
				attendance.append(nbr_predicted)
                	print "{} (train) is Correctly Recognized with confidence {} against {} (test)".format(nbr_predicted, conf, nbr_actual)
			if(c[nbr_predicted]>conf):
				c[nbr_predicted]=conf
			if(nbr_emotion==1):
				d[nbr_predicted]="happy"
			elif(nbr_emotion==2):
				d[nbr_predicted]="interested"
			elif(nbr_emotion==3):
				d[nbr_predicted]="sad"
			elif(nbr_emotion==0):
				d[nbr_predicted]="sleepy"		

        cv2.imshow("Recognizing Face", predict_image[y: y + h, x: x + w])
        cv2.waitKey(1000)

#print "The minimum confidence level for each person"
f= open("detected_faces.txt","w+")

print attendance
print "Accuracy : "+str(len(attendance)*100/40)+"%"
print
for i in range(1,41):
	if(d[i]!=""):
		print [str(i) + " / " + str(c[i]) + " / " + d[i]]
		if(d[i]=="happy"):
			nbr_orig=(i-1)*4+1
		elif(d[i]=="interested"):
			nbr_orig=(i-1)*4+2
		elif(d[i]=="sad"):
			nbr_orig=(i-1)*4+3
		elif(d[i]=="sleepy"):
			nbr_orig=(i-1)*4+4
		filename[i]=str(nbr_orig)+"."+d[i]
filecount=0
print 
for i in range(1,41):
	print filename[i]
	if(filename[i]!=""):
		filecount = filecount+1
        	f.write('dataset_final/'+filename[i]+"\n")
f.close()


with open("detected_faces.txt", "r") as ins:
    for line in ins:
        img = Image.open(line.strip())
        image={'filename':line.strip(),'img':img}
        arr.append(image)

def plot_gallery(images, n_row=8, n_col=5):
    #Helper function to plot a gallery of portraits
    plt.figure(figsize=(2.8 * n_col, 2.4 * n_row))
    plt.subplots_adjust(bottom=0, left=.01, right=.99, top=.90, hspace=.95)
    for i in range(filecount):
        plt.subplot(n_row, n_col, i + 1)
	var=images[i]['filename'].split('/')[-1].split('.')[0]
	if int(var) in range(1,5):
		var=1
	elif int(var) in range(5,9):			# (2-1)*4+1	
		var=2
	elif int(var) in range(9,13):
		var=3
	elif int(var) in range(13,17):
		var=4
	elif int(var) in range(17,21):
		var=5
	elif int(var) in range(21,25):
		var=6
	elif int(var) in range(25,29):
		var=7
	elif int(var) in range(29,33):
		var=8
	elif int(var) in range(33,37):
		var=9
	elif int(var) in range(37,41):
		var=10
	elif int(var) in range(41,45):
		var=11
	elif int(var) in range(45,49):
		var=12
	elif int(var) in range(49,53):
		var=13
	elif int(var) in range(53,57):
		var=14
	elif int(var) in range(57,61):
		var=15
	elif int(var) in range(61,65):
		var=16
	elif int(var) in range(65,69):
		var=17
	elif int(var) in range(69,73):
		var=18
	elif int(var) in range(73,77):
		var=19
	elif int(var) in range(77,81):
		var=20
	elif int(var) in range(81,85):
		var=21
	elif int(var) in range(85,89):
		var=22
	elif int(var) in range(89,93):
		var=23
	elif int(var) in range(93,97):
		var=24
	elif int(var) in range(97,101):
		var=25
	elif int(var) in range(101,105):
		var=26
	elif int(var) in range(105,109):
		var=27
	elif int(var) in range(109,113):
		var=28
	elif int(var) in range(113,117):
		var=29
	elif int(var) in range(117,121):
		var=30
	elif int(var) in range(121,125):
		var=31
	elif int(var) in range(125,129):
		var=32
	elif int(var) in range(129,133):
		var=33
	elif int(var) in range(133,137):
		var=34
	elif int(var) in range(137,141):
		var=35
	elif int(var) in range(141,145):
		var=36
	elif int(var) in range(145,149):
		var=37
	elif int(var) in range(149,153):
		var=38
	elif int(var) in range(153,157):
		var=39
	elif int(var) in range(157,161):
		var=40	
        label = '\n\nRoll number: %s\n emotion: %s' % (var,images[i]['filename'].split('.')[-1])
        plt.imshow(images[i]['img'], cmap=plt.cm.gray, aspect='equal', extent=None)
        plt.title(label,size = 12)
        plt.xticks(())
        plt.yticks(())


plot_gallery(arr)

plt.show()


		

