import os
pics = os.listdir()
COUNT = 0
for pic in pics:
    os.rename(pic, "badapple-%05d.jpg"%COUNT)
    COUNT += 1