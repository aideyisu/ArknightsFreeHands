# 捕获屏幕

from PIL import ImageGrab

px=ImageGrab.grab().load()
for y in range(0,100,10):
    for x in range(0,100,10):
        color=px[x,y]
        print(color)