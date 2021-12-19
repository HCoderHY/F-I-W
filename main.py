# -*- coding: utf-8 -*-
import playsound
from gtts import gTTS
import random
import speech_recognition as sr
import webbrowser
import os
from PyQt5 import QtCore, QtGui, QtWidgets
def say(message):
    voise = gTTS(message, lang="ru")
    fvn = "-audio-"+str(random.randint(-100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000))+".mp3"
    voise.save(fvn)
    playsound.playsound(fvn)
    os.system(f"del {fvn}")
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1366, 41))
        font = QtGui.QFont()
        font.setFamily("Particle")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("background: #221F1F;color: white;")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 120, 221, 101))
        font = QtGui.QFont()
        font.setFamily("Particle")
        font.setPointSize(37)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background: #221F1F;color: white;border: 0px solid white;border-radius: 5px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 120, 201, 101))
        font = QtGui.QFont()
        font.setFamily("Particle")
        font.setPointSize(34)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background: #221F1F;color: white;border: 0px solid white;border-radius: 5px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(910, 120, 201, 101))
        font = QtGui.QFont()
        font.setFamily("Particle")
        font.setPointSize(42)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background: #221F1F;color: white;border: 0px solid white;border-radius: 5px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(470, 120, 201, 101))
        font = QtGui.QFont()
        font.setFamily("Particle")
        font.setPointSize(28)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background: #221F1F;color: white;border: 0px solid white;border-radius: 5px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(690, 120, 201, 101))
        font = QtGui.QFont()
        font.setFamily("Particle")
        font.setPointSize(28)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background: #221F1F;color: white;border: 0px solid white;border-radius: 5px;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(690, 240, 201, 101))
        font = QtGui.QFont()
        font.setFamily("Particle")
        font.setPointSize(28)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background: #221F1F;color: white;border: 0px solid white;border-radius: 5px;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 240, 221, 101))
        font = QtGui.QFont()
        font.setFamily("Particle")
        font.setPointSize(37)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background: #221F1F;color: white;border: 0px solid white;border-radius: 5px;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(470, 240, 201, 101))
        font = QtGui.QFont()
        font.setFamily("Particle")
        font.setPointSize(28)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background: #221F1F;color: white;border: 0px solid white;border-radius: 5px;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(250, 240, 201, 101))
        font = QtGui.QFont()
        font.setFamily("Particle")
        font.setPointSize(34)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background: #221F1F;color: white;border: 0px solid white;border-radius: 5px;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(910, 240, 201, 101))
        font = QtGui.QFont()
        font.setFamily("Particle")
        font.setPointSize(55)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background: #221F1F;color: white;border: 0px solid white;border-radius: 5px;")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(1130, 240, 221, 101))
        font = QtGui.QFont()
        font.setFamily("Particle")
        font.setPointSize(45)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("background: #221F1F;color: white;border: 0px solid white;border-radius: 5px;")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(1130, 120, 221, 101))
        font = QtGui.QFont()
        font.setFamily("Particle")
        font.setPointSize(42)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("background: #221F1F;color: white;border: 0px solid white;border-radius: 5px;")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(690, 360, 201, 101))
        font = QtGui.QFont()
        font.setFamily("Particle")
        font.setPointSize(60)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("background: #221F1F;color: white;border: 0px solid white;border-radius: 5px;")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(1130, 360, 221, 101))
        font = QtGui.QFont()
        font.setFamily("Particle")
        font.setPointSize(35)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("background: #221F1F;color: white;border: 0px solid white;border-radius: 5px;")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(470, 360, 201, 101))
        font = QtGui.QFont()
        font.setFamily("Particle")
        font.setPointSize(60)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("background: #221F1F;color: white;border: 0px solid white;border-radius: 5px;")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(250, 360, 201, 101))
        font = QtGui.QFont()
        font.setFamily("Particle")
        font.setPointSize(35)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("background: #221F1F;color: white;border: 0px solid white;border-radius: 5px;")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(910, 360, 201, 101))
        font = QtGui.QFont()
        font.setFamily("Particle")
        font.setPointSize(42)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("background: #221F1F;color: white;border: 0px solid white;border-radius: 5px;")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(10, 360, 221, 101))
        font = QtGui.QFont()
        font.setFamily("Particle")
        font.setPointSize(32)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet("background: #221F1F;color: white;border: 0px solid white;border-radius: 5px;")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(250, 480, 201, 101))
        font = QtGui.QFont()
        font.setFamily("Particle")
        font.setPointSize(42)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("background: #221F1F;color: white;border: 0px solid white;border-radius: 5px;")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(1130, 480, 221, 101))
        font = QtGui.QFont()
        font.setFamily("Particle")
        font.setPointSize(30)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet("background: #221F1F;color: white;border: 0px solid white;border-radius: 5px;")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(690, 480, 201, 101))
        font = QtGui.QFont()
        font.setFamily("Particle")
        font.setPointSize(35)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet("background: #221F1F;color: white;border: 0px solid white;border-radius: 5px;")
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(10, 480, 221, 101))
        font = QtGui.QFont()
        font.setFamily("Particle")
        font.setPointSize(20)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setStyleSheet("background: #221F1F;color: white;border: 0px solid white;border-radius: 5px;")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_23.setGeometry(QtCore.QRect(470, 480, 201, 101))
        font = QtGui.QFont()
        font.setFamily("Particle")
        font.setPointSize(55)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setStyleSheet("background: #221F1F;color: white;border: 0px solid white;border-radius: 5px;")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_24.setGeometry(QtCore.QRect(910, 480, 201, 101))
        font = QtGui.QFont()
        font.setFamily("Particle")
        font.setPointSize(42)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setStyleSheet("background: #221F1F;color: white;border: 0px solid white;border-radius: 5px;")
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_25.setGeometry(QtCore.QRect(10, 50, 1341, 61))
        font = QtGui.QFont()
        font.setFamily("Particle")
        font.setPointSize(34)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setStyleSheet("background: #221F1F;color: white;border: 0px solid white;border-radius: 5px;")
        self.pushButton_25.setObjectName("pushButton_25")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.function()
    def function(self):
        self.pushButton_25.clicked.connect(self.exit_of_programm)
        self.pushButton.clicked.connect(self.fgoogle)
        self.pushButton_2.clicked.connect(self.fyoutube)
        self.pushButton_3.clicked.connect(self.fyahoo)
        self.pushButton_4.clicked.connect(self.fek)
        self.pushButton_6.clicked.connect(self.fhowdy)
        self.pushButton_7.clicked.connect(self.fbmn)
        self.pushButton_5.clicked.connect(self.frozetka)
        self.pushButton_8.clicked.connect(self.fkp)
        self.pushButton_9.clicked.connect(self.fhdr)
        self.pushButton_10.clicked.connect(self.fbing)
        self.pushButton_11.clicked.connect(self.fddgo)
        self.pushButton_12.clicked.connect(self.fyandex)
        self.pushButton_13.clicked.connect(self.fask)
        self.pushButton_14.clicked.connect(self.frambler)
        self.pushButton_15.clicked.connect(self.faol)
        self.pushButton_16.clicked.connect(self.famazon)
        self.pushButton_17.clicked.connect(self.fbaidu)
        self.pushButton_18.clicked.connect(self.fali)
        self.pushButton_19.clicked.connect(self.fgithub)
        self.pushButton_20.clicked.connect(self.feld)
        self.pushButton_21.clicked.connect(self.fht)
        self.pushButton_22.clicked.connect(self.fsof)
        self.pushButton_23.clicked.connect(self.fbigl)
        self.pushButton_24.clicked.connect(self.fcomfi)
    def exit_of_programm(self):
        exit()
    def fgoogle(self):
        r = sr.Recognizer()
        with sr.Microphone(device_index = 1) as s:
            say("Что найти")
            r.adjust_for_ambient_noise(s)
            audio = r.listen(s)
        try:
            find = r.recognize_google(audio, language="ru-RU")
            webbrowser.open_new_tab("https://www.google.com/search?q="+find)
        except sr.UnknownValueError:
            find = "-"
        except sr.RequestError:
            say("Ошибка, проверьте подключение к интернету")
    def fyoutube(self):
        r = sr.Recognizer()
        with sr.Microphone(device_index = 1) as s:
            say("Что найти")
            r.adjust_for_ambient_noise(s)
            audio = r.listen(s)
        try:
            find = r.recognize_google(audio, language="ru-RU")
            webbrowser.open_new_tab("https://www.youtube.com/results?search_query="+find)
        except sr.UnknownValueError:
            find = "-"
        except sr.RequestError:
            say("Ошибка, проверьте подключение к интернету")
    def fhowdy(self):
        r = sr.Recognizer()
        with sr.Microphone(device_index = 1) as s:
            say("Что найти")
            r.adjust_for_ambient_noise(s)
            audio = r.listen(s)
        try:
            find = r.recognize_google(audio, language="ru-RU")
            webbrowser.open_new_tab("https://howdyho.net/search?q="+find)
        except sr.UnknownValueError:
            find = "-"
        except sr.RequestError:
            say("Ошибка, проверьте подключение к интернету")
    def fek(self):
        r = sr.Recognizer()
        with sr.Microphone(device_index = 1) as s:
            say("Что найти")
            r.adjust_for_ambient_noise(s)
            audio = r.listen(s)
        try:
            find = r.recognize_google(audio, language="ru-RU")
            webbrowser.open_new_tab("https://ek.ua/ek-list.php?search_="+find)
        except sr.UnknownValueError:
            find = "-"
        except sr.RequestError:
            say("Ошибка, проверьте подключение к интернету")
    def fyahoo(self):
        r = sr.Recognizer()
        with sr.Microphone(device_index = 1) as s:
            say("Что найти")
            r.adjust_for_ambient_noise(s)
            audio = r.listen(s)
        try:
            find = r.recognize_google(audio, language="ru-RU")
            webbrowser.open_new_tab("https://search.yahoo.com/search?p="+find+"&fr=yfp-t&ei=UTF-8&fp=1")
        except sr.UnknownValueError:
            find = "-"
        except sr.RequestError:
            say("Ошибка, проверьте подключение к интернету")
    def fbmn(self):
        r = sr.Recognizer()
        with sr.Microphone(device_index = 1) as s:
            say("Что найти")
            r.adjust_for_ambient_noise(s)
            audio = r.listen(s)
        try:
            find = r.recognize_google(audio, language="ru-RU")
            webbrowser.open_new_tab("https://news.bigmir.net/search?s="+find)
        except sr.UnknownValueError:
            find = "-"
        except sr.RequestError:
            say("Ошибка, проверьте подключение к интернету")
    def frozetka(self):
        r = sr.Recognizer()
        with sr.Microphone(device_index = 1) as s:
            say("Что найти")
            r.adjust_for_ambient_noise(s)
            audio = r.listen(s)
        try:
            find = r.recognize_google(audio, language="ru-RU")
            webbrowser.open_new_tab("https://rozetka.com.ua/ua/search/?text="+find)
        except sr.UnknownValueError:
            find = "-"
        except sr.RequestError:
            say("Ошибка, проверьте подключение к интернету")
    def fkp(self):
        r = sr.Recognizer()
        with sr.Microphone(device_index = 1) as s:
            say("Что найти")
            r.adjust_for_ambient_noise(s)
            audio = r.listen(s)
        try:
            find = r.recognize_google(audio, language="ru-RU")
            webbrowser.open_new_tab("https://www.kinopoisk.ru/index.php?kp_query="+find)
        except sr.UnknownValueError:
            find = "-"
        except sr.RequestError:
            say("Ошибка, проверьте подключение к интернету")
    def fhdr(self):
        r = sr.Recognizer()
        with sr.Microphone(device_index = 1) as s:
            say("Что найти")
            r.adjust_for_ambient_noise(s)
            audio = r.listen(s)
        try:
            find = r.recognize_google(audio, language="ru-RU")
            webbrowser.open_new_tab("https://rezka.ag/search/?do=search&subaction=search&q="+find)
        except sr.UnknownValueError:
            find = "-"
        except sr.RequestError:
            say("Ошибка, проверьте подключение к интернету")
    def fbing(self):
        r = sr.Recognizer()
        with sr.Microphone(device_index = 1) as s:
            say("Что найти")
            r.adjust_for_ambient_noise(s)
            audio = r.listen(s)
        try:
            find = r.recognize_google(audio, language="ru-RU")
            webbrowser.open_new_tab("https://www.bing.com/search?q="+find)
        except sr.UnknownValueError:
            find = "-"
        except sr.RequestError:
            say("Ошибка, проверьте подключение к интернету")
    def fddgo(self):
        r = sr.Recognizer()
        with sr.Microphone(device_index = 1) as s:
            say("Что найти")
            r.adjust_for_ambient_noise(s)
            audio = r.listen(s)
        try:
            find = r.recognize_google(audio, language="ru-RU")
            webbrowser.open_new_tab("https://duckduckgo.com/?q="+find)
        except sr.UnknownValueError:
            find = "-"
        except sr.RequestError:
            say("Ошибка, проверьте подключение к интернету")
    def fyandex(self):
        r = sr.Recognizer()
        with sr.Microphone(device_index = 1) as s:
            say("Что найти")
            r.adjust_for_ambient_noise(s)
            audio = r.listen(s)
        try:
            find = r.recognize_google(audio, language="ru-RU")
            webbrowser.open_new_tab("https://yandex.ua/search/?lr=145&text="+find)
        except sr.UnknownValueError:
            find = "-"
        except sr.RequestError:
            say("Ошибка, проверьте подключение к интернету")
    def fask(self):
        r = sr.Recognizer()
        with sr.Microphone(device_index = 1) as s:
            say("Что найти")
            r.adjust_for_ambient_noise(s)
            audio = r.listen(s)
        try:
            find = r.recognize_google(audio, language="ru-RU")
            webbrowser.open_new_tab("https://www.ask.com/web?q="+find)
        except sr.UnknownValueError:
            find = "-"
        except sr.RequestError:
            say("Ошибка, проверьте подключение к интернету")
    def frambler(self):
        r = sr.Recognizer()
        with sr.Microphone(device_index = 1) as s:
            say("Что найти")
            r.adjust_for_ambient_noise(s)
            audio = r.listen(s)
        try:
            find = r.recognize_google(audio, language="ru-RU")
            webbrowser.open_new_tab("https://nova.rambler.ru/search?utm_source=head&utm_campaign=self_promo&utm_medium=form&utm_content=search&query="+find)
        except sr.UnknownValueError:
            find = "-"
        except sr.RequestError:
            say("Ошибка, проверьте подключение к интернету")
    def faol(self):
        r = sr.Recognizer()
        with sr.Microphone(device_index = 1) as s:
            say("Что найти")
            r.adjust_for_ambient_noise(s)
            audio = r.listen(s)
        try:
            find = r.recognize_google(audio, language="ru-RU")
            webbrowser.open_new_tab("https://suche.aol.de/aol/search?q="+find)
        except sr.UnknownValueError:
            find = "-"
        except sr.RequestError:
            say("Ошибка, проверьте подключение к интернету")
    def famazon(self):
        r = sr.Recognizer()
        with sr.Microphone(device_index = 1) as s:
            say("Что найти")
            r.adjust_for_ambient_noise(s)
            audio = r.listen(s)
        try:
            find = r.recognize_google(audio, language="ru-RU")
            webbrowser.open_new_tab("https://www.amazon.de/s?k="+find)
        except sr.UnknownValueError:
            find = "-"
        except sr.RequestError:
            say("Ошибка, проверьте подключение к интернету")
    def fbaidu(self):
        r = sr.Recognizer()
        with sr.Microphone(device_index = 1) as s:
            say("Что найти")
            r.adjust_for_ambient_noise(s)
            audio = r.listen(s)
        try:
            find = r.recognize_google(audio, language="ru-RU")
            webbrowser.open_new_tab("http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&ch=&tn=baidu&bar=&wd="+find+"&rn=&fenlei=256&oq=&rsv_pq=95e870d5000e5d9e&rsv_t=83f0JUIYT8SJj6v5UplMJ%2FJmyeQ0y4GiHZsgulblsaFibBYL1YhWL%2F7b4q9%2F&rqlang=en")
        except sr.UnknownValueError:
            find = "-"
        except sr.RequestError:
            say("Ошибка, проверьте подключение к интернету")
    def fali(self):
        r = sr.Recognizer()
        with sr.Microphone(device_index = 1) as s:
            say("Что найти")
            r.adjust_for_ambient_noise(s)
            audio = r.listen(s)
        try:
            find = r.recognize_google(audio, language="ru-RU")
            webbrowser.open_new_tab("https://de.aliexpress.com/premium/sd.html?d=y&origin=y&catId=0&initiative_id=SB_20211218134103&SearchText="+find)
        except sr.UnknownValueError:
            find = "-"
        except sr.RequestError:
            say("Ошибка, проверьте подключение к интернету")
    def fgithub(self):
        r = sr.Recognizer()
        with sr.Microphone(device_index = 1) as s:
            say("Что найти")
            r.adjust_for_ambient_noise(s)
            audio = r.listen(s)
        try:
            find = r.recognize_google(audio, language="ru-RU")
            webbrowser.open_new_tab("https://github.com/search?q="+find)
        except sr.UnknownValueError:
            find = "-"
        except sr.RequestError:
            say("Ошибка, проверьте подключение к интернету")
    def feld(self):
        r = sr.Recognizer()
        with sr.Microphone(device_index = 1) as s:
            say("Что найти")
            r.adjust_for_ambient_noise(s)
            audio = r.listen(s)
        try:
            find = r.recognize_google(audio, language="ru-RU")
            webbrowser.open_new_tab("https://eldorado.ua/search/?q="+find)
        except sr.UnknownValueError:
            find = "-"
        except sr.RequestError:
            say("Ошибка, проверьте подключение к интернету")
    def fht(self):
        r = sr.Recognizer()
        with sr.Microphone(device_index = 1) as s:
            say("Что найти")
            r.adjust_for_ambient_noise(s)
            audio = r.listen(s)
        try:
            find = r.recognize_google(audio, language="ru-RU")
            webbrowser.open_new_tab("https://hotline.ua/sr/?q="+find)
        except sr.UnknownValueError:
            find = "-"
        except sr.RequestError:
            say("Ошибка, проверьте подключение к интернету")
    def fsof(self):
        r = sr.Recognizer()
        with sr.Microphone(device_index = 1) as s:
            say("Что найти")
            r.adjust_for_ambient_noise(s)
            audio = r.listen(s)
        try:
            find = r.recognize_google(audio, language="ru-RU")
            webbrowser.open_new_tab("https://stackoverflow.com/search?q="+find)
        except sr.UnknownValueError:
            find = "-"
        except sr.RequestError:
            say("Ошибка, проверьте подключение к интернету")
    def fbigl(self):
        r = sr.Recognizer()
        with sr.Microphone(device_index = 1) as s:
            say("Что найти")
            r.adjust_for_ambient_noise(s)
            audio = r.listen(s)
        try:
            find = r.recognize_google(audio, language="ru-RU")
            webbrowser.open_new_tab("https://bigl.ua/ua/search?search_term="+find)
        except sr.UnknownValueError:
            find = "-"
        except sr.RequestError:
            say("Ошибка, проверьте подключение к интернету")
    def fcomfi(self):
        r = sr.Recognizer()
        with sr.Microphone(device_index = 1) as s:
            say("Что найти")
            r.adjust_for_ambient_noise(s)
            audio = r.listen(s)
        try:
            find = r.recognize_google(audio, language="ru-RU")
            webbrowser.open_new_tab("https://comfy.ua/ua/catalogsearch/result/?q="+find)
        except sr.UnknownValueError:
            find = "-"
        except sr.RequestError:
            say("Ошибка, проверьте подключение к интернету")
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "                                                                         Find in website"))
        self.pushButton.setText(_translate("MainWindow", "Google"))
        self.pushButton_2.setText(_translate("MainWindow", "YouTube"))
        self.pushButton_3.setText(_translate("MainWindow", "Yahoo"))
        self.pushButton_4.setText(_translate("MainWindow", "E-Katalog"))
        self.pushButton_6.setText(_translate("MainWindow", "Howdy ho"))
        self.pushButton_7.setText(_translate("MainWindow", "BigMir-net"))
        self.pushButton_5.setText(_translate("MainWindow", "Rozetka"))
        self.pushButton_8.setText(_translate("MainWindow", "Kinopoisk"))
        self.pushButton_9.setText(_translate("MainWindow", "HDrezka"))
        self.pushButton_10.setText(_translate("MainWindow", "BING"))
        self.pushButton_11.setText(_translate("MainWindow", "D-D go"))
        self.pushButton_12.setText(_translate("MainWindow", "Yandex"))
        self.pushButton_13.setText(_translate("MainWindow", "ASK"))
        self.pushButton_14.setText(_translate("MainWindow", "Rambler"))
        self.pushButton_15.setText(_translate("MainWindow", "AOL"))
        self.pushButton_16.setText(_translate("MainWindow", "amazon"))
        self.pushButton_17.setText(_translate("MainWindow", "BAIDU"))
        self.pushButton_18.setText(_translate("MainWindow", "aliexpress"))
        self.pushButton_19.setText(_translate("MainWindow", "Github"))
        self.pushButton_20.setText(_translate("MainWindow", "eldorado"))
        self.pushButton_21.setText(_translate("MainWindow", "hotline"))
        self.pushButton_22.setText(_translate("MainWindow", "Stack overflow"))
        self.pushButton_23.setText(_translate("MainWindow", "bigl"))
        self.pushButton_24.setText(_translate("MainWindow", "comfi"))
        self.pushButton_25.setText(_translate("MainWindow", "EXIT"))
import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
