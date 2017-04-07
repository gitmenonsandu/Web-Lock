
# coding: utf-8

# In[36]:

import cv2
import time
import pandas as pd
import cv2,os
import numpy as np
from PIL import Image
def make_dataset(name):
    cam = cv2.VideoCapture(0)
    detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    import csv   
    sampleNum=0
    data=pd.read_csv('userdata.csv')
    Id=len(data['Id'])+1
    fields=[Id,name]
    with open(r'userdata.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
        
    i=0
    userlist={}
    with open('userdata.csv') as csvfile:
        reader=csv.reader(csvfile)
        for row in reader:
            if i==0:
                i=1
                continue
            print row
            userlist[row[0]]=row[1]
    
    Id=str(Id)
    while(True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

            #incrementing sample number 
            sampleNum=sampleNum+1
            #saving the captured face in the dataset folder
            cv2.imwrite("dataset/User."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])

            cv2.imshow('frame',img)
        #wait for 100 miliseconds 
        time.sleep(0.2)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
        # break if the sample number is morethan 20
        elif sampleNum>30:
            break

    cam.release()
    cv2.destroyAllWindows()
    return userlist


def train_dataset():

    
    recognizer = cv2.createLBPHFaceRecognizer()
    detector= cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
    
    faces,Ids = getImagesAndLabels('dataset')
    recognizer.train(faces, np.array(Ids))
    recognizer.save('trainner/trainner.yml')



def getImagesAndLabels(path):
    recognizer = cv2.createLBPHFaceRecognizer()
    detector= cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
    
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    #create empth face list
    faceSamples=[]
    #create empty ID list
    Ids=[]
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        pilImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        imageNp=np.array(pilImage,'uint8')
        #getting the Id from the image
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces=detector.detectMultiScale(imageNp)
        #If a face is there then append that in the list as well as Id of it
        for (x,y,w,h) in faces:
            faceSamples.append(imageNp[y:y+h,x:x+w])
            Ids.append(Id)
    return faceSamples,Ids


# In[71]:
import cv2
import numpy as np
def predict_face(userlist):

    
    print userlist

    recognizer = cv2.createLBPHFaceRecognizer()
    recognizer.load('trainner/trainner.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);


    count=0
    cam = cv2.VideoCapture(0)
    font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
    flag=False
    while True:
        if flag:
            break
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
            if(conf<70):
                print Id
                Id= userlist.get(str(Id))
                count+=1
                if count==5:
                    flag=True
                    break
            else:
                Id="Unknown"
            cv2.cv.PutText(cv2.cv.fromarray(im),str(Id), (x,y+h),font, 255)
        cv2.imshow('im',im) 
        if cv2.waitKey(10) & 0xFF==ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()
    
    if flag:
        return Id
    else:
        return -1

