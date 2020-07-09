import cv2
import numpy as np

cap = cv2.VideoCapture('https://r6---sn-3u-bh2sd.googlevideo.com/videoplayback?expire=1594290145&ei=gZsGX7WBLoG24QKmwrmYBg&ip=39.7.47.38&id=o-AAQ0tewe7qB2ukn4Y-eC2pxQU7shElc9W3QXalNbZ4j9&itag=22&source=youtube&requiressl=yes&mh=0p&mm=31%2C26&mn=sn-3u-bh2sd%2Csn-i3belnls&ms=au%2Conr&mv=m&mvi=6&pcm2cms=yes&pl=24&initcwndbps=1501250&vprv=1&mime=video%2Fmp4&ratebypass=yes&dur=1402.369&lmt=1575387335129835&mt=1594268502&fvip=4&c=WEB&txp=5535432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAPiXryH6MBUYdIhlXr5_O1K-qHA_j6on2wWB-ThymaXXAiEAgAru392pd6GEqYXYs-x1j2CYXVXmuJJQXLjLpl-RiWo%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAPcIYlZjo8CxJagzpDe5qZEijHYAAagx8na0ffG4mshzAiBvTCZOwiRb3R8YTTyrYyvVnMlC3I0tNkorxXuDkoWyKg%3D%3D')            #영상을 캡쳐

while cap.isOpened():                                       #영상이 열려있을 때만 반복
    ret, frame = cap.read()                                 #영상에서 새 프레임을 읽음
    try:
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        flip = np.flip(frame, (0, 1))
        cv2.imshow('window', flip)                         #영상 프레임을 window창에 표시
    except:
        pass
    if cv2.waitKey(1) == ord('q'):                          #키보드 q가 눌리면
        break                                               #반복 중단
cv2.destroyAllWindows()                                     #모든 cv창 종료
