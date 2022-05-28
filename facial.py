import cv2
trained_face_data = cv2.CascadeClassifier('C:\\Users\\Your Shop as\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
#img = cv2.imread('aa..jpg')
webcam = cv2.VideoCapture(0)
while True:
    successful_frame_read ,frame = webcam.read()



    grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(grayscale_img)

    for (x, y, w, h) in face_coordinates:
#(x, y, w, h) = face_coordinates[1]
     cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 255), 2)


    cv2.imshow('newabhi', frame)
    key = cv2.waitKey(1)
    if key==81 or key == 113:
        break




print("code completed")