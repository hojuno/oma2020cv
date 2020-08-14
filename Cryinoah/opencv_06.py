import cv2

cap = cv2.VideoCapture(
    'https://r2---sn-n3cgv5qc5oq-bh2ek.googlevideo.com/videoplayback?expire=1594375951&ei=r-oHX57dFeaElQSpv7r4Dg&ip=119.193.18.123&id=o-AAp6A3oy0jmlrExBIgeHOe63z09I4skl4fEniRC2IZ2A&itag=22&source=youtube&requiressl=yes&mh=1N&mm=31%2C26&mn=sn-n3cgv5qc5oq-bh2ek%2Csn-i3belnel&ms=au%2Conr&mv=m&mvi=2&pl=24&initcwndbps=955000&vprv=1&mime=video%2Fmp4&ratebypass=yes&dur=1287.894&lmt=1594119660814943&mt=1594354293&fvip=2&c=WEB&txp=5535432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRQIgcah5ne_Di7NIpoJF4QjHT7Wjy3YgxgteQBJoXG1tDSsCIQDn3lUOnwISS4ZJWsd7aUD6khwQw0UjKXwOFsrMfL0wJA%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgd71o81S2bwv6IpAs9KASqsR-S7GwjqDK2MABiWMY5QcCIFyKqJ_hW4JJa6viD1okeMuHccsKdwtsY7mQAkzZwoFo')


def gray(frame):
    new_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return new_frame


def binary(frame, threshold):
    ret, new_frame = cv2.threshold(frame, threshold, 255, cv2.THRESH_BINARY)
    return new_frame


while cap.isOpened():
    ret, frame = cap.read()
    gray_frame = gray(frame)
    binary_frame = binary(gray_frame, 128)
    cv2.imshow('window', binary_frame)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()
