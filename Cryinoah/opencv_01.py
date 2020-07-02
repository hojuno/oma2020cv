import os
import cv2

dirname = os.path.dirname(__file__)                         #현재 파일의 위치
filename = os.path.join(dirname, '../images/trump.jpg')     #현재 위치로 부터 원하는 파일의 [상대적 위치]
img = cv2.imread(filename)                                  #이미지 열어서 img에 저장

while True:                                                 #무조건 반복
    cv2.imshow('window', img)                                #img를 window창에 표시
    if cv2.waitKey(1) == ord('q'):                          #키보드 q가 눌리면
        break                                               #반복 중단
cv2.destroyAllWindows()                                     #모든 cv창 종료
