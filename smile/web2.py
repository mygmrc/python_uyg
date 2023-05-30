import cv2
import numpy as np
''' Gerçek zamanli işlemlerde rol oynamaktadir.
 OpenCV kütüphanesi sayesinde web kameralari, video dosyalari veya diğer aygit türleri
 tarafindan bir bilgisayara bağlanan görsel bilgilerin yakalanmasini, analiz edilmesini 
ve değiştirilmesini destekleyen yüzlerce işlev içerir.
'''

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smileCascade = cv2.CascadeClassifier('haarcascade_smile.xml')
 
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,      
        minSize=(30, 30)
    )

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
                
        smile = smileCascade.detectMultiScale(
            roi_gray,
            scaleFactor= 1.5,
            minNeighbors=15,
            minSize=(25, 25),
            )
        
        for i in smile:
            if len(smile)>1:
                cv2.putText(img,"Smiling",(x,y-30),cv2.FONT_HERSHEY_SIMPLEX,
                    2,(0,255,0),3,cv2.LINE_AA)
               
    cv2.imshow('video', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()