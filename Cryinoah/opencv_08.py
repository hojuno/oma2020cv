import cv2
import numpy as np

url = {
    'babybus': 'https://r2---sn-n3cgv5qc5oq-bh2ek.googlevideo.com/videoplayback?expire=1594361965&ei=DLQHX6GvPO-D1d8P2vKUgAo&ip=123.214.4.204&id=o-AL6QdjdfdXAjIDefknXpVhGhZwHn62sc87u0rBj9xO-M&itag=22&source=youtube&requiressl=yes&mh=1N&mm=31%2C26&mn=sn-n3cgv5qc5oq-bh2ek%2Csn-i3b7knl6&ms=au%2Conr&mv=m&mvi=2&pl=16&initcwndbps=2345000&vprv=1&mime=video%2Fmp4&ratebypass=yes&dur=1287.894&lmt=1594119660814943&mt=1594340256&fvip=2&c=WEB&txp=5535432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRgIhALR0qP5QurUI6fxoOVlv87dYwkz1Ha3RrhAoKU1wL9baAiEAxIM0M30sFP5RL12IaO6bcDZdw7ZSFYwOKLpua8576Fo%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAOLRRLTd4jCgX4go3V2GeFr2lWa4moNoJHyWAtSjwuCFAiAGD22H1eIK1DRJOdMkkWBTPC5q_dC8miEZR-7HIm_H_g%3D%3D',
    'pinkfong': 'https://r7---sn-n3cgv5qc5oq-bh2ed.googlevideo.com/videoplayback?expire=1594361993&ei=KbQHX866Coem4wLJxb2QDA&ip=123.214.4.204&id=o-AFxGYPuec29xcc6YsQgXN_zfozwdrIubTsVBAN6TDgUh&itag=22&source=youtube&requiressl=yes&mh=EQ&mm=31%2C26&mn=sn-n3cgv5qc5oq-bh2ed%2Csn-i3b7knsd&ms=au%2Conr&mv=m&mvi=7&pl=16&initcwndbps=1937500&vprv=1&mime=video%2Fmp4&ratebypass=yes&dur=1066.678&lmt=1585773739834010&mt=1594340314&fvip=2&c=WEB&txp=5432432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRQIgVcyFNiu9YYj9dm9cQAtGehZ5fYmdH7KQJw1DEgAk8YMCIQDqXR6_7NoqupvLOhvFGSXQgk2QgOnINyW9t6aEAsxsAA%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgO6gN_aPNcV16gHw4q3iyuFnOy3SUhd76aAHhuNvnGh4CICZei0NbJzEkSFOGSxFXv7Y-p5zMqEph545dadQmhhYg'}

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
    # https://en.wikipedia.org/wiki/Nearest-neighbor_interpolatione
    # merged_frame = merge1(frame_1, frame_2, 0.5)
    # merged_frame = merge2(frame_1, frame_2, greater=False)
    # merged_frame = merge3(frame_1, frame_2, greater=True)
    # merged_frame = merge4(frame_1, frame_2, filter_type=2)
    merged_frame = merge5(frame_1, frame_2)
    cv2.imshow('window', merged_frame)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()
