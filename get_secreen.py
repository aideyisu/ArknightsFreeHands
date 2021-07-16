
import win32gui
import win32api
classname = "MozillaWindowClass"
# titlename = "MuMu模拟器"
titlename = "明日方舟 - MuMu模拟器"
#获取句柄
hwnd = win32gui.FindWindow(0, titlename)

#获取窗口左上角和右下角坐标
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
print(left, top, right, bottom)

ww = right - left
hh = bottom - top

print(ww, hh)
# 来源
# https://blog.csdn.net/weixin_33595571/article/details/92751255