import cv2
''' Gerçek zamanlı işlemlerde rol oynamaktadır.
 OpenCV kütüphanesi sayesinde web kameraları, video dosyaları veya diğer aygıt türleri
 tarafından bir bilgisayara bağlanan görsel bilgilerin yakalanmasını, analiz edilmesini 
ve değiştirilmesini destekleyen yüzlerce işlev içerir.
'''
#Sınıflandırıcıları yükleriz
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

cap = cv2.VideoCapture(0)

while True:
    #fotoğrafları kare kare oku
    ret, frame = cap.read()

    #gri renge çevir
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #yüzleri arar
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    #yüzün x,y kordinatı; genişliği ve yüksekliği dörtgenin ayarlanması
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        #gülümsemeyi bulduktan sonra çıkarırız
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        #çıkardıktan sonra gülümsemeyi algılarız
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)

        #gülümsemeleri getirip etrafında dörtgen çizeriz
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2)
        
    #görüntüyü listeleriz
    cv2.imshow('frame', frame)
    
    #bitirmek için ‘q’ ya basalım
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#kamerayı bırakırız ve pencereleri kapatırız
cap.release()
cv2.destroyAllWindows()
