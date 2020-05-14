import cv2
import numpy as np
import re, time, os, sys

# color = ['  ', '\033[46m  \033[0m']
color = ['草', '  ']
ZOOM = 15
FORMAT = 'jpg'
RESOLUTION = (1440, 1080)
FPS = 30 if not sys.argv[2] else int(sys.argv[2])


def transform(img_in: np.array):
    reduced = np.zeros((RESOLUTION[1] // ZOOM, RESOLUTION[0] // ZOOM), dtype='i8')
    for j in range(RESOLUTION[1] // ZOOM):
        for i in range(RESOLUTION[0] // ZOOM):
            block = img_in[(j * ZOOM):((j + 1) * ZOOM), (i * ZOOM):((i + 1) * ZOOM), 0]
            avr = block.sum() // (ZOOM ** 2)
            reduced[j, i] = avr
    return reduced


def create_timeline():
    filelist = os.listdir(sys.argv[1])
    timeline = []
    for file in filelist:
        try:
            timeline.append(re.findall(r'(.*)\.' + FORMAT + r'$', file)[0])
        except:
            break
    return timeline


def getpath(s_time: float, c_time: float, timeline: list):
    d = c_time - s_time
    while timeline:
        # print(timeline[0])
        if int(timeline[0]) / FPS > d:
            break
        timeline.pop(0)
    return timeline[0]
    pass


def translate(img_in: np.array):
    str_picture = ""
    for j, line in enumerate(img_in):
        for i, pixel in enumerate(line):
            str_picture += color[0 if pixel < 150 else 1]
        str_picture += "\n"
    return str_picture


if __name__ == '__main__':
    tl = create_timeline()
    start = time.time()
    TOTAL = 0
    count = 0
    fps = 0
    fps_timeflag = time.time()
    os.system('cls')
    print("\033[1000D\033[1000A\033[2J")
    while (len(tl) > 0):
        print(f"FPS:{fps}")
        t = time.time()
        img = cv2.imread("%s\\%s.%s" % (sys.argv[1], getpath(start, t, tl), FORMAT))
        imgstr = translate(transform(img))
        print(imgstr)
        print("\033[1;1H")
        # print("\033[1000D\033[1000A\033[2J")
        # os.system('cls')
        count += 1
        TOTAL += 1
        if t - fps_timeflag > 1:
            fps = count
            count = 0
            fps_timeflag = t
    print(TOTAL)
    print(time.time() - start)
    os.system('cls')
    os.system('pause')