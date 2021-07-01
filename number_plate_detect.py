import cv2

def save_plate():
  img = cv2.imread("car.jpg")

  #load HAAR cascade
  plate_classifier = cv2.CascadeClassifier("indian_plate.xml")

  gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  plate = plate_classifier.detectMultiScale(gray, 1.3, 7)

  for (x,y,w,h) in plate:
      n_plate = img[y:y+h, x:x+w]

  cv2.imwrite("detected_plate.png", n_plate)