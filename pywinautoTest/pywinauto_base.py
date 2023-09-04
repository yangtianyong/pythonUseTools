# -*- coding: utf-8 -*-
"""
    Author:1112
    Date:2023-09-04
    Update: ---
    Achieve:pywinauto知识点记录
"""

'''
    链接资料:
        具体例子：https://www.cnblogs.com/xp1315458571/p/13892205.html#_lab20_1
        pywinauto作者个人网页，可以提问：https://stackoverflow.com/users/3648361/vasily-ryabov
        github连接：https://github.com/yangtianyong/pywinauto
'''

'''
    使用UIspy进行元素的定位，定位属性一般使用：ClassName、Name、ProcessId、AutomationId
    pywinauto:
    支持控件访问技术：Win32 API MS UI Automation  uia
    Application:作用范围是一个进程，如一般桌面应用程序
    Desktop:作用范围可以跨进程，主要用于一个程序可以包含多个进程(实例)的程序
    辅助检查工具：Inspect.exe、spy++.exe、ViewWizard、UISpy.exe

    控件分类：
    状态栏：StatusBar          静态内容：Static
    按钮：Button               复选框：CheckBox
    单选框：RadioButton        组框：GroupBox
    组合框：ComboBox           对话框：Dialog
    编辑栏：Edit               头部内容：Header
    列表框：ListBox            选项卡控件：TabControl
    工具栏：Toolbar            工具提示：ToolTips
    树状视图：Tree View         菜单：Menu
    菜单项：MenuItem            窗格：Pane
'''

from pywinauto import Application
from pywinauto.keyboard import send_keys
import time
from pywinauto import mouse

# --------------------------  启动软件和连接已经打开的软件  ------------------------------------
# 使用地址来启动软件
# app = Application(backend="uia").start(r"D:\notepad\Notepad++\notepad++.exe")
# 连接已经打开的应用程序 -- 方式一：通过进程号  -- 方式二：通过窗口句柄 --- 可以通过ViewWizard查看到
# app = Application("uia").connect(process=4132)


# --------------------------  选择窗口  ----------------------------------------------------
#获取应用程序所有的窗口
# app.windows()
# 根据类名选择窗口
# dlg = app["Notepad++"]
# 根据标题选择窗口
# dlg = app["new 1 - Notepad++"]
# 打印窗口中所有的控件
# dlg.print_control_identifiers()

# --------------------------  窗口操作  ----------------------------------------------------
#窗口最大化
# dlg.maximize()
#窗口最小化
# dlg.minimize()
#窗口恢复正常大小
# dlg.restore()
#查看窗口显示状态,最大化：1；正常：0
# dlg.get_show_state()
#关闭窗口
# dlg.close()
#获取窗口坐标 -- 这个后续可能会用到
# rect = dlg.rectangle()
# print(rect)

# --------------------------  窗口控件选择  ------------------------------------------------
#选择控件
# menu = dlg["应用程序Menu"]
#  这种方式有时候会选择失效，则需要用下面一种方法选取
#file1 = menu["文件(F)"]
# file = menu.child_window(title="文件(F)")

# --------------------------  获取控件属性  ------------------------------------------------
#查看控件类型
# print(menu.wrapper_object())
# print(file.wrapper_object())
#获取控件文本内容
# print(file.texts())
#获取控件子元素
# print(menu.children())
#获取控件类名
# print(dlg.class_name())
#获取控件属性，返回值是字典
# print(menu.get_properties())
#窗口和控件截图处理  #若报错，运行 pip install image
# pic = dlg.capture_as_image()
# print(pic)
# pic.save("01.png")

# --------------------------  获取子菜单项  ------------------------------------------------
# 获取菜单的子菜单项
# print(menu.items())
#通过下标选择菜单项
# m = menu.item_by_index(0)
#通过路径选择菜单项
# T_save = menu.item_by_path("搜索->替换(R)...")
# T_save = menu.item_by_path("文件")

# --------------------------  菜单项点击  --------------------------------------------------
#点击菜单项
# file.click_input()
# T_save.click_input()

# --------------------------  等待机制 ----------------------------------------------------
'''
    等待机制： wait()方法：
    参数：wait_for:
        exists:表示该窗口是有效的句柄
        visible:表示该窗口未隐藏
        enabled:表示未禁用的窗口
        ready:表示该窗口可见并启用
        active：表示该窗口处于活动状态
    timeout:超时时间
    retry_interval:重试时间间隔
'''

#连接新的窗口
# new_dlg = app["另存为"]  # 这种情况有时候会报错，可以使用下面的方法
# new_dlg = dlg.child_window(title="替换")
# new_dlg.print_control_identifiers()
# new_dlg.wait(wait_for="ready",timeout=10,retry_interval=1)
# print("等待通过")

# --------------------------  键盘操作模块 -------------------------------------------
#按F1
# send_keys("{F1}")   #或者 send_keys("{VK_F1}")
#输入字母
# send_keys("A")

#example 通过按键操作进入cmd  打开python
# send_keys("{VK_LWIN}")
# send_keys("cmd")
# send_keys("{VK_RETURN}")
# send_keys("{VK_LWIN}cmd{VK_RETURN}")
# #延时等待
# time.sleep(2)
# send_keys("python")
# send_keys("{VK_RETURN}")

# --------------------------  键盘操修饰符 --------------------------------------------
'''
    "+"   -> 按Shift
    "^"   -> 按Ctrl
    "%"   -> 按Alt
    "^s"  -> 按Ctrl+S进行保存的操作
'''
# send_keys("^+n")

'''
    click            鼠标单击
    double_click     鼠标双击
    right_click      鼠标右击
    wheel_click      鼠标中间点击
'''
# mouse.click(coords=())       # 鼠标左键 通过像素坐标确认位置
# mouse.right_click(coords=)   # 鼠标右键 通过像素坐标确认位置
# mouse.double_click(coords=)  # 鼠标双击 通过像素坐标确认位置
#按下鼠标,运行后鼠标不会主动释放
# mouse.press(coords=)
#释放鼠标
# mouse.release(coords=)
#滑动鼠标滚轮 wheel_dist滚动的次数  +-表示往上滚动或者往下滚动
# mouse.scroll(coords=(),wheel_dist=1)
#移动鼠标位置
# mouse.move(coords=)

def exampleNotpad():
    #运行
    app = Application(backend="uia").start(r"D:\notepad\Notepad++\notepad++.exe")
    #连接主窗口
    dlg = app["Notepad++"]
    # 写入内容
    dlg["Pane0"].type_keys("hello, pywinauto")
    #菜单栏
    menu = dlg["应用程序Menu"]
    #选择
    T_repl = menu.item_by_path("搜索->替换(R)...")
    #点击
    T_repl.click_input()
    # 选择新窗口
    repl = dlg["替换"]
    # repl = dlg.child_window(title="替换")
    repl.wait(wait_for="ready",timeout=10,retry_interval=1)
    print("替换窗口ready检测成功")
    #查找新窗口下所有属性
    repl.print_control_identifiers()
    #选择查找目标编辑框
    repl.child_window(title="Edit")
    #工具类型的控件不能直接输入内容，需要点击选中 -- 从键盘输入

# exampleNotpad()

'''
    备注：
    1、有一些控件无法点击，需要通过鼠标的操作实现点击的功能;
    2、行为封装;
    3、一般会与其他工具结合起来：Unittest、Selenium;
    
'''