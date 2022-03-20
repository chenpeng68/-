# 文件同时读写冲突实验
import time
import math
import random
# a = 10
# b = 20
i = 0
while i<10000:
    # x= x+10
    # x = (a+x)/(x+1)-0.2
    # y = x - 1 + b/2.5
    time.sleep(2)

    x = float(random.uniform(0.0, 2.7))
    y = float(random.uniform(0.0, 4.7))
    with open('D:\Robot_path\position_para.txt', mode='w') as f:
        f.write(str((x, y)))
        print('--(x,y)--', (x, y))
    i = i+1



        # if x > 18.7 or y < 0.1 :
        #     with open('D:\Robot_path\warning.txt', mode='w') as f2:
        #         f2.write(str(1))
        # else:
        #     with open('D:\Robot_path\warning.txt', mode='w') as f2:
        #         f2.write(str(0))
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
# import sys
# from PyQt5 import QtGui
# #
# #
# class AutoCloseWindow(QMainWindow):
#     """
#     自动关闭窗口第二种方法
#     """
#     def __init__(self):
#         super(AutoCloseWindow, self).__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         # self.setWindowTitle('自动关闭窗口第二种方法')
#         label = QLabel('<font color=red size=140><b>Hello World,窗口在5s后自动关闭！</b></font>')
#         label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)  # 无框架 闪屏
#         self.setCentralWidget(label)
#         QTimer.singleShot(5000, app.quit)  # 只执行一次
#
#
# # 第二种方法 其实是一样的
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     main = AutoCloseWindow()
#     # print(main.__doc__)
#     main.show()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import *
#
# app = QApplication(sys.argv)
# widget = QWidget()
# label = QLabel(widget)
# label.setText('Hello World!')
#
# '''主要逻辑'''
# def mouseDoubleClickEvent(event):
#     text, ok = QInputDialog().getText(QWidget(), '修改Label', '输入文本:')
#     if ok and text:
#         label.setText(text)
# label.mouseDoubleClickEvent = mouseDoubleClickEvent
#
# widget.show()
# sys.exit(app.exec_())







# 第一种方法
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     label = QLabel('<font color=red size=140><b>Hello World,窗口在5s后自动关闭！</b></font>')
#     label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)  # 无框架 闪屏
#     label.show()
#     QTimer.singleShot(5000, app.quit)   # 只执行一次
#     sys.exit(app.exec_())


# from PyQt5.QtWidgets import *
# import sys
#
#
# class Main(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("主窗口")
#         button = QPushButton("弹出子窗", self)
#         button.clicked.connect(self.show_child)
#
#     def show_child(self):
#         self.child_window = Child()
#         self.child_window.show()
#
#
# class Child(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("我是子窗口啊")
#
#
# # 运行主窗口
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#
#     window = Main()
#     window.show()
#
#     sys.exit(app.exec_())


# import sys;
# from PyQt5.QtCore import *;
# from PyQt5.QtWidgets import *;
#
#
# class WinForm(QWidget):
#     def __init__(self, parent=None):
#         super(WinForm, self).__init__(parent)
#         self.setGeometry(300, 300, 800, 800)  # 确定窗口位置大小
#         self.setWindowTitle('点击按钮关闭窗口')  # 设置窗口标题
#         quit = QPushButton('Close', self)  # button 对象
#         quit.setGeometry(10, 10, 100, 60)  # 设置按钮的位置 和 大小
#         quit.setStyleSheet("background-color: red")  # 设置按钮的风格和颜色
#         quit.clicked.connect(self.close)  # 点击按钮之后关闭窗口
#
#         self.timer = QTimer(self)  # 初始化一个定时器
#         self.timer.timeout.connect(self.close)  # 计时结束调用operate()方法
#         self.timer.start(5000)  # 设置计时间隔并启动 2s后关闭窗口
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     win = WinForm()  # 实体化 类
#     win.show()
#     sys.exit(app.exec_())


# import turtle
# from datetime import *
#
#
# # 抬起画笔，向前运动一段距离放下
# def Skip(step):
#     turtle.penup()
#     turtle.forward(step)
#     turtle.pendown()
#
#
# def drawCircle(content, content_len, init_data, init_data_type, circle_radius, circle_radius_step, color, font_size):
#     '''
# 	content:传入的数组，代表要画的圆上面写的内容，比如1-12月
# 	content_len：数组长度，用这个元素来做循环，便于调整每次的偏置角度
# 	init_data： x轴正方向显示当前时间，这个数据就是当前时间
# 	init_data_type:代表这个是什么类型的，时，分，秒之类的
# 	circle_radius：圆的半径
# 	circle_radius_step： 圆环上的数据根据半径和这个长度结合写上内容
# 	color： 画笔颜色
#     '''
#     # turtle.pos()
#     turtle.home()
#     # turtle.mode("logo")
#     turtle.pensize(3)
#     turtle.pencolor(color)
#     turtle.fillcolor('#33BB00')
#
#     # turtle.right(90)
#     # turtle.right(-360/content_len)
#     # Skip(circle_radius+circle_radius_step+10*3)
#     # turtle.write(' ', align="center", font=("Courier", font_size,'bold'))
#     # Skip(-circle_radius-circle_radius_step-10*3)
#     # #turtle.right(360/content_len)
#
#     Skip(circle_radius + circle_radius_step + 10 * 3)
#     turtle.write(init_data_type, align="center", font=("Courier", font_size, 'bold'))
#     Skip(-circle_radius - circle_radius_step - 10 * 3)
#
#     # turtle.right(-90)
#
#     initdata_index = content.index(init_data)
#     for i in range(initdata_index, content_len):
#         Skip(circle_radius)
#         fantilen = len(content[i])
#         if i == initdata_index:
#             turtle.forward(75)
#             turtle.forward(-90)
#             turtle.forward(15)
#
#         for name in range(fantilen):
#             turtle.write(content[i][name], align="center", font=("Courier", font_size))
#             Skip(15)
#         Skip(-15 * fantilen)
#         Skip(-circle_radius)
#         turtle.left(360 / content_len)
#     for i in range(initdata_index):
#         Skip(circle_radius)
#         fantilen = len(content[i])
#         for name in range(fantilen):
#             turtle.write(content[i][name], align="center", font=("Courier", font_size))
#             Skip(15)
#         Skip(-15 * fantilen)
#         Skip(-circle_radius)
#         turtle.left(360 / content_len)
#
#
# def Week(t):
#     week = ["星期一", "星期二", "星期三",
#             "星期四", "星期五", "星期六", "星期日"]
#     return week[t.weekday()]
#
#
# def Date(t):
#     y = t.year
#     m = t.month
#     d = t.day
#     return "%s-%d-%d" % (y, m, d)
#
#
# def runclock():
#     turtle.reset()
#     t = datetime.today()
#     print(t)
#     second = t.second  # + t.microsecond * 0.000001
#     minute = t.minute  # + second / 60.0
#     hour = t.hour  # + minute / 60.0
#
#     Traditional_Chinese = [' ', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖',
#                            '拾', '拾壹', '拾贰', '拾叁', '拾肆', '拾伍', '拾陆', '拾柒', '拾捌', '拾玖',
#                            '贰拾', '贰拾壹', '贰拾贰', '贰拾叁', '贰拾肆', '贰拾伍', '贰拾陆', '贰拾柒', '贰拾捌', '贰拾玖',
#                            '叁拾', '叁拾壹', '叁拾贰', '叁拾叁', '叁拾肆', '叁拾伍', '叁拾陆', '叁拾柒', '叁拾捌', '叁拾玖',
#                            '肆拾', '肆拾壹', '肆拾贰', '肆拾叁', '肆拾肆', '肆拾伍', '肆拾陆', '肆拾柒', '肆拾捌', '肆拾玖',
#                            '伍拾', '伍拾壹', '伍拾贰', '伍拾叁', '伍拾肆', '伍拾伍', '伍拾陆', '伍拾柒', '伍拾捌', '伍拾玖']
#     Simplified_Chinese = [' ', '一', '二', '三', '四', '五', '六', '七', '八', '九', '十',
#                           '十一', '十二', '十三', '十四', '十五', '十六', '十七', '十八', '十九',
#                           '二十', '二十一', '二十二', '二十三', '二十四', '二十五', '二十六', '二十七', '二十八', '二十九',
#                           '三十', '三十一', '三十二', '三十三', '三十四', '三十五', '三十六', '三十七', '三十八', '三十九',
#                           '四十', '四十一', '四十二', '四十三', '四十四', '四十五', '四十六', '四十七', '四十八', '四十九',
#                           '五十', '五十一', '五十二', '五十三', '五十四', '五十五', '五十六', '五十七', '五十八', '五十九'
#                           ]
#
#     hours = ['壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖', '拾', '拾壹', '拾贰',
#              '拾叁', '拾肆', '拾伍', '拾陆', '拾柒', '拾捌', '拾玖', '贰拾', '贰拾壹', '贰拾贰', '贰拾叁', '贰拾肆']
#     Simplified_hours = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十',
#                         '十一', '十二', '十三', '十四', '十五', '十六', '十七', '十八', '十九',
#                         '二十', '二十一', '二十二', '二十三', '二十四']
#
#     drawCircle(Simplified_Chinese, len(Simplified_Chinese), Simplified_Chinese[second], '秒', 250, 25, 'blue', 10)
#     drawCircle(Simplified_Chinese, len(Simplified_Chinese), Simplified_Chinese[minute], '分', 170, 20, 'green', 10)
#     drawCircle(Simplified_hours, len(Simplified_hours), Simplified_hours[hour - 1], '时', 80, 15, 'red', 10)
#
#     printer = turtle.Turtle()
#     # 隐藏画笔的turtle形状
#     printer.hideturtle()
#     printer.color('#11CCFF')
#     printer.right(-90)
#     printer.penup()
#     printer.forward(40)
#     printer.write(Week(t), align="center", font=("Courier", 10, "bold"))
#     printer.back(80)
#     printer.write(Date(t), align="center", font=("Courier", 14, "bold"))
#     print(Week(t), Date(t))
#     printer.right(90)
#     turtle.ontimer(runclock, 1000)
#
#
# def main():
#     # 打开/关闭龟动画，并为更新图纸设置延迟。
#     turtle.tracer(False)
#     ts = turtle.getscreen()
#     ts.bgcolor("black")
#
#     runclock()
#     turtle.mainloop()
#
#
# if __name__ == "__main__":
#     main()

#
# import sys
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtGui import QFont
# from PyQt5.QtWidgets import (QApplication, QWidget, QDial,
#                              QLabel, QHBoxLayout)
#
#
# class DemoDial(QWidget):
#     def __init__(self, parent=None):
#         super(DemoDial, self).__init__(parent)
#
#         # 设置窗口标题
#         self.setWindowTitle('实战PyQt5: QDial Demo!')
#         # 设置窗口大小
#         self.resize(400, 300)
#
#         self.initUi()
#
#     def initUi(self):
#         self.dial = QDial(self)
#         self.dial.setRange(0, 300)
#         self.dial.setNotchesVisible(True)
#         self.dial.valueChanged.connect(self.onDialValueChanged)
#
#         self.labValue = QLabel('0', self)
#         self.labValue.setFont(QFont('Arial Black', 24))
#
#         hLayout = QHBoxLayout(self)
#         hLayout.addWidget(self.dial)
#         hLayout.addWidget(self.labValue)
#
#         self.setLayout(hLayout)
#
#     def onDialValueChanged(self):
#         self.labValue.setText(str(self.dial.value()))
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = DemoDial()
#     window.show()
#     sys.exit(app.exec())


# 倒圆的范围控制
# 汽车仪表盘速度计
# QDial

# from PyQt5.Qt import *
#
# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('QDial_操作')
#         self.resize(500,500)
#         self.iniUI()
#
#     def iniUI(self):
#         dial = QDial(self)
#         dial.setRange(30,150)           #设置范围
#         dial.setNotchesVisible(True)    #设置刻度
#         dial.setPageStep(20)            #翻页步长
#         dial.setWrapping(True)          #刻度不留缺口
#         dial.setNotchTarget(50)         #设置刻度密度，即单位刻度所代表的大小
#
#         label = QLabel(self)
#         self.label = label
#         label.setAlignment(Qt.AlignCenter)
#
#         label.resize(self.width() / 3, self.height() / 3)
#         label.move((self.width() - label.width()) / 2, (self.height() - label.height()) * 0.8 / 2)
#
#
#         def cao(value):
#             label.setText(str(value))
#             label.setStyleSheet('font-size:{}px;background-color:cyan;'.format(value))
#             label.adjustSize()
#         dial.valueChanged.connect(cao)
#
# if __name__ == '__main__':
#     import sys
#     app = QApplication(sys.argv)
#
#
#     win = MyWindow()
#     win.show()
#     sys.exit(app.exec_())


# import matplotlib.pyplot as plt
# import numpy as np
#
# loc = np.random.randint(0,10,size = (10,2))
# plt.figure(figsize=(10, 10))
# plt.plot(loc[:,0], loc[:,1], 'g*', ms=20)
# plt.grid(True)
#
# # 路径
# way = np.arange(10)
# np.random.shuffle(way)
#
# for i in range(0, len(way)-1):
#     start = loc[way[i]]
#     end = loc[way[i+1]]
#     plt.arrow(start[0], start[1], end[0]-start[0], end[1]-start[1], # 坐标与距离
#     head_width=0.2, lw=2,#箭头⻓度，箭尾线宽
#     length_includes_head = True) # ⻓度计算包含箭头箭尾
#     plt.text(start[0],start[1],s = i,fontsize = 18,color = 'red') # ⽂本
#     if i == len(way) - 2: # 最后⼀个点
#         plt.text(end[0],end[1],s = i + 1,fontsize = 18,color = 'red')


'''UDP通信'''
# import socket
# def main():
#
#    ip = "192.168.199.141"  # 对方ip和端口
#    port = 8888
#    other_addr = (ip, port)
#    byte = 1024
#    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
#    while True:
#        send_data = input("输入要发送的信息:").encode("utf-8")
#        udp_socket.sendto(send_data, other_addr)
#        """输入数据为空退出,否则进入接收状态"""
#        if send_data:
#            recv_data, other_addr = udp_socket.recvfrom(byte)
#            print("收到来自%s的消息: %s" % (other_addr, recv_data.decode("utf-8")))
#        else:
#            break
#    udp_socket.close()
# if __name__ == '__main__':
#    main()

# import socket
#
# def main():
#     ip = ""
#     port = 8887
#     own_addr = (ip, port)  # 接收方端口信息
#     byte = 1024
#     udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     udp_socket.bind(own_addr)  # 绑定端口信息
#     p = 0
#     print('%%%%%',p)
#     while True:
#         p = p+1
#         print('----', p)
#         recv_data, other_addr = udp_socket.recvfrom(byte)
#         print("收到来自%s的消息: %s" % (other_addr, recv_data.decode("utf-8")))
#
# if __name__ == '__main__':
#     main()




