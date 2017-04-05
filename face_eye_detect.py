import cv2
import sys

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cap = cv2.VideoCapture(sys.argv[1]) 
g1=sys.argv[1]
g2=g1[-5:-4]
g=int(g2)
i = (g-1)*500 + 1
#i=1
#cap=cv2.VideoCapture('c6.MP4')
flag = False
count=0
while (cap.isOpened()):
	if count%100==0:
		ret, img = cap.read()
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
		for(x,y,w,h) in faces:
			cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
			roi_gray = gray[y:y+h, x:x+w]
			roi_color = img[y:y+h, x:x+w]
			#if not flag:
			imgpath='c_final/'+str(i)+'.jpg'
			cv2.imwrite(imgpath , roi_color )
			#eyes = eye_cascade.detectMultiScale(roi_gray,scaleFactor=1.3,minNeighbors=5,minSize=(30, 30))
			#for(ex,ey,ew,eh) in eyes:
			#	cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
			i=i+1
			if i%500==1:
				break
	count = count+1
	cv2.imshow('img',img)
	if (cv2.waitKey(1) & 0xFF == ord('q')) or (i%500==1):
        	break

cap.release()
cv2.destroyAllWindows()

