import cv2

cap = cv2.VideoCapture('https://r1---sn-n3cgv5qc5oq-bh2z7.googlevideo.com/videoplayback?expire=1597401699&ei=AxY2X-u7AYndrQTzyo_QDg&ip=119.193.18.123&id=o-AFudcsYgd09DvJt9j3FGA1l1siT3XM4HP5dJSRSFT6Ct&itag=22&source=youtube&requiressl=yes&mh=-A&mm=31%2C26&mn=sn-n3cgv5qc5oq-bh2z7%2Csn-i3b7kn7s&ms=au%2Conr&mv=m&mvi=1&pl=24&initcwndbps=4982500&vprv=1&mime=video%2Fmp4&ratebypass=yes&dur=177.237&lmt=1597309689266205&mt=1597379978&fvip=1&fexp=23883098&c=WEB&txp=6316222&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRQIgPXh5dRZu0XAUh5owuPyr4us_Ne-kK6nEPtwMUnV8Q_0CIQC-YRfsWaE8mPJxxTrc89qt_ZZkiBHnPTKgBR8XZupjiA%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgLmgf2n5U9QA5i1PydE_Mfh13-I4YSE67VOqo2-6sQUkCIFxkDuFQx7uDcohgZ_WO_1JpFltT55uBO1nJz4c6Tn6A')

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
