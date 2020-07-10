import cv2
import numpy as np

url = {
    'babybus': 'https://r2---sn-n3cgv5qc5oq-bh2ek.googlevideo.com/videoplayback?expire=1594375951&ei=r-oHX57dFeaElQSpv7r4Dg&ip=119.193.18.123&id=o-AAp6A3oy0jmlrExBIgeHOe63z09I4skl4fEniRC2IZ2A&itag=22&source=youtube&requiressl=yes&mh=1N&mm=31%2C26&mn=sn-n3cgv5qc5oq-bh2ek%2Csn-i3belnel&ms=au%2Conr&mv=m&mvi=2&pl=24&initcwndbps=955000&vprv=1&mime=video%2Fmp4&ratebypass=yes&dur=1287.894&lmt=1594119660814943&mt=1594354293&fvip=2&c=WEB&txp=5535432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRQIgcah5ne_Di7NIpoJF4QjHT7Wjy3YgxgteQBJoXG1tDSsCIQDn3lUOnwISS4ZJWsd7aUD6khwQw0UjKXwOFsrMfL0wJA%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgd71o81S2bwv6IpAs9KASqsR-S7GwjqDK2MABiWMY5QcCIFyKqJ_hW4JJa6viD1okeMuHccsKdwtsY7mQAkzZwoFo',
    'pinkfong': 'https://r5---sn-n3cgv5qc5oq-bh2ll.googlevideo.com/videoplayback?expire=1594375999&ei=3-oHX8TZBPScs8IP4Oa3uA4&ip=119.193.18.123&id=o-AIeu8cmURr0O4Y7h-PSi2uhnbKjLWYjfLZX5ByFodRXp&itag=22&source=youtube&requiressl=yes&mh=qu&mm=31%2C26&mn=sn-n3cgv5qc5oq-bh2ll%2Csn-i3belnls&ms=au%2Conr&mv=m&mvi=5&pl=24&initcwndbps=2408750&vprv=1&mime=video%2Fmp4&ratebypass=yes&dur=88.189&lmt=1594164177547661&mt=1594354293&fvip=5&c=WEB&txp=5535432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRQIgKQH7PSx00l7ho0c2lnAkoQ2yTwGWURfDwjWbuh8hNxMCIQCH8xiuakVoRLZ9ioflRBlQ4paQ_EDjml4S679dUJHOEg%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgb6UkuI4znshlJZaylmKTSe_zO6jZ0nSAUH9HA0SS5EECIQCcSDJL7lHQJ641RrLLaQ3CMqUKe8MAoipoKm6YDGuybw%3D%3D'}

cap_1 = cv2.VideoCapture(url['babybus'])
cap_2 = cv2.VideoCapture(url['pinkfong'])


def merge1(f1, f2, ratio):
    new_frame = ratio * f1 + (1 - ratio) * f2
    new_frame = new_frame.astype(np.uint8)
    return new_frame


def merge2(f1, f2, greater=True):
    if greater:
        comparison = np.greater(f1, f2)
    else:
        comparison = np.less(f1, f2)
    new_frame = comparison * f1 + np.logical_not(comparison) * f2
    return new_frame


def merge3(f1, f2, greater=True):
    f1_gray = cv2.cvtColor(f1, cv2.COLOR_BGR2GRAY)
    f2_gray = cv2.cvtColor(f2, cv2.COLOR_BGR2GRAY)

    if greater:
        comparison = np.greater(f1_gray, f2_gray)
    else:
        comparison = np.less(f1_gray, f2_gray)
    comparison = np.expand_dims(comparison, 2)
    new_frame = comparison * f1 + np.logical_not(comparison) * f2
    return new_frame


def merge4(f1, f2, filter_type=0):
    filters = [np.array([[0, 1], [1, 0]]), np.array([[0, 1], [0, 1]]), np.array([[1, 1], [0, 0]])]
    filter = np.tile(filters[filter_type], (int(f1.shape[0] / 2), int(f1.shape[1] / 2)))
    filter = np.expand_dims(filter, 2)
    new_frame = filter * f1 + np.logical_not(filter) * f2
    new_frame = new_frame.astype(np.uint8)
    return new_frame


def merge5(f1, f2, height=0):
    if height == 0:
        height, width, depth = f1.shape
        f1_resized = f1
        f2_resized = f2
    else:
        width = height/f1.shape[0]*f1.shape[1]
        f1_resized = cv2.resize(f1, (width, height), interpolation=cv2.INTER_CUBIC)
        f2_resized = cv2.resize(f2, (width, height), interpolation=cv2.INTER_CUBIC)
    new_frame = np.zeros((height, width*2, 3), dtype=np.uint8)
    new_frame[:, :width] = f1_resized
    new_frame[:, width:] = f2_resized
    return new_frame


while cap_1.isOpened() and cap_2.isOpened():
    ret, frame_1 = cap_1.read()
    ret, frame_2 = cap_2.read()
    frame_2 = cv2.resize(frame_2, (frame_1.shape[1], frame_1.shape[0]), interpolation=cv2.INTER_CUBIC)
    # https://en.wikipedia.org/wiki/Nearest-neighbor_interpolation
    merged_frame = merge1(frame_1, frame_2, 0.5)
    # merged_frame = merge2(frame_1, frame_2, greater=False)
    # merged_frame = merge3(frame_1, frame_2, greater=True)
    # merged_frame = merge4(frame_1, frame_2, filter_type=0)
    # merged_frame = merge5(frame_1, frame_2)
    cv2.imshow('window', merged_frame)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()
