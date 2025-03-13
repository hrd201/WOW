import pyautogui
import pygetwindow as gw
import time
import threading
import keyboard

# 配置区 --------------------------------------------
WOW_TITLES = ["World of Warcraft", "魔兽世界"]
SPACE_INTERVAL = 120        # 空格组合循环间隔
COMBO_INTERVAL = 60       # 4+3键循环间隔
Q5_INTERVAL = 300          # Q+5组合循环间隔（5分钟）
HOLD_DURATION = 1.0
HOLD_DURATION1 = 1.5         # WASD长按时间
PRESS_DURATION = 0.1       # 普通按键持续时间
# ---------------------------------------------------

# 全局控制
running = True
action_lock = threading.Lock()  # 动作互斥锁

def activate_wow_window():
    """智能窗口激活（带异常处理）"""
    for _ in range(3):
        for title in WOW_TITLES:
            try:
                win = gw.getWindowsWithTitle(title)
                if win and not win[0].isMinimized:
                    win[0].activate()
                    time.sleep(0.3)
                    return True
            except Exception as e:
                print(f"窗口激活异常: {str(e)}")
        time.sleep(1)
    return False

def hold_key(key, duration):
    """长按按键函数"""
    try:
        if activate_wow_window():
            pyautogui.keyDown(key)
            print(f"[{time.strftime('%H:%M:%S')}] 开始按住 {key} 键")
            time.sleep(duration)
            pyautogui.keyUp(key)
            print(f"[{time.strftime('%H:%M:%S')}] 释放 {key} 键")
            return True
    except Exception as e:
        print(f"长按失败: {str(e)}")
    return False

def press_key(key):
    """短按按键函数"""
    try:
        if activate_wow_window():
            pyautogui.keyDown(key)
            time.sleep(PRESS_DURATION)
            pyautogui.keyUp(key)
            print(f"[{time.strftime('%H:%M:%S')}] 点击 {key} 键")
            return True
    except Exception as e:
        print(f"按键失败: {str(e)}")
    return False

def space_ws_task():
    """空格+WS组合任务"""
    while running:
        time.sleep(SPACE_INTERVAL)
        with action_lock:
            print("\n-- 开始执行空格+WS组合 --")
            press_key('space')
            hold_key('w', HOLD_DURATION)
            hold_key('s', HOLD_DURATION1)
            print("-- 空格+WS组合完成 --\n")

def combo_task():
    """4+3键组合任务"""
    while running:
        with action_lock:
            print("\n== 开始执行4+3组合 ==")
            start_time = time.time()
            
            if press_key('4'):
                time.sleep(2)
                for _ in range(2):
                    press_key('3')
                    time.sleep(5)
            
            elapsed = time.time() - start_time
            wait_time = COMBO_INTERVAL - elapsed
            print(f"== 组合执行完成，等待 {wait_time:.1f} 秒 ==")
        time.sleep(wait_time if wait_time > 0 else 0)

def q5_task():
    """Q+5组合任务"""
    while running:
        time.sleep(Q5_INTERVAL)
        with action_lock:
            print("\n** 开始执行Q+5组合 **")
            start_time = time.time()
            
            # 双击Q键
            for _ in range(2):
                press_key('q')
                time.sleep(1)
            
            # 5键和空格组合
            time.sleep(5)
            press_key('5')
            time.sleep(3)
            press_key('space')
            
            elapsed = time.time() - start_time
            wait_time = Q5_INTERVAL - elapsed
            print(f"** 组合执行完成，等待 {wait_time:.1f} 秒 **")
        time.sleep(wait_time if wait_time > 0 else 0)

def stop_script():
    """安全停止脚本"""
    global running
    running = False
    print("\n脚本已安全终止")

if __name__ == "__main__":
    print("魔兽世界五重循环助手 V5.0")
    print("功能清单：")
    print(f"- 每 {SPACE_INTERVAL} 秒：空格 + W/S长按")
    print(f"- 每 {COMBO_INTERVAL//60} 分钟：4→3×2组合")
    print(f"- 每 {Q5_INTERVAL//60} 分钟：Q×2→5→空格组合")
    print("- 全功能互斥执行，无按键冲突\n")
    print("- 按下 F12 停止脚本")

    keyboard.add_hotkey('F12', stop_script)

    threading.Thread(target=space_ws_task, daemon=True).start()
    threading.Thread(target=combo_task, daemon=True).start()
    threading.Thread(target=q5_task, daemon=True).start()

    try:
        while running:
            time.sleep(0.5)
    except KeyboardInterrupt:
        stop_script()
