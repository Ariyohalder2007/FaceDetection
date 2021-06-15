import cv2
path='Face.jpg'
cap=cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
faceCascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    sucess, img=cap.read()
    imgGray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces= faceCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

