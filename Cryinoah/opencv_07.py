import cv2
import numpy as np

cap = cv2.VideoCapture(
    'https://r2---sn-n3cgv5qc5oq-bh2ek.googlevideo.com/videoplayback?expire=1594375951&ei=r-oHX57dFeaElQSpv7r4Dg&ip=119.193.18.123&id=o-AAp6A3oy0jmlrExBIgeHOe63z09I4skl4fEniRC2IZ2A&itag=22&source=youtube&requiressl=yes&mh=1N&mm=31%2C26&mn=sn-n3cgv5qc5oq-bh2ek%2Csn-i3belnel&ms=au%2Conr&mv=m&mvi=2&pl=24&initcwndbps=955000&vprv=1&mime=video%2Fmp4&ratebypass=yes&dur=1287.894&lmt=1594119660814943&mt=1594354293&fvip=2&c=WEB&txp=5535432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRQIgcah5ne_Di7NIpoJF4QjHT7Wjy3YgxgteQBJoXG1tDSsCIQDn3lUOnwISS4ZJWsd7aUD6khwQw0UjKXwOFsrMfL0wJA%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgd71o81S2bwv6IpAs9KASqsR-S7GwjqDK2MABiWMY5QcCIFyKqJ_hW4JJa6viD1okeMuHccsKdwtsY7mQAkzZwoFo')

def nothing(x):
    pass

cv2.namedWindow('window', cv2.WINDOW_AUTOSIZE)

cv2.createTrackbar('RED', 'window', 0, 100, nothing)
cv2.createTrackbar('GREEN', 'window', 0, 100, nothing)
cv2.createTrackbar('BLUE', 'window', 0, 100, nothing)

cv2.setTrackbarPos('RED', 'window', 50)
cv2.setTrackbarPos('GREEN', 'window', 50)
cv2.setTrackbarPos('BLUE', 'window', 50)


def colorize(frame):
    r = cv2.getTrackbarPos('RED', 'window')/100
    g = cv2.getTrackbarPos('GREEN', 'window')/100
    b = cv2.getTrackbarPos('BLUE', 'window')/100
    filter = np.array([b,g,r])
    new_frame = frame[:, :] * filter
    new_frame = new_frame.astype(np.uint8)
    return new_frame


while cap.isOpened():
    ret, frame = cap.read()
    color_frame = colorize(frame)
    cv2.imshow('window', color_frame)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()
