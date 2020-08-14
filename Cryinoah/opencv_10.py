import cv2

cap = cv2.VideoCapture(0)

def nothing(x):
    pass

cv2.namedWindow('canny', cv2.WINDOW_AUTOSIZE)

cv2.createTrackbar('MIN', 'canny', 0, 255, nothing)
cv2.createTrackbar('MAX', 'canny', 0, 255, nothing)


cv2.setTrackbarPos('MIN', 'canny', 50)
cv2.setTrackbarPos('MAX', 'canny', 200)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    min = cv2.getTrackbarPos('MIN', 'canny')
    max = cv2.getTrackbarPos('MAX', 'canny')
    canny = cv2.Canny(gray, min, max)
    cv2.imshow('canny', canny)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()