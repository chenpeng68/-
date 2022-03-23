from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QDesktopWidget, QLabel, QWidget
from camera_mini import Ui_mainWindow
import pyqtgraph as pg
import sys
from PyQt5 import QtWidgets, QtCore
import math
import socket
from threading import Thread

class mywindow(QMainWindow, Ui_mainWindow, QtWidgets.QWidget):
    def __init__(self, parent=None):
        '''
        self.data_y = [],self.data_x = []为读取的实时坐标，供warning函数去判断警告状态
        self.data_yy = []，self.data_xx = []用于存储一系列不同的坐标，供绘图使用
        利用self.data_yy、self.data_xx设置机器人的固定的起点
        1000=1毫秒,刷新执行时间
        '''
        super(mywindow, self).__init__(parent)
        self.setupUi(self)
        '''航向显示采用多线程'''

        self.udp = self.udpinit()
        self.t = Thread(target=self.getudpdata)
        self.t.setDaemon(True)
        self.t.start()
        self.data = str(0)

        '''初始化参数'''
        self.InitUI()
        self.data_y = []
        self.data_x = []
        self.data_yy = []
        self.data_xx = []
        self.x = []
        self.y = []
        self.ptr = 0
        self.p = -1
        self.datax1 = ''
        self.datay1 = ''



        '''角度参数初始化'''
        self.angel_para =[]
        self.angel_x_list = [0]
        self.angel_y_list = [0]

        '''定时器1画路线'''
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.update_data)
        self.timer.start(1000)

        '''定时器2报警'''
        self.timer1 = pg.QtCore.QTimer()
        self.timer1.timeout.connect(self.Warning)
        self.timer1.start(1000)

        '''定时器3画航向'''
        self.flag = 0
        self.timer2 = pg.QtCore.QTimer()
        self.timer2.timeout.connect(self.pyplotfsf)
        self.timer2.start(1000)

        '''设置屏幕靠右显示'''
        self.setCenter()

    '''点击定时器关闭'''
    def timeclick(self):
        self.timer1.stop()

    '''定时器开启'''
    def timer_start(self):
        self.timer1.start()

    '''UDP初始化'''
    def udpinit(self):
        ip = ""
        port = 6666
        own_addr = (ip, port)  # 接收方端口信息
        byte = 1024
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.bind(own_addr)  # 绑定端口信息
        return udp_socket

    '''接收对方主机发来的信号'''
    def getudpdata(self):
        while True:
            recv_data, other_addr = self.udp.recvfrom(1024)
            self.data = recv_data.decode("utf-8")
            # print("收到来自主机%s的消息: %s" % (other_addr, recv_data.decode("utf-8")))

    '''plot_rudder方向显示模块,对接收对方主机的数据进行处理并绘图'''
    def pyplotfsf(self):
        float_angle = float(self.data)
        self.angel_para.append(float_angle)
        '''
        math.degrees(传入参数为弧度值）# 比如math.degrees(math.PI) 结果为180（度）
        math.radians(传入参数为角度值）# 比如math.radians(180) 结果为PI
        '''
        self.angel = self.angel_para[-1]
        self.angel_to_x = math.cos(math.radians(self.angel))
        self.angel_to_y = math.sin(math.radians(self.angel))
        self.angel_x_list.append(self.angel_to_x)
        self.angel_y_list.append(self.angel_to_y)
        self.angel_x_list[1] = self.angel_to_x
        self.angel_y_list[1] = self.angel_to_y
        self.curve_angle_zero.setData(self.angel_x_list[:1], self.angel_y_list[:1])
        self.curve_angle.setData(self.angel_x_list[:2], self.angel_y_list[:2])

    def InitUI(self):

        '''程序启动时，首先将position_para.txt文件清空,写入(0.00,0.00)'''
        f1_original = open('D:\Robot_path\position_para.txt', mode='w')
        f1_original.write("(0.00,0.00)")
        f1_original.close()

        '''
        plot控件创建
        全局参数设定
        setRange机器人行走范围设置
        pw.setMouseEnabled禁用轴操作(使鼠标滑轮在本App中失效)
        '''
        pg.setConfigOptions(leftButtonPan=True)
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')

        '''
        初始化线路模拟控件
        self.pw.plot(pen=(0, 255, 0)) 设置线条的颜色
        symbolSize=14设置点的大小
        symbolBrush=(255,0,0)a设置点的颜色
        symbol='t'三角形点
        pen=(200, 100, 255),
        '''
        self.pw = pg.PlotWidget()
        self.pw.setRange(xRange=[0, 2.7], yRange=[0, 4.7])
        self.pw.setMouseEnabled(x=False, y=False)
        self.curve = self.pw.plot(pen=pg.mkPen(width=5, color=(30, 144, 255)), symbolBrush=(255, 69, 0), symbolSize=10)
        self.curve_zero = self.pw.plot(symbolBrush=(0, 255, 0), symbolSize=20)
        plot_display = self.findChild(QHBoxLayout, 'pyplot')
        plot_display.addWidget(self.pw)
        self.show()

        '''航向角模拟symbolSize=20, symbol=,, symbolBrush=(0, 255, 0)'''''
        self.pw_angle = pg.PlotWidget()
        self.pw_angle.setRange(xRange=[-1.5, 1.5], yRange=[-1.5, 1.5])
        self.pw_angle.setMouseEnabled(x=False, y=False)
        self.curve_angle = self.pw_angle.plot(pen=pg.mkPen(width=10, color=(0, 0, 255)))
        plot_display = self.findChild(QHBoxLayout, 'pyplot_rudder')
        plot_display.addWidget(self.pw_angle)
        self.show()

        '''航向原点绘制'''
        self.pw_angle_zero = pg.PlotWidget()
        self.pw_angle_zero.setRange(xRange=[-1.5, 1.5], yRange=[-1.5, 1.5])
        self.pw_angle_zero.setMouseEnabled(x=False, y=False)
        self.curve_angle_zero = self.pw_angle.plot(pen=pg.mkPen(width=5, color=(30, 144, 255)), symbolBrush=(255, 0, 0),symbolSize=20)

    def update_data(self):
        '''
        循环读txt文件中的第一行，将其绑定至qt界面当前坐标显示槽中，
        并对读取的数据解码，添加至self.data_x[]和self.data_y[]数组，
        再由pygraph绘制路线
        读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数
        position_x = round(x_number, 2)*0.0085表示将读取的x像素坐标先保留两位小数，然后再乘上像素比例0.0085
        '''

        with open('D:\Robot_path\position_para.txt', mode='r', encoding='ANSI') as f1:
            self.s = f1.readline()
            number_str = self.s[1:-1]
            t = -1
            for i in number_str:
                t += 1
                if number_str[t] == ',':
                    w = t
            x = number_str[0:w]
            y = number_str[w+1:]
            x_number = float(x)
            position_x = float('%.2f' % x_number)
            y_number = float(y)
            position_y = float('%.2f' % y_number)
            self.xy_text.setText(str(((position_x), (position_y))))
            self.data_x.append(position_x)
            self.data_y.append(position_y)
            length = len(self.data_x)

            '''
            此处判断读取的坐标是否相同，若相同，则不将坐标append到数组中；否则将参数加到数组末尾
            此判断解决重复读取相同坐标或者传输相同坐标的问题，至于取前5个的均值有待考量~
            self.data_xx、self.data_yy中存储的坐标特点是无重复的，
            '''
            if length > 1:
                if self.data_x[length-2] != self.data_x[length-1] or self.data_y[length-2] != self.data_y[length-1]:
                    self.p += 1
                    self.data_xx.append(position_x)
                    self.data_yy.append(position_y)
                    '''当第6个点出现后，对数组从后往前求五个坐标的均值,'''
                    # if self.p >= 5:
                    #     xxx = (self.data_xx[-5] + self.data_xx[-4] + self.data_xx[-3] + self.data_xx[-2] + self.data_xx[-1])/5
                    #     self.x.append(xxx)
                    #     yyy = (self.data_yy[-5] + self.data_yy[-4] + self.data_yy[-3] + self.data_yy[-2] + self.data_yy[-1])/5
                    #     self.y.append(yyy)
                    #     self.curve.setData(self.x[:], self.y[:])
                    # else:
                    #     self.x.append(self.data_xx[self.p])
                    #     self.y.append(self.data_yy[self.p])
                    #     self.curve.setData(self.x[:], self.y[:])

                    '''阈值方式更新坐标'''
                    if (self.p > 0):
                        DetR = math.sqrt((math.pow(self.data_xx[self.p]-self.data_xx[self.p-1], 2)+(math.pow(self.data_yy[self.p]-self.data_yy[self.p-1], 2))))
                        if (DetR > 0.1) and (DetR < 0.8):
                            self.x.append(self.data_xx[self.p])
                            self.y.append(self.data_yy[self.p])
                            self.curve.setData(self.x[:], self.y[:])

                        else:

                            pass

                    else:
                        ip = "192.168.0.10"  # 确定对方ip和端口号，除1024以外的端口均可使用
                        port = 6667
                        other_addr = (ip, port)
                        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        '''此处为第一个点的坐标，需要通过UDP通信协议传输给个机器人,写完退出当前UDP端口'''
                        self.x.append(self.data_xx[self.p])
                        self.y.append(self.data_yy[self.p])
                        '''绘制起点'''
                        self.curve_zero.setData(self.x[:], self.y[:])
                        self.curve.setData(self.x[:], self.y[:])

                        xx0 = str(self.x[0])
                        strx = xx0.ljust(5, '0')
                        yy0 = str(self.y[0])
                        stry = yy0.ljust(5, '0')
                        str_xy = strx + stry
                        send_data = str_xy.encode('utf-8')
                        udp_socket.sendto(send_data, other_addr)
                        print('第一个坐标已发送到对方主机端口')
                        udp_socket.close()

                    '''第一个描点为读取的第一个数值，第二个为2，3，4，5，6个读取的均值，防止坐标更新过快'''
                    # if (self.p)%5 == 0:
                    #     if self.p == 0:
                    #         self.x.append(self.data_xx[self.p])
                    #         self.y.append(self.data_yy[self.p])
                    #         self.curve.setData(self.x[:], self.y[:])
                    #     else:
                    #         xxx = (self.data_xx[self.p] + self.data_xx[self.p-1] + self.data_xx[self.p-2] + self.data_xx[self.p-3] + self.data_xx[self.p-4])/5
                    #         yyy = (self.data_yy[self.p] + self.data_yy[self.p-1] + self.data_yy[self.p-2] + self.data_yy[self.p-3] + self.data_yy[self.p-4])/5
                    #         self.x.append(xxx)
                    #         self.y.append(yyy)
                    #         self.curve.setData(self.x[:], self.y[:])

                    '''报警显示和弹窗警告段'''
                    if self.data_x[length-1] <= 0.3 or self.data_x[length-1] >= 2.4 or self.data_y[length-1] <= 0.3 or self.data_y[length-1] >= 4.4:
                        self.warning_inf.setText("警告")
                        self.warning_inf.setStyleSheet("color:red;border:1px solid white;font-size:30px;")
                        self.timer_start()
                    else:
                        self.warning_inf.setText("正常")
                        self.warning_inf.setStyleSheet("color:green;border:1px solid white;font-size:30px;")

            else:
                '''
                此段代码的存在与否，可以认定是否设置(0,0)点为起点;
                若为pass则视起点为开启声呐得到的第一个坐标
                '''
                # pass
                self.warning_inf.setText("正常")
                self.warning_inf.setStyleSheet("color:green;border:1px solid white;font-size:30px;")

                # self.data_xx.append(position_x)
                # self.data_yy.append(position_y)
                # self.curve.setData(self.data_xx[:], self.data_yy[:])

    def Warning(self):
        '''
        不读warning.txt文件，直接在本函数段内对实时坐标进行判断
        if x < 0.3 or x > 2.4 or y < 0.3 or y > 4.4的功能是判断x,y任意方向距墙壁之间的距离是否在安全范围内
        利用try execpt屏蔽当清淤小车在原点时的报警情况
        本程序段设置的0.3m为警示区
        '''
        if self.p >= 0:
            x = self.data_xx[self.p]
            y = self.data_yy[self.p]
            if x <= 0.3 or x >= 2.4 or y <= 0.3 or y >= 4.4:
                if self.flag == 0:
                    self.flag = 1
                    self.show_message()
            else:
                pass

        ''' 
        读取waring.txt中的报警状态：
        若读取为1，则代表此时清淤机器人离四周墙壁小于0.1m,需要弹出警告⚠
        若读取为0，则代表此时清淤机器人处在正常工作状态
        '''
        # with open('D:\Robot_path\warning.txt', mode='r', encoding='ANSI') as state:
        #     self.state = state.readline()
            # if self.state == '1':
                # self.nomal_inf.setText("")
                # self.warning_inf.setText("请暂停前行")
                # self.AutoCloseWindow()
                # self.show_message()
                # self.show_child()
                # QTimer.singleShot(10000, self.show_message)
            # else:
                # QTimer.singleShot(1000, self.show_message)
                # self.warning_inf.setText("")
                # self.nomal_inf.setText("正常")
                # pass

    def show_message(self):
            b = QtWidgets.QMessageBox.information(self, "警告", "请操控机器人到达安全区域!!!",
                                    QtWidgets.QMessageBox.Yes)
            if b == QtWidgets.QMessageBox.Yes:
                self.flag = 0
                self.timeclick()

    def setCenter(self):
        '''
        setCenter() 设置界面靠居右显示
        '''
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width())), int((screen.height() - size.height()) / 2))

    def closeEvent(self, event):
        '''
        关闭窗口，提示确认消息
        '''
        a = QtWidgets.QMessageBox.question(self, '退出', '你确定要退出吗?',
                                           QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if a == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    '''高分辨率自适应'''
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    test_ui = mywindow()
    test_ui.show()
    sys.exit(app.exec_())