import os
import cv2

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '../videos/nyan_cat.mp4')
cap = cv2.VideoCapture(filename)                            #영상을 캡쳐
fps = cap.get(5)

while cap.isOpened():                                       #영상이 열려있을 때만 반복
    ret, frame = cap.read()                                 #영상에서 새 프레임을 읽음
    cv2.imshow('window', frame)                             #영상 프레임을 window창에 표시
    if cv2.waitKey(int(1000/fps)) == ord('q'):              #키보드 q가 눌리면
        break                                               #반복 중단
cv2.destroyAllWindows()                                     #모든 cv창 종료
