# -*- coding: utf-8 -*-
"""
    Author:1112
    Date:2023-09-06
    Update: ---
    Achieve:实时获取电脑CPU占用率和内存使用情况
"""
import os
import sys
import time
import psutil

class MonitorCPUMemory:

    def __init__(self,target_pid):
        self.target_pid = target_pid
        self.pid = None
        self.check_pro = False

    def clear_log(self):
        if os.path.exists("text.log"):
            os.remove("text.log")

    def write(self, text1, text2, text3):
        # 写入log中
        timer = time.strftime("%Y-%m-%d %H:%M:%S")
        with open('text.log', 'a+', encoding='utf-8') as tf:
            text = timer + "软件内存占用率= {:.5f}% ，软件cpu使用率为 {}%，系统cpu使用率为 {}%\n".format(text1, text2, text3)
            tf.write(text)

    def check_process(self):
        for i in psutil.pids():
            self.pid = psutil.Process(i)
            if self.pid.pid == self.target_pid:
                self.check_pro = True
                return self.check_pro

    def CM_monitor(self):
        # CPU+内存监控
        self.clear_log()
        while self.check_process():
            print("2222")
            a = self.pid.memory_percent()  # 内存占用%
            b = self.pid.cpu_percent()
            c = psutil.cpu_percent()
            time.sleep(1)
            self.write(a, b, c)

if __name__ == '__main__':
    target_pid = 5220  # 这里修改索要监控的pid
    a = MonitorCPUMemory(target_pid)
    a.CM_monitor()
