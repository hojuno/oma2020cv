import cv2

cap = cv2.VideoCapture(
    'https://r3---sn-n3cgv5qc5oq-bh2z7.googlevideo.com/videoplayback?expire=1594328853&ei=tTIHX_TzMZGPlQTP85wI&ip=123.214.4.204&id=o-AIpzYQjs9wDzXymX0io096cI9rlkZ2kplqy3NlNkH_HN&itag=22&source=youtube&requiressl=yes&mh=f8&mm=31%2C26&mn=sn-n3cgv5qc5oq-bh2z7%2Csn-i3beln76&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1513750&vprv=1&mime=video%2Fmp4&ratebypass=yes&dur=1467.036&lmt=1553556328440939&mt=1594307140&fvip=3&c=WEB&txp=5535432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAPiPtfZLHdxQjSGVNP5vqATsIoNCTFsQ5b-fKZtBqAqYAiEA0-K1YCAjlVBJE5uFtrEGFHPobISIIDokjQJ2XGSgmgM%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgMDfG47KWXNo4yYgGOy8rptuLO7HbnpGUyIdTJegT4ygCIFUpfuXQNWBM8qZOTBybQUSM8AetrAkO1x-TM4QZh8Nc')  # 영상을 캡쳐


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
