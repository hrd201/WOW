<MARKDOWN>
# wow世界怀旧服猎人抓宠自动化助手
- 功能自动蹲守宠物，旁边最好是有其他野怪，这样能防止掉线
- 机制：选取目标指定抓获，如果没有目标就选取可见野怪射击、假死触发系统机制防止掉线
## 🚀 核心功能

| 功能名称         | 间隔时间   | 操作序列                           | 互斥机制  |
|------------------|------------|------------------------------------|-----------|
| 空格+WS组合      | 60秒       | `空格` → `W长按3秒` → `S长按3秒`  | 🔒 共享锁 |
| 4+3技能连击      | 120秒      | `4` → 等待2秒 → `3×2次(间隔5秒)`  | 🔒 共享锁 |
| Q+5爆发循环      | 300秒      | `Q×2次(间隔1秒)` → 等待5秒 → `5` → 等待3秒 → `空格` | 🔒 共享锁 |

```python
with action_lock:  # 关键段保护
    perform_actions()
```

**热键监控系统**  
`F12` 一键安全终止所有进程

---

## 📥 快速开始

### 环境要求
- Python 3.8+
- 依赖库：`pip install pyautogui pygetwindow keyboard`

### 配置指南
```python
# 🔧 核心参数配置
WOW_TITLES = ["World of Warcraft", "魔兽世界"]  # 窗口标题
SPACE_INTERVAL = 60    # 空格循环间隔(秒)
COMBO_INTERVAL = 120   # 技能连击间隔(秒) 
Q5_INTERVAL = 300      # 爆发循环间隔(秒)
HOLD_DURATION = 3.0    # 长按持续时间
```

### 启动命令
```bash
python wow_assistant.py
```

---

## 🛑 安全措施
- 窗口最小化时自动跳过操作
- 单次操作超时保护机制
- 异常错误日志记录
- 系统资源占用监控

---
## 按键设置
按键5 放假死

按键4 放冰霜陷阱

按键3 放一个宏
- #showtooltip 驯服野兽
- /cleartarget
- /target 狮王休玛
- /stopmacro [noexists][dead]
- /script RetrieveCorpse()
- /castsequence reset=60/combat 冰冻陷阱,驯服野兽,
- /stopattack

按键Q 放一个宏
- #showtooltip
- /startatta
- /cast !自动射击
- /cast 奥术射击
- /petattack

## ⚠️ 重要提示
- 需要以管理员身份运行
- 游戏需设置为窗口化/无边框模式
- 确保游戏界面不被遮挡
- 首次使用前在沙盒环境测试

---

## 📜 许可协议
MIT License © 2023 [hrd201]
