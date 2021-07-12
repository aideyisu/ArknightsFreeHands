'''

start /f/mumu/emulator/nemu/EmulatorShell/NemuPlayer.exe

'''

import time
import subprocess

time_start_wait = 30
mumu_helper_url = f"f:\\mumu\\emulator\\nemu\\EmulatorShell\\NemuPlayer.exe"

if __name__ == "__main__":
    # 启动模拟器
    subprocess.Popen(mumu_helper_url)

    # 等待 40秒
    time.sleep(time_start_wait)

    print("yes")
