import cv2
import numpy as np

cap = cv2.VideoCapture(
    'https://r2---sn-n3cgv5qc5oq-bh2ek.googlevideo.com/videoplayback?expire=1594361965&ei=DLQHX6GvPO-D1d8P2vKUgAo&ip=123.214.4.204&id=o-AL6QdjdfdXAjIDefknXpVhGhZwHn62sc87u0rBj9xO-M&itag=22&source=youtube&requiressl=yes&mh=1N&mm=31%2C26&mn=sn-n3cgv5qc5oq-bh2ek%2Csn-i3b7knl6&ms=au%2Conr&mv=m&mvi=2&pl=16&initcwndbps=2345000&vprv=1&mime=video%2Fmp4&ratebypass=yes&dur=1287.894&lmt=1594119660814943&mt=1594340256&fvip=2&c=WEB&txp=5535432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRgIhALR0qP5QurUI6fxoOVlv87dYwkz1Ha3RrhAoKU1wL9baAiEAxIM0M30sFP5RL12IaO6bcDZdw7ZSFYwOKLpua8576Fo%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAOLRRLTd4jCgX4go3V2GeFr2lWa4moNoJHyWAtSjwuCFAiAGD22H1eIK1DRJOdMkkWBTPC5q_dC8miEZR-7HIm_H_g%3D%3D')

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
    filter = np.array([r,g,b])
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
