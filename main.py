import sys

import sqlite3
from PyQt5.QtGui import QPixmap
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSignal, QTimer
import time


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.levels = None
        uic.loadUi('main.ui', self)
        self.centralwidget.setStyleSheet("#centralwidget {background: #270847;}")
        self.recordsbtn.setStyleSheet('QPushButton {background-color: #4B0082; color: white; border-radius: 5px}'
                                      "QPushButton:hover{background: #310062; border:none;}")
        self.levelsbtn.setStyleSheet('QPushButton {background-color: #4B0082; color: white; border-radius: 5px}'
                                     "QPushButton:hover{background: #310062; border:none;}")
        self.rulesbtn.setStyleSheet('QPushButton {background-color: #4B0082; color: white; border-radius: 5px}'
                                     "QPushButton:hover{background: #310062; border:none;}")
        self.name.setStyleSheet('QLabel {color: white}')
        self.recordsbtn.clicked.connect(self.showrecords)
        self.levelsbtn.clicked.connect(self.showlevels)
        self.rulesbtn.clicked.connect(self.showrules)

    def closeEvent(self, e):

        con = sqlite3.connect('records.db')
        cur = con.cursor()
        cur.execute('''DELETE FROM statistic''')
        con.commit()
        con.close()

    def showrecords(self):
        self.records = Records()
        self.records.show()

    def showlevels(self):
        self.levels = Levels()
        self.levels.show()

    def showrules(self):
        self.rules = Rules()
        self.rules.show()


class Rules(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('rules.ui', self)
        self.centralwidget.setStyleSheet("#centralwidget {background: #270847;}")

        f = open("rules.txt", encoding="utf8")
        a = f.read()
        if a:
            self.textBrowser.setText(a)
        f.close()

        self.pushButton.setStyleSheet('QPushButton {background-color: #4B0082; border-radius: 5px}')
        self.pushButton_2.setStyleSheet('QPushButton {background-color: white; border-radius: 5px}')
        self.pushButton_3.setStyleSheet('QPushButton {background-color: #4B0082; border-radius: 5px}')
        self.pushButton_4.setStyleSheet('QPushButton {background-color: #4B0082; border-radius: 5px}')
        self.pushButton_5.setStyleSheet('QPushButton {background-color: white; border-radius: 5px}')
        self.pushButton_6.setStyleSheet('QPushButton {background-color: #4B0082; border-radius: 5px}')
        self.pushButton_7.setStyleSheet('QPushButton {background-color: #4B0082; border-radius: 5px}')
        self.pushButton_8.setStyleSheet('QPushButton {background-color: white; border-radius: 5px}')
        self.pushButton_9.setStyleSheet('QPushButton {background-color: #4B0082; border-radius: 5px}')
        self.pushButton_10.setStyleSheet('QPushButton {background-color: #4B0082; border-radius: 5px}')
        self.pushButton_11.setStyleSheet('QPushButton {background-color: #4B0082; border-radius: 5px}')
        self.pushButton_12.setStyleSheet('QPushButton {background-color: white; border-radius: 5px}')
        self.pushButton_13.setStyleSheet('QPushButton {background-color: white; border-radius: 5px}')
        self.pushButton_14.setStyleSheet('QPushButton {background-color: white; border-radius: 5px}')
        self.pushButton_15.setStyleSheet('QPushButton {background-color: white; border-radius: 5px}')
        self.pushButton_16.setStyleSheet('QPushButton {background-color: white; border-radius: 5px}')
        self.pushButton_17.setStyleSheet('QPushButton {background-color: white; border-radius: 5px}')
        self.pushButton_18.setStyleSheet('QPushButton {background-color: #4B0082; border-radius: 5px}')


class Levels(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Levels')
        self.name = 'NoName'
        self.levels2 = None
        uic.loadUi('levels.ui', self)
        self.centralwidget.setStyleSheet("#centralwidget {background: #270847;}")
        self.OKbtn.setStyleSheet('QPushButton {background-color: #4B0082; color: white; border-radius: 5px}'
                                 "QPushButton:hover{background: #310062; border:none;}")
        self.lineedit.setStyleSheet('QLineEdit {background-color: #4B0082; color: white; border-radius: 2px}')
        self.entername.setStyleSheet('QLabel {color: white}')
        self.OKbtn.clicked.connect(self.okevent)

    def okevent(self):
        if self.lineedit.text():
            self.name = self.lineedit.text()

        self.levels2 = Levels2(self.name)

        con = sqlite3.connect('records.db')
        cur = con.cursor()
        if self.name not in list(cur.execute('''SELECT name FROM records''')):
            cur.execute('''INSERT INTO records(name,all_attemps,best_time) VALUES('%s',0,0);'''%(self.name))

        con.commit()
        con.close()

        self.levels2.show()
        self.close()


class Levels2(QMainWindow):
    def __init__(self, name):
        super().__init__()
        self.level2 = None
        self.level1 = None
        self.name = name
        uic.loadUi('levels2.ui', self)
        self.centralwidget.setStyleSheet("#centralwidget {background: #270847;}")
        for i in range(1, 6):
            eval(f"""self.lvl{i}btn.setStyleSheet('QPushButton {{color: white; background-color: #4B0082; border-radius: 2px;}}'
        "QPushButton:hover{{background: #310062; border:none;}}")""")
        for i in range(1, 6):
            eval(f"""self.lvl{i}btn.clicked.connect(self.lvl{i}fun)""")
        self.lvllabel.setStyleSheet('QLabel {color: white}')

    def lvl1fun(self):
        self.level1 = Level1(self.name)
        self.level1.show()
        self.close()

    def lvl2fun(self):
        self.level2 = Level2(self.name)
        self.level2.show()
        self.close()

    def lvl3fun(self):
        self.level3 = Level3(self.name)
        self.level3.show()
        self.close()

    def lvl4fun(self):
        self.level4 = Level4(self.name)
        self.level4.show()
        self.close()

    def lvl5fun(self):
        self.level5 = Level5(self.name)
        self.level5.show()
        self.close()


class Level1(QMainWindow):
    timeout = pyqtSignal()

    def __init__(self, name):
        self.besttime = 0
        self.lose = None
        self.name = name
        super().__init__()
        self.setWindowTitle('Levels')
        self.levels2 = None
        self.newlevel = None
        uic.loadUi('level12.ui', self)

        self.time = 0
        self.timerUp = QTimer()
        self.timerUp.setInterval(1000)
        self.timerUp.timeout.connect(self.updateUptime)
        self.timerUp.start()

        self.centralwidget.setStyleSheet("#centralwidget {background: #270847;}")
        self.count = 0
        self.errors = 0
        self.line2.hide()
        self.pauselabel.hide()
        self.continuebtn.setStyleSheet(
            "QPushButton {color: white; background-color: #4B0082; border-radius: 2px;}"  "QPushButton:hover{{"
            "background: #310062; border:none;}}")
        self.continuebtn.hide()
        self.pausebtn.setStyleSheet(
            "QPushButton {color: white; background-color: #4B0082; border-radius: 2px;}"  "QPushButton:hover{{"
            "background: #310062; border:none;}}")
        self.restartbtn.setStyleSheet(
            "QPushButton {color: white; background-color: #4B0082; border-radius: 2px;}"  "QPushButton:hover{{"
            "background: #310062; border:none;}}")
        self.restartbtn.hide()
        self.levelsbtn.setStyleSheet(
            "QPushButton {color: white; background-color: #4B0082; border-radius: 2px;}"  "QPushButton:hover{{"
            "background: #310062; border:none;}}")
        self.levelsbtn.hide()
        self.pausebtn.clicked.connect(self.pauseevent)
        self.restartbtn.clicked.connect(self.restartevent)
        self.levelsbtn.clicked.connect(self.levelsevent)
        self.continuebtn.clicked.connect(self.continueevent)
        self.level2label.hide()
        for i in range(1, 17):
            eval(
                f"self.btn{i}.setStyleSheet('QPushButton {{background-color: #4B0082; border-radius: 3px; color: "
                f"white}}'\n"
                f"        \"QPushButton:hover{{background: #310062; border:none;}}\")")
        for i in range(1, 17):
            eval(f"""self.btn{i}.clicked.connect(self.clickevent{i})""")
        self.btn9_2.setStyleSheet('QPushButton {{background-color: #310062; border-radius: 3px; }}')
        self.btn14_2.setStyleSheet('QPushButton {{background-color: #310062; border-radius: 3px; }}')
        self.btn16_2.setStyleSheet('QPushButton {{background-color: #310062; border-radius: 3px; }}')
        for i in range(1, 17):
            eval(f"self.btn{i}_2.setStyleSheet('QPushButton {{background-color: white; border-radius: 3px; }}')")
        for i in range(1, 17):
            eval(f'self.btn{i}_2.hide()')
        self.btn9.hide()
        self.btn14.hide()
        self.btn6.hide()
        self.btn9_2.show()
        self.btn14_2.show()
        self.btn6_2.show()

    def updateUptime(self):
        self.time += 1
        self.settimer(self.time)

    def settimer(self, int):
        self.time = int
        self.timer.setText(time.strftime('%M:%S', time.gmtime(self.time)))

    def pauseevent(self):
        self.timerUp.stop()
        self.pausebtn.hide()
        self.restartbtn.show()
        self.levelsbtn.show()
        self.pauselabel.show()
        for i in range(1, 17):
            eval(f"""self.btn{i}.setEnabled(False)""")
        self.continuebtn.show()
        self.level1label.hide()
        for i in range(1, 17):
            eval(f"""self.btn{i}.setStyleSheet('QPushButton {{background-color: #310062; }}')""")

    def continueevent(self):
        self.timerUp.start()
        self.restartbtn.hide()
        self.levelsbtn.hide()
        self.continuebtn.hide()
        self.pauselabel.hide()
        for i in range(1, 17):
            eval(f"""self.btn{i}.setEnabled(True)""")
        for i in range(1, 17):
            eval(
                f"self.btn{i}.setStyleSheet('QPushButton {{background-color: #4B0082; border-radius: 3px; color: "
                f"white}}'\n"
                f"        \"QPushButton:hover{{background: #310062; border:none;}}\")")
        self.pausebtn.show()
        self.level1label.show()

    def restartevent(self):
        self.newlevel = Level1(self.name)
        self.newlevel.show()
        self.close()

    def levelsevent(self):
        self.levels2 = Levels2(self.name)
        self.levels2.show()
        self.close()

    def clickevent1(self):
        self.btn1.setText('X')
        self.btn1.disconnect()
        self.checkerrors()

    def clickevent2(self):
        self.btn2.setText('X')
        self.btn2.disconnect()
        self.checkerrors()

    def clickevent3(self):
        self.btn3.setText('X')
        self.btn3.disconnect()
        self.checkerrors()

    def clickevent4(self):
        self.btn4.setText('X')
        self.btn4.disconnect()
        self.checkerrors()

    def clickevent5(self):
        self.btn5.disconnect()
        self.btn5.hide()
        self.btn5_2.show()
        self.checkcounter()

    def clickevent6(self):
        pass

    def clickevent7(self):
        self.btn7.setText('X')
        self.btn7.disconnect()
        self.checkerrors()

    def clickevent8(self):
        self.btn8.setText('X')
        self.btn8.disconnect()
        self.checkerrors()

    def clickevent9(self):
        pass

    def clickevent10(self):
        self.btn10.disconnect()
        self.btn10.hide()
        self.btn10_2.show()
        self.checkcounter()

    def clickevent11(self):
        self.btn11.setText('X')
        self.btn11.disconnect()
        self.checkerrors()

    def clickevent12(self):
        self.btn12.setText('X')
        self.btn12.disconnect()
        self.checkerrors()

    def clickevent13(self):
        self.btn13.disconnect()
        self.btn13.hide()
        self.btn13_2.show()
        self.checkcounter()

    def clickevent14(self):
        pass

    def clickevent15(self):
        self.btn15.setText('X')
        self.btn15.disconnect()
        self.checkerrors()

    def clickevent16(self):
        self.btn16.setText('X')
        self.btn16.disconnect()
        self.checkerrors()

    def checkcounter(self):
        self.count += 1
        if self.count == 3:
            self.win = Win(self.name, self.time)

            con = sqlite3.connect('records.db')
            cur = con.cursor()
            cur.execute('''UPDATE records
                        SET all_attemps = all_attemps + 1
                        WHERE name == '%s' '''%(self.name))

            cur.execute('''INSERT INTO statistic(time) VALUES(%s)'''%(self.time))

            cur.execute('''UPDATE records 
                        SET best_time = (SELECT MIN(time) FROM statistic)
                        WHERE name == '%s' '''%(self.name))
            con.commit()
            con.close()
            self.win.show()
            self.close()

    def checkerrors(self):
        self.errors += 1
        if self.errors == 3:
            self.lose = Lose(self.name)
            self.lose.show()
            self.close()


class Level2(QMainWindow):
    timeout = pyqtSignal()

    def __init__(self, name):
        self.lose = None
        self.name = name
        super().__init__()
        self.setWindowTitle('Level2')
        self.levels2 = None
        self.newlevel = None
        uic.loadUi('level12.ui', self)

        self.time = 0
        self.timerUp = QTimer()
        self.timerUp.setInterval(1000)
        self.timerUp.timeout.connect(self.updateUptime)
        self.timerUp.start()

        self.centralwidget.setStyleSheet("#centralwidget {background: #270847;}")
        self.count = 0
        self.errors = 0
        self.line3.hide()
        self.pauselabel.hide()
        self.continuebtn.setStyleSheet(
            "QPushButton {color: white; background-color: #4B0082; border-radius: 2px;}"  "QPushButton:hover{{"
            "background: #310062; border:none;}}")
        self.continuebtn.hide()
        self.pausebtn.setStyleSheet(
            "QPushButton {color: white; background-color: #4B0082; border-radius: 2px;}"  "QPushButton:hover{{"
            "background: #310062; border:none;}}")
        self.restartbtn.setStyleSheet(
            "QPushButton {color: white; background-color: #4B0082; border-radius: 2px;}"  "QPushButton:hover{{"
            "background: #310062; border:none;}}")
        self.restartbtn.hide()
        self.levelsbtn.setStyleSheet(
            "QPushButton {color: white; background-color: #4B0082; border-radius: 2px;}"  "QPushButton:hover{{"
            "background: #310062; border:none;}}")
        self.levelsbtn.hide()
        self.pausebtn.clicked.connect(self.pauseevent)
        self.restartbtn.clicked.connect(self.restartevent)
        self.levelsbtn.clicked.connect(self.levelsevent)
        self.continuebtn.clicked.connect(self.continueevent)
        self.level1label.hide()
        for i in range(1, 17):
            eval(
                f"self.btn{i}.setStyleSheet('QPushButton {{background-color: #4B0082; border-radius: 3px; color: "
                f"white}}'\n"
                f"        \"QPushButton:hover{{background: #310062; border:none;}}\")")
        for i in range(1, 17):
            eval(f"""self.btn{i}.clicked.connect(self.clickevent{i})""")
        self.btn9_2.setStyleSheet('QPushButton {{background-color: #310062; border-radius: 3px; }}')
        self.btn14_2.setStyleSheet('QPushButton {{background-color: #310062; border-radius: 3px; }}')
        self.btn16_2.setStyleSheet('QPushButton {{background-color: #310062; border-radius: 3px; }}')
        for i in range(1, 17):
            eval(f"self.btn{i}_2.setStyleSheet('QPushButton {{background-color: white; border-radius: 3px; }}')")
        for i in range(1, 17):
            eval(f'self.btn{i}_2.hide()')
        self.btn9.hide()
        self.btn14.hide()
        self.btn16.hide()
        self.btn9_2.show()
        self.btn14_2.show()
        self.btn16_2.show()

    def updateUptime(self):
        self.time += 1
        self.settimer(self.time)

    def settimer(self, int):
        self.time = int
        self.timer.setText(time.strftime('%M:%S', time.gmtime(self.time)))

    def pauseevent(self):
        self.timerUp.stop()
        self.pausebtn.hide()
        self.restartbtn.show()
        self.levelsbtn.show()
        self.pauselabel.show()
        for i in range(1, 17):
            eval(f"""self.btn{i}.setEnabled(False)""")
        self.continuebtn.show()
        self.level2label.hide()
        for i in range(1, 17):
            eval(f"""self.btn{i}.setStyleSheet('QPushButton {{background-color: #310062; }}')""")

    def continueevent(self):
        self.timerUp.start()
        self.restartbtn.hide()
        self.levelsbtn.hide()
        self.continuebtn.hide()
        self.pauselabel.hide()
        for i in range(1, 17):
            eval(f"""self.btn{i}.setEnabled(True)""")
        for i in range(1, 17):
            eval(
                f"self.btn{i}.setStyleSheet('QPushButton {{background-color: #4B0082; border-radius: 3px; color: "
                f"white}}'\n"
                f"        \"QPushButton:hover{{background: #310062; border:none;}}\")")
        self.pausebtn.show()
        self.level2label.show()

    def restartevent(self):
        self.newlevel = Level2(self.name)
        self.newlevel.show()
        self.close()

    def levelsevent(self):
        self.levels2 = Levels2(self.name)
        self.levels2.show()
        self.close()

    def clickevent1(self):
        self.btn1.disconnect()
        self.btn1.hide()
        self.btn1_2.show()
        self.checkcounter()

    def clickevent2(self):
        self.btn2.disconnect()
        self.btn2.hide()
        self.btn2_2.show()
        self.checkcounter()

    def clickevent3(self):
        self.btn3.disconnect()
        self.btn3.hide()
        self.btn3_2.show()
        self.checkcounter()

    def clickevent4(self):
        self.btn4.disconnect()
        self.btn4.hide()
        self.btn4_2.show()
        self.checkcounter()

    def clickevent5(self):
        self.btn5.disconnect()
        self.btn5.hide()
        self.btn5_2.show()
        self.checkcounter()

    def clickevent6(self):
        self.btn6.setText('X')
        self.btn6.disconnect()
        self.checkerrors()

    def clickevent7(self):
        self.btn7.setText('X')
        self.btn7.disconnect()
        self.checkerrors()

    def clickevent8(self):
        self.btn8.disconnect()
        self.btn8.hide()
        self.btn8_2.show()
        self.checkcounter()

    def clickevent9(self):
        pass

    def clickevent10(self):
        self.btn10.setText('X')
        self.btn10.disconnect()
        self.checkerrors()

    def clickevent11(self):
        self.btn11.setText('X')
        self.btn11.disconnect()
        self.checkerrors()

    def clickevent12(self):
        self.btn12.disconnect()
        self.btn12.hide()
        self.btn12_2.show()
        self.checkcounter()

    def clickevent13(self):
        self.btn13.disconnect()
        self.btn13.hide()
        self.btn13_2.show()
        self.checkcounter()

    def clickevent14(self):
        pass

    def clickevent15(self):
        self.btn15.disconnect()
        self.btn15.hide()
        self.btn15_2.show()
        self.checkcounter()

    def clickevent16(self):
        pass

    def checkcounter(self):
        self.count += 1
        if self.count == 9:
            self.win = Win(self.name, self.time)

            con = sqlite3.connect('records.db')
            cur = con.cursor()
            cur.execute('''UPDATE records
                        SET all_attemps = all_attemps + 1
                        WHERE name == '%s' '''%(self.name))

            cur.execute('''INSERT INTO statistic(time) VALUES(%s)'''%(self.time))

            cur.execute('''UPDATE records 
                        SET best_time = (SELECT MIN(time) FROM statistic)
                        WHERE name == '%s' '''%(self.name))
            con.commit()
            con.close()

            self.win.show()
            self.close()

    def checkerrors(self):
        self.errors += 1
        if self.errors == 3:
            self.lose = Lose(self.name)
            self.lose.show()
            self.close()


class Win(QMainWindow):
    def __init__(self, name, timer):
        super().__init__()
        self.setWindowTitle('Congratulations!!')
        self.menu = None
        self.levels = None
        self.name = name
        self.time = timer
        uic.loadUi('win.ui', self)
        self.centralwidget.setStyleSheet("#centralwidget {background: #270847;}")
        self.levelsbtn.setStyleSheet(
            "QPushButton {color: white; background-color: #4B0082; border-radius: 2px;}"  "QPushButton:hover{{"
            "background: #310062; border:none;}}")
        self.menubtn.setStyleSheet(
            "QPushButton {color: white; background-color: #4B0082; border-radius: 2px;}"  "QPushButton:hover{{"
            "background: #310062; border:none;}}")
        self.levelsbtn.clicked.connect(self.levelsevent)
        self.menubtn.clicked.connect(self.menuevent)
        self.rezlabel.setText('Time: ' + time.strftime('%M:%S', time.gmtime(self.time)))
        self.pixmap = QPixmap('pic' + str(random.randint(1, 5)) + '.jpg')
        self.piclabel.setPixmap(self.pixmap)

    def levelsevent(self):
        self.levels = Levels2(self.name)
        self.levels.show()
        self.close()

    def menuevent(self):
        self.menu = MainMenu()
        self.menu.show()
        self.close()


class Level3(QMainWindow):
    timeout = pyqtSignal()

    def __init__(self, name):
        self.lose = None
        self.win = None
        self.name = name
        super().__init__()
        self.setWindowTitle('Level3')
        self.levels2 = None
        self.newlevel = None
        uic.loadUi('level34.ui', self)

        self.time = 0
        self.timerUp = QTimer()
        self.timerUp.setInterval(1000)
        self.timerUp.timeout.connect(self.updateUptime)
        self.timerUp.start()

        self.centralwidget.setStyleSheet("#centralwidget {background: #270847;}")
        self.count = 0
        self.errors = 0
        self.line3.hide()
        self.line4.hide()
        self.pauselabel.hide()
        self.continuebtn.setStyleSheet(
            "QPushButton {color: white; background-color: #4B0082; border-radius: 2px;}"  "QPushButton:hover{{"
            "background: #310062; border:none;}}")
        self.continuebtn.hide()
        self.pausebtn.setStyleSheet(
            "QPushButton {color: white; background-color: #4B0082; border-radius: 2px;}"  "QPushButton:hover{{"
            "background: #310062; border:none;}}")
        self.restartbtn.setStyleSheet(
            "QPushButton {color: white; background-color: #4B0082; border-radius: 2px;}"  "QPushButton:hover{{"
            "background: #310062; border:none;}}")
        self.restartbtn.hide()
        self.levelsbtn.setStyleSheet(
            "QPushButton {color: white; background-color: #4B0082; border-radius: 2px;}"  "QPushButton:hover{{"
            "background: #310062; border:none;}}")
        self.levelsbtn.hide()
        self.pausebtn.clicked.connect(self.pauseevent)
        self.restartbtn.clicked.connect(self.restartevent)
        self.levelsbtn.clicked.connect(self.levelsevent)
        self.continuebtn.clicked.connect(self.continueevent)
        self.level4label.hide()
        for i in range(1, 25):
            eval(
                f"self.btn{i}.setStyleSheet('QPushButton {{background-color: #4B0082; border-radius: 3px; color: "
                f"white}}'\n"
                f"        \"QPushButton:hover{{background: #310062; border:none;}}\")")
        for i in range(1, 25):
            eval(f"""self.btn{i}.clicked.connect(self.clickevent{i})""")
        for i in range(1, 25):
            eval(f"self.btn{i}_2.setStyleSheet('QPushButton {{background-color: white; border-radius: 3px; }}')")
        for i in range(1, 25):
            eval(f'self.btn{i}_2.hide()')
        self.btn2.hide()
        self.btn6.hide()
        self.btn7.hide()
        self.btn2_2.show()
        self.btn6_2.show()
        self.btn7_2.show()

    def updateUptime(self):
        self.time += 1
        self.settimer(self.time)

    def settimer(self, int):
        self.time = int
        self.timer.setText(time.strftime('%M:%S', time.gmtime(self.time)))

    def pauseevent(self):
        self.timerUp.stop()
        self.pausebtn.hide()
        self.restartbtn.show()
        self.levelsbtn.show()
        self.pauselabel.show()
        for i in range(1, 25):
            eval(f"""self.btn{i}.setEnabled(False)""")
        self.continuebtn.show()
        self.level3label.hide()
        for i in range(1, 25):
            eval(f"""self.btn{i}.setStyleSheet('QPushButton {{background-color: #310062; }}')""")

    def continueevent(self):
        self.timerUp.start()
        self.restartbtn.hide()
        self.levelsbtn.hide()
        self.continuebtn.hide()
        self.pauselabel.hide()
        for i in range(1, 25):
            eval(f"""self.btn{i}.setEnabled(True)""")
        for i in range(1, 25):
            eval(
                f"self.btn{i}.setStyleSheet('QPushButton {{background-color: #4B0082; border-radius: 3px; color: "
                f"white}}'\n"
                f"        \"QPushButton:hover{{background: #310062; border:none;}}\")")
        self.pausebtn.show()
        self.level3label.show()

    def restartevent(self):
        self.newlevel = Level3(self.name)
        self.newlevel.show()
        self.close()

    def levelsevent(self):
        self.levels2 = Levels2(self.name)
        self.levels2.show()
        self.close()

    def clickevent1(self):
        self.btn1.disconnect()
        self.btn1.hide()
        self.btn1_2.show()
        self.checkcounter()

    def clickevent2(self):
        pass

    def clickevent3(self):
        self.btn3.setText('X')
        self.btn3.disconnect()
        self.checkerrors()

    def clickevent4(self):
        self.btn4.setText('X')
        self.btn4.disconnect()
        self.checkerrors()

    def clickevent5(self):
        self.btn5.disconnect()
        self.btn5.hide()
        self.btn5_2.show()
        self.checkcounter()

    def clickevent6(self):
        pass

    def clickevent7(self):
        pass

    def clickevent8(self):
        self.btn8.setText('X')
        self.btn8.disconnect()
        self.checkerrors()

    def clickevent9(self):
        self.btn9.setText('X')
        self.btn9.disconnect()
        self.checkerrors()

    def clickevent10(self):
        self.btn10.setText('X')
        self.btn10.disconnect()
        self.checkerrors()

    def clickevent11(self):
        self.btn11.setText('X')
        self.btn11.disconnect()
        self.checkerrors()

    def clickevent12(self):
        self.btn12.disconnect()
        self.btn12.hide()
        self.btn12_2.show()
        self.checkcounter()

    def clickevent13(self):
        self.btn13.disconnect()
        self.btn13.hide()
        self.btn13_2.show()
        self.checkcounter()

    def clickevent14(self):
        self.btn14.setText('X')
        self.btn14.disconnect()
        self.checkerrors()

    def clickevent15(self):
        self.btn15.setText('X')
        self.btn15.disconnect()
        self.checkerrors()

    def clickevent16(self):
        self.btn16.setText('X')
        self.btn16.disconnect()
        self.checkerrors()

    def clickevent17(self):
        self.btn17.setText('X')
        self.btn17.disconnect()
        self.checkerrors()

    def clickevent19(self):
        self.btn19.setText('X')
        self.btn19.disconnect()
        self.checkerrors()

    def clickevent20(self):
        self.btn20.setText('X')
        self.btn20.disconnect()
        self.checkerrors()

    def clickevent21(self):
        self.btn21.setText('X')
        self.btn21.disconnect()
        self.checkerrors()

    def clickevent22(self):
        self.btn22.setText('X')
        self.btn22.disconnect()
        self.checkerrors()

    def clickevent18(self):
        self.btn18.disconnect()
        self.btn18.hide()
        self.btn18_2.show()
        self.checkcounter()

    def clickevent23(self):
        self.btn23.disconnect()
        self.btn23.hide()
        self.btn23_2.show()
        self.checkcounter()

    def clickevent24(self):
        self.btn24.disconnect()
        self.btn24.hide()
        self.btn24_2.show()
        self.checkcounter()

    def checkcounter(self):
        self.count += 1
        if self.count == 7:
            self.win = Win(self.name, self.time)

            con = sqlite3.connect('records.db')
            cur = con.cursor()
            cur.execute('''UPDATE records
                        SET all_attemps = all_attemps + 1
                        WHERE name == '%s' '''%(self.name))

            cur.execute('''INSERT INTO statistic(time) VALUES(%s)'''%(self.time))

            cur.execute('''UPDATE records 
                        SET best_time = (SELECT MIN(time) FROM statistic)
                        WHERE name == '%s' '''%(self.name))
            con.commit()
            con.close()
            self.win.show()
            self.close()

    def checkerrors(self):
        self.errors += 1
        if self.errors == 3:
            self.lose = Lose(self.name)
            self.lose.show()
            self.close()


class Level4(QMainWindow):
    timeout = pyqtSignal()

    def __init__(self, name):
        self.lose = None
        self.win = None
        self.name = name
        super().__init__()
        self.setWindowTitle('Level4')
        self.levels2 = None
        self.newlevel = None
        uic.loadUi('level34.ui', self)

        self.time = 0
        self.timerUp = QTimer()
        self.timerUp.setInterval(1000)
        self.timerUp.timeout.connect(self.updateUptime)
        self.timerUp.start()

        self.centralwidget.setStyleSheet("#centralwidget {background: #270847;}")
        self.count = 0
        self.errors = 0
        self.line2.hide()
        self.pauselabel.hide()
        self.continuebtn.setStyleSheet(
            "QPushButton {color: white; background-color: #4B0082; border-radius: 2px;}"  "QPushButton:hover{{"
            "background: #310062; border:none;}}")
        self.continuebtn.hide()
        self.pausebtn.setStyleSheet(
            "QPushButton {color: white; background-color: #4B0082; border-radius: 2px;}"  "QPushButton:hover{{"
            "background: #310062; border:none;}}")
        self.restartbtn.setStyleSheet(
            "QPushButton {color: white; background-color: #4B0082; border-radius: 2px;}"  "QPushButton:hover{{"
            "background: #310062; border:none;}}")
        self.restartbtn.hide()
        self.levelsbtn.setStyleSheet(
            "QPushButton {color: white; background-color: #4B0082; border-radius: 2px;}"  "QPushButton:hover{{"
            "background: #310062; border:none;}}")
        self.levelsbtn.hide()
        self.pausebtn.clicked.connect(self.pauseevent)
        self.restartbtn.clicked.connect(self.restartevent)
        self.levelsbtn.clicked.connect(self.levelsevent)
        self.continuebtn.clicked.connect(self.continueevent)
        self.level3label.hide()
        for i in range(1, 25):
            eval(
                f"self.btn{i}.setStyleSheet('QPushButton {{background-color: #4B0082; border-radius: 3px; color: "
                f"white}}'\n"
                f"        \"QPushButton:hover{{background: #310062; border:none;}}\")")
        for i in range(1, 25):
            eval(f"""self.btn{i}.clicked.connect(self.clickevent{i})""")
        for i in range(1, 25):
            eval(f"self.btn{i}_2.setStyleSheet('QPushButton {{background-color: white; border-radius: 3px; }}')")
        for i in range(1, 25):
            eval(f'self.btn{i}_2.hide()')
        self.btn1.hide()
        self.btn13.hide()
        self.btn14.hide()
        self.btn1_2.show()
        self.btn13_2.show()
        self.btn14_2.show()

    def updateUptime(self):
        self.time += 1
        self.settimer(self.time)

    def settimer(self, int):
        self.time = int
        self.timer.setText(time.strftime('%M:%S', time.gmtime(self.time)))

    def pauseevent(self):
        self.timerUp.stop()
        self.pausebtn.hide()
        self.restartbtn.show()
        self.levelsbtn.show()
        self.pauselabel.show()
        for i in range(1, 25):
            eval(f"""self.btn{i}.setEnabled(False)""")
        self.continuebtn.show()
        self.level4label.hide()
        for i in range(1, 25):
            eval(f"""self.btn{i}.setStyleSheet('QPushButton {{background-color: #310062; }}')""")

    def continueevent(self):
        self.timerUp.start()
        self.restartbtn.hide()
        self.levelsbtn.hide()
        self.continuebtn.hide()
        self.pauselabel.hide()
        for i in range(1, 25):
            eval(f"""self.btn{i}.setEnabled(True)""")
        for i in range(1, 25):
            eval(
                f"self.btn{i}.setStyleSheet('QPushButton {{background-color: #4B0082; border-radius: 3px; color: "
                f"white}}'\n"
                f"        \"QPushButton:hover{{background: #310062; border:none;}}\")")
        self.pausebtn.show()
        self.level4label.show()

    def restartevent(self):
        self.newlevel = Level4(self.name)
        self.newlevel.show()
        self.close()

    def levelsevent(self):
        self.levels2 = Levels2(self.name)
        self.levels2.show()
        self.close()

    def clickevent1(self):
        pass

    def clickevent2(self):
        self.btn3.setText('X')
        self.btn3.disconnect()
        self.checkerrors()

    def clickevent3(self):
        self.btn3.setText('X')
        self.btn3.disconnect()
        self.checkerrors()

    def clickevent4(self):
        self.btn4.setText('X')
        self.btn4.disconnect()
        self.checkerrors()

    def clickevent5(self):
        self.btn5.setText('X')
        self.btn5.disconnect()
        self.checkerrors()

    def clickevent6(self):
        self.btn6.disconnect()
        self.btn6.hide()
        self.btn6_2.show()
        self.checkcounter()

    def clickevent7(self):
        self.btn7.disconnect()
        self.btn7.hide()
        self.btn7_2.show()
        self.checkcounter()

    def clickevent8(self):
        self.btn8.disconnect()
        self.btn8.hide()
        self.btn8_2.show()
        self.checkcounter()

    def clickevent9(self):
        self.btn9.setText('X')
        self.btn9.disconnect()
        self.checkerrors()

    def clickevent10(self):
        self.btn10.setText('X')
        self.btn10.disconnect()
        self.checkerrors()

    def clickevent11(self):
        self.btn11.disconnect()
        self.btn11.hide()
        self.btn11_2.show()
        self.checkcounter()

    def clickevent12(self):
        self.btn12.disconnect()
        self.btn12.hide()
        self.btn12_2.show()
        self.checkcounter()

    def clickevent13(self):
        pass

    def clickevent14(self):
        pass

    def clickevent15(self):
        self.btn15.setText('X')
        self.btn15.disconnect()
        self.checkerrors()

    def clickevent16(self):
        self.btn16.setText('X')
        self.btn16.disconnect()
        self.checkerrors()

    def clickevent17(self):
        self.btn17.disconnect()
        self.btn17.hide()
        self.btn17_2.show()
        self.checkcounter()

    def clickevent19(self):
        self.btn19.disconnect()
        self.btn19.hide()
        self.btn19_2.show()
        self.checkcounter()

    def clickevent20(self):
        self.btn20.setText('X')
        self.btn20.disconnect()
        self.checkerrors()

    def clickevent21(self):
        self.btn21.setText('X')
        self.btn21.disconnect()
        self.checkerrors()

    def clickevent22(self):
        self.btn22.setText('X')
        self.btn22.disconnect()
        self.checkerrors()

    def clickevent18(self):
        self.btn18.disconnect()
        self.btn18.hide()
        self.btn18_2.show()
        self.checkcounter()

    def clickevent23(self):
        self.btn23.setText('X')
        self.btn23.disconnect()
        self.checkerrors()

    def clickevent24(self):
        self.btn24.disconnect()
        self.btn24.hide()
        self.btn24_2.show()
        self.checkcounter()

    def checkcounter(self):
        self.count += 1
        if self.count == 9:
            self.win = Win(self.name, self.time)

            con = sqlite3.connect('records.db')
            cur = con.cursor()
            cur.execute('''UPDATE records
                        SET all_attemps = all_attemps + 1
                        WHERE name == '%s' '''%(self.name))

            cur.execute('''INSERT INTO statistic(time) VALUES(%s)'''%(self.time))

            cur.execute('''UPDATE records 
                        SET best_time = (SELECT MIN(time) FROM statistic)
                        WHERE name == '%s' '''%(self.name))
            con.commit()
            con.close()
            self.win.show()
            self.close()

    def checkerrors(self):
        self.errors += 1
        if self.errors == 3:
            self.lose = Lose(self.name)
            self.lose.show()
            self.close()


class Level5(QMainWindow):
    timeout = pyqtSignal()

    def __init__(self, name):
        self.lose = None
        self.win = None
        self.name = name
        super().__init__()
        self.setWindowTitle('Level5')
        self.levels2 = None
        self.newlevel = None
        uic.loadUi('level5.ui', self)

        self.time = 0
        self.timerUp = QTimer()
        self.timerUp.setInterval(1000)
        self.timerUp.timeout.connect(self.updateUptime)
        self.timerUp.start()

        self.centralwidget.setStyleSheet("#centralwidget {background: #270847;}")
        self.count = 0
        self.errors = 0
        self.pauselabel.hide()
        self.continuebtn.setStyleSheet(
            "QPushButton {color: white; background-color: #4B0082; border-radius: 2px;}"  "QPushButton:hover{{"
            "background: #310062; border:none;}}")
        self.continuebtn.hide()
        self.pausebtn.setStyleSheet(
            "QPushButton {color: white; background-color: #4B0082; border-radius: 2px;}"  "QPushButton:hover{{"
            "background: #310062; border:none;}}")
        self.restartbtn.setStyleSheet(
            "QPushButton {color: white; background-color: #4B0082; border-radius: 2px;}"  "QPushButton:hover{{"
            "background: #310062; border:none;}}")
        self.restartbtn.hide()
        self.levelsbtn.setStyleSheet(
            "QPushButton {color: white; background-color: #4B0082; border-radius: 2px;}"  "QPushButton:hover{{"
            "background: #310062; border:none;}}")
        self.levelsbtn.hide()
        self.pausebtn.clicked.connect(self.pauseevent)
        self.restartbtn.clicked.connect(self.restartevent)
        self.levelsbtn.clicked.connect(self.levelsevent)
        self.continuebtn.clicked.connect(self.continueevent)
        for i in range(1, 37):
            eval(
                f"self.btn{i}.setStyleSheet('QPushButton {{background-color: #4B0082; border-radius: 3px; color: "
                f"white}}'\n"
                f"        \"QPushButton:hover{{background: #310062; border:none;}}\")")
        for i in range(1, 37):
            eval(f"""self.btn{i}.clicked.connect(self.clickevent{i})""")
        for i in range(1, 37):
            eval(f"self.btn{i}_2.setStyleSheet('QPushButton {{background-color: white; border-radius: 3px; }}')")
        for i in range(1, 37):
            eval(f'self.btn{i}_2.hide()')
        self.btn22.hide()
        self.btn26.hide()
        self.btn36.hide()
        self.btn22_2.show()
        self.btn26_2.show()
        self.btn36_2.show()

    def updateUptime(self):
        self.time += 1
        self.settimer(self.time)

    def settimer(self, int):
        self.time = int
        self.timer.setText(time.strftime('%M:%S', time.gmtime(self.time)))

    def pauseevent(self):
        self.timerUp.stop()
        self.pausebtn.hide()
        self.restartbtn.show()
        self.levelsbtn.show()
        self.pauselabel.show()
        for i in range(1, 37):
            eval(f"""self.btn{i}.setEnabled(False)""")
        self.continuebtn.show()
        self.level5label.hide()
        for i in range(1, 37):
            eval(f"""self.btn{i}.setStyleSheet('QPushButton {{background-color: #310062; }}')""")

    def continueevent(self):
        self.timerUp.start()
        self.restartbtn.hide()
        self.levelsbtn.hide()
        self.continuebtn.hide()
        self.pauselabel.hide()
        for i in range(1, 37):
            eval(f"""self.btn{i}.setEnabled(True)""")
        for i in range(1, 37):
            eval(
                f"self.btn{i}.setStyleSheet('QPushButton {{background-color: #4B0082; border-radius: 3px; color: "
                f"white}}'\n"
                f"        \"QPushButton:hover{{background: #310062; border:none;}}\")")
        self.pausebtn.show()
        self.level5label.show()

    def restartevent(self):
        self.newlevel = Level5(self.name)
        self.newlevel.show()
        self.close()

    def levelsevent(self):
        self.levels2 = Levels2(self.name)
        self.levels2.show()
        self.close()

    def clickevent1(self):
        self.btn1.disconnect()
        self.btn1.hide()
        self.btn1_2.show()
        self.checkcounter()

    def clickevent2(self):
        self.btn2.setText('X')
        self.btn2.disconnect()
        self.checkerrors()

    def clickevent3(self):
        self.btn3.setText('X')
        self.btn3.disconnect()
        self.checkerrors()

    def clickevent4(self):
        self.btn4.setText('X')
        self.btn4.disconnect()
        self.checkerrors()

    def clickevent5(self):
        self.btn5.setText('X')
        self.btn5.disconnect()
        self.checkerrors()

    def clickevent6(self):
        self.btn6.setText('X')
        self.btn6.disconnect()
        self.checkerrors()

    def clickevent7(self):
        self.btn7.setText('X')
        self.btn7.disconnect()
        self.checkerrors()

    def clickevent8(self):
        self.btn8.disconnect()
        self.btn8.hide()
        self.btn8_2.show()
        self.checkcounter()

    def clickevent9(self):
        self.btn9.setText('X')
        self.btn9.disconnect()
        self.checkerrors()

    def clickevent10(self):
        self.btn10.setText('X')
        self.btn10.disconnect()
        self.checkerrors()

    def clickevent11(self):
        self.btn11.setText('X')
        self.btn11.disconnect()
        self.checkerrors()

    def clickevent12(self):
        self.btn12.setText('X')
        self.btn12.disconnect()
        self.checkerrors()

    def clickevent13(self):
        self.btn13.setText('X')
        self.btn13.disconnect()
        self.checkerrors()

    def clickevent14(self):
        self.btn14.setText('X')
        self.btn14.disconnect()
        self.checkerrors()

    def clickevent15(self):
        self.btn15.disconnect()
        self.btn15.hide()
        self.btn15_2.show()
        self.checkcounter()

    def clickevent16(self):
        self.btn16.disconnect()
        self.btn16.hide()
        self.btn16_2.show()
        self.checkcounter()

    def clickevent17(self):
        self.btn17.setText('X')
        self.btn17.disconnect()
        self.checkerrors()

    def clickevent18(self):
        self.btn18.setText('X')
        self.btn18.disconnect()
        self.checkerrors()

    def clickevent19(self):
        self.btn19.setText('X')
        self.btn19.disconnect()
        self.checkerrors()

    def clickevent20(self):
        self.btn20.setText('X')
        self.btn20.disconnect()
        self.checkerrors()

    def clickevent21(self):
        self.btn21.disconnect()
        self.btn21.hide()
        self.btn21_2.show()
        self.checkcounter()

    def clickevent22(self):
        pass

    def clickevent23(self):
        self.btn23.setText('X')
        self.btn23.disconnect()
        self.checkerrors()

    def clickevent24(self):
        self.btn24.setText('X')
        self.btn24.disconnect()
        self.checkerrors()

    def clickevent25(self):
        self.btn25.setText('X')
        self.btn25.disconnect()
        self.checkerrors()

    def clickevent26(self):
        pass

    def clickevent27(self):
        self.btn27.setText('X')
        self.btn27.disconnect()
        self.checkerrors()

    def clickevent28(self):
        self.btn28.setText('X')
        self.btn28.disconnect()
        self.checkerrors()

    def clickevent29(self):
        self.btn29.disconnect()
        self.btn29.hide()
        self.btn29_2.show()
        self.checkcounter()

    def clickevent30(self):
        self.btn30.setText('X')
        self.btn30.disconnect()
        self.checkerrors()

    def clickevent31(self):
        self.btn31.disconnect()
        self.btn31.hide()
        self.btn31_2.show()
        self.checkcounter()

    def clickevent32(self):
        self.btn32.setText('X')
        self.btn32.disconnect()
        self.checkerrors()

    def clickevent33(self):
        self.btn33.setText('X')
        self.btn33.disconnect()
        self.checkerrors()

    def clickevent34(self):
        self.btn34.setText('X')
        self.btn34.disconnect()
        self.checkerrors()

    def clickevent35(self):
        self.btn35.setText('X')
        self.btn35.disconnect()
        self.checkerrors()

    def clickevent36(self):
        pass

    def checkcounter(self):
        self.count += 1
        if self.count == 7:
            self.win = Win(self.name, self.time)

            con = sqlite3.connect('records.db')
            cur = con.cursor()
            cur.execute('''UPDATE records
                        SET all_attemps = all_attemps + 1
                        WHERE name == '%s' '''%(self.name))

            cur.execute('''INSERT INTO statistic(time) VALUES(%s)'''%(self.time))

            cur.execute('''UPDATE records 
                        SET best_time = (SELECT MIN(time) FROM statistic)
                        WHERE name == '%s' '''%(self.name))
            con.commit()
            con.close()
            self.win.show()
            self.close()

    def checkerrors(self):
        self.errors += 1
        if self.errors == 3:
            self.lose = Lose(self.name)

            self.lose.show()
            self.close()


class Lose(QMainWindow):
    def __init__(self, name):
        self.name = name
        super().__init__()
        self.menu = None
        self.levels = None
        uic.loadUi('lose.ui', self)
        self.centralwidget.setStyleSheet("#centralwidget {background: #270847;}")
        self.levelsbtn.setStyleSheet(
            "QPushButton {color: white; background-color: #4B0082; border-radius: 2px;}"  "QPushButton:hover{{"
            "background: #310062; border:none;}}")
        self.menubtn.setStyleSheet(
            "QPushButton {color: white; background-color: #4B0082; border-radius: 2px;}"  "QPushButton:hover{{"
            "background: #310062; border:none;}}")
        self.levelsbtn.clicked.connect(self.levelsevent)
        self.menubtn.clicked.connect(self.menuevent)
        self.pixmap = QPixmap('pic10' + str(random.randint(1, 5)) + '.jpg')
        self.piclabel.setPixmap(self.pixmap)

    def levelsevent(self):
        self.levels = Levels2(self.name)
        self.levels.show()
        self.close()

    def menuevent(self):
        self.menu = MainMenu()
        self.menu.show()
        self.close()


class Records(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('records.ui', self)
        self.centralwidget.setStyleSheet("#centralwidget {background: #270847;}")
        self.recbtn.setStyleSheet(
            "QPushButton {color: white; background-color: #4B0082; border-radius: 2px;}"  "QPushButton:hover{{"
            "background: #310062; border:none;}}")
        self.statbtn.setStyleSheet(
            "QPushButton {color: white; background-color: #4B0082; border-radius: 2px;}"  "QPushButton:hover{{"
            "background: #310062; border:none;}}")
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('records.db')
        db.open()
        self.model = QSqlTableModel(self)
        self.model.setTable("records")
        self.model.select()
        self.tableView.setModel(self.model)

        self.model2 = QSqlTableModel(self)
        self.model2.setTable("statistic")
        self.model2.select()
        self.tableView_2.setModel(self.model2)
        self.recbtn.clicked.connect(self.records)
        self.statbtn.clicked.connect(self.stat)
        self.tableView_2.hide()

    def records(self):
        self.tableView.show()
        self.tableView_2.hide()

    def stat(self):
        self.tableView.hide()
        self.tableView_2.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainMenu()
    ex.show()
    sys.exit(app.exec_())
