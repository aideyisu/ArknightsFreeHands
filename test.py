# 捕获屏幕

from PIL import ImageGrab

px=ImageGrab.grab().load()
for y in range(0,100,10):
    for x in range(0,100,10):
        color=px[x,y]
        print(color)

# 对程序窗口与桌面截图并保存
# https://blog.csdn.net/zhuisui_woxin/article/details/84345036


# ImageGrab.grab()方法介绍
# https://www.geeksforgeeks.org/pyhton-pil-imagegrab-grab-method/