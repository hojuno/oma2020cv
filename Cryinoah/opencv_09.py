import cv2

cap = cv2.VideoCapture('https://r1---sn-n3cgv5qc5oq-bh2z7.googlevideo.com/videoplayback?expire=1597401699&ei=AxY2X-u7AYndrQTzyo_QDg&ip=119.193.18.123&id=o-AFudcsYgd09DvJt9j3FGA1l1siT3XM4HP5dJSRSFT6Ct&itag=22&source=youtube&requiressl=yes&mh=-A&mm=31%2C26&mn=sn-n3cgv5qc5oq-bh2z7%2Csn-i3b7kn7s&ms=au%2Conr&mv=m&mvi=1&pl=24&initcwndbps=4982500&vprv=1&mime=video%2Fmp4&ratebypass=yes&dur=177.237&lmt=1597309689266205&mt=1597379978&fvip=1&fexp=23883098&c=WEB&txp=6316222&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRQIgPXh5dRZu0XAUh5owuPyr4us_Ne-kK6nEPtwMUnV8Q_0CIQC-YRfsWaE8mPJxxTrc89qt_ZZkiBHnPTKgBR8XZupjiA%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgLmgf2n5U9QA5i1PydE_Mfh13-I4YSE67VOqo2-6sQUkCIFxkDuFQx7uDcohgZ_WO_1JpFltT55uBO1nJz4c6Tn6A')

while True:
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sobel_x = cv2.convertScaleAbs(sobel_x)
        sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        sobel_y = cv2.convertScaleAbs(sobel_y)
        sobel = cv2.addWeighted(sobel_x, 1, sobel_y, 1, 0)
        cv2.imshow('sobel X', sobel_x)
        cv2.imshow('sobel Y', sobel_y)
        cv2.imshow('sobel', sobel)
        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
