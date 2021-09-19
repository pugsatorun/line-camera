import cv2

deviceid=1 # it depends on the order of USB connection. 
# capture = cv2.VideoCapture(deviceid)
capture = cv2.VideoCapture(0)

ret, frame = capture.read()
cv2.imwrite('test.jpg', frame)
