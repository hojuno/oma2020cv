import cv2

cap = cv2.VideoCapture('http://ca4.desco.com:8082/mjpg/video.mjpg?overview=0&camera=1')            #영상을 캡쳐

while cap.isOpened():                                       #영상이 열려있을 때만 반복
    ret, frame = cap.read()                                 #영상에서 새 프레임을 읽음
    try:
        cv2.imshow('window', frame)                         #영상 프레임을 window창에 표시
    except:
        pass
    if cv2.waitKey(1) == ord('q'):                          #키보드 q가 눌리면
        break                                               #반복 중단
cv2.destroyAllWindows()                                     #모든 cv창 종료
