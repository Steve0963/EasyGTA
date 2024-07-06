from threading import Thread
from pystray import Icon, Menu, MenuItem
from PIL import Image

# 假设这些函数来自外部模块
from Scripts import badsport_value
from Utils import restart, exit_click
from Config import AppParmas

value = 3

# 更新 BadSportValue 菜单项的回调函数
def test():
    global value
    value += 1
    print(value)
    # 重新创建菜单项
    menu = Menu(
        # MenuItem(f"测试 : {value} (点击刷新)", test),
        MenuItem(f"BadSportValue : {badsport_value()}", update_bad_sport_value),
        MenuItem("重新加载", restart),
        MenuItem("退出", exit_click)
    )
    AppParmas.Icon.menu = menu

def update_bad_sport_value():

    AppParmas.Icon.menu = Menu(
        # MenuItem(f"测试 : {value} (点击刷新)", test),
        MenuItem(f"恶意值 : {badsport_value()}", update_bad_sport_value),
        MenuItem("重新加载", restart),
        MenuItem("退出", exit_click)
    )

# 创建托盘图标和菜单项
def create_ui():
    icon_image = Image.open(AppParmas.Icon_Path)

    # 初始菜单项
    menu_items = [
        # MenuItem(f"测试 : {value} (点击刷新)", test),
        MenuItem(f"恶意值 : {badsport_value()}", update_bad_sport_value),
        MenuItem("重新加载", restart),
        MenuItem("退出", exit_click)
    ]

    menu = Menu(*menu_items)
    AppParmas.Icon = Icon(
        "Easy GTA5", icon_image, menu=menu, title="Created By QuoVadis8 For GTA5"
    )

    AppParmas.Icon.run()

def init():
    Thread(target=create_ui).start()

