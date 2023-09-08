# -*- coding: utf-8 -*-
"""
    Author:1112
    Date:2023-09-08
    Update: ---
    Achieve:解析数据，作图
"""

import re
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

x_time    = []
y_softcpu = []
y_softmem = []
y_syscpu  = []

class show_data:
    def __int__(self):
        pass
    def read_log(self):
        with open("CPU_Mem.log",'r',encoding="utf-8") as log:
            for line in log:
                # 去除行末尾的换行符
                line = line.rstrip('\n')
                # 使用逗号分割行数据
                x_time.append(line.split('，')[0])
                y_softcpu.append(line.split('，')[1])
                y_softmem.append(line.split('，')[2])
                y_syscpu.append(line.split('，')[3])

    def data_proce(self):
        begin_time = datetime.strptime(x_time[0], '%Y-%m-%d %H:%M:%S')
        pattern = r"(\d+\.\d+)%"
        for num in range(len(x_time)):
            #时间
            lis_time = datetime.strptime(x_time[num], '%Y-%m-%d %H:%M:%S')
            x_time[num] =float((lis_time - begin_time).total_seconds())

            #y_softcpu
            y_softcpumatch = match = re.search(pattern, y_softcpu[num])
            y_softcpu[num] = float(y_softcpumatch.group(1))

            #y_softmem
            y_softmemmatch = match = re.search(pattern, y_softmem[num])
            y_softmem[num] = float(y_softmemmatch.group(1))

            #y_syscpu
            y_syscpumatch = match = re.search(pattern, y_syscpu[num])
            y_syscpu[num] = float(y_syscpumatch.group(1))

    def plot(self):
        self.read_log()
        self.data_proce()
        # 用来正常显示中文标签
        plt.rcParams['font.sans-serif'] = ['SimHei']
        fig = plt.figure()
        # y_softcpu
        ysu = fig.add_subplot(221)
        ysu.plot(x_time, y_softcpu)
        plt.xlabel("时间")
        plt.ylabel("软件内存使用率")

        # y_softmem
        ysm = fig.add_subplot(222)
        ysm.plot(x_time, y_softmem)
        plt.xlabel("时间")
        plt.ylabel("软件CPU使用率")

        # y_syscpu
        ysu = fig.add_subplot(223)
        ysu.plot(x_time, y_syscpu)
        ysu.yaxis.set_major_locator(ticker.MultipleLocator(8))
        plt.xlabel("时间")
        plt.ylabel("系统CPU使用率")
        plt.show()

if __name__ == '__main__':
    sd = show_data
    sd().plot()

