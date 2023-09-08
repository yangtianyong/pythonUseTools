# -*- coding: utf-8 -*-
"""
    Author:1112
    Date:2023-09-06
    Update: ---
    Achieve:根据进程名获取进程号
"""

'''
    1、获取电脑CPU和内存使用情况是性能测试中一点；
    2、真实的性能测试涉及范围更广更深入;
    3、由于是监控程序，自身不能占用过多的内存，这里仅记录数据，不做其他判断；
    4、为了消耗较小的内存，在目标软件使用期间，记录数据和处理数据分开进行；
    5、可以优化点：输入判断、进程判断、设置停止记录信息点、log文件备份等
'''

'''
    注意：记录的初始时间一般为软件启动加载完成的时刻，可以认为是打开软件可以开始使用了
'''

import sys
import psutil
import os
import time

class MonitorCPUMemory:

    def __init__(self):
        self.process_list = ["NineSimPlatform.exe","hw.exe","notepad++.exe"]
        self.process_pid = None
        self.process_name = None
        self.internal = 1

    #获取进程pid
    def get_process_pid(self):
        while True:
            print('please choose process name: "1 for NineSimPlatform"  "2 for Hypermesh" "3 for notepad++"')
            #在这里并没有对输入数据做判断处理：是否为纯数字 -- isdigit()
            choose  = int(input("请输入对应的数字： "))
            if choose not in [1,2,3]:
                continue
            self.process_name = self.process_list[choose-1]
            break
        pids = psutil.process_iter()
        for pid in pids:
            if (pid.name()==self.process_name):
                self.process_pid = pid
        return self.process_pid

    #判断进程是否存在
    def check_process(self):
        if self.get_process_pid():
            print("*** 进程名为" + self.process_name + "的进程号为：" + str(self.process_pid.pid) + " ***")
        else:
            print(self.process_name + "进程不存在，请启动进程")

    #log文件数据清空
    def clear_log(self):
        if os.path.exists("CPU_Mem.log"):
            os.remove("CPU_Mem.log")

    #写入数据到log中
    def write(self, text1, text2, text3):
        # 写入log中
        timer = time.strftime("%Y-%m-%d %H:%M:%S")
        with open('CPU_Mem.log', 'a+', encoding='utf-8') as tf:
            text = timer + "，软件内存占用率= {:.3f}%，软件cpu使用率为 {}%，系统cpu使用率为 {}%\n".format(text1, text2, text3)
            tf.write(text)

    #获取数据
    def CM_monitor(self):
        self.clear_log()
        while self.process_pid:
            a = self.process_pid.memory_percent()  # 内存占用%
            b = self.process_pid.cpu_percent()
            c = psutil.cpu_percent()
            time.sleep(self.internal)
            self.write(a, b, c)

if __name__ == '__main__':
    getproce = MonitorCPUMemory()
    getproce.check_process()
    getproce.CM_monitor()

