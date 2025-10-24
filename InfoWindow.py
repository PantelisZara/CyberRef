# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CyberRefUIInfoIVTLgn.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_CyberRefInfo(object):
    def setupUi(self, CyberRef):
        if not CyberRef.objectName():
            CyberRef.setObjectName(u"CyberRef")
        CyberRef.resize(1137, 861)
        CyberRef.setStyleSheet(u"background-color: rgb(36, 29, 50);")
        self.central = QWidget(CyberRef)
        self.central.setObjectName(u"central")
        self.INFO_LABEL = QLabel(self.central)
        self.INFO_LABEL.setObjectName(u"INFO_LABEL")
        self.INFO_LABEL.setGeometry(QRect(0, 310, 1131, 351))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.INFO_LABEL.sizePolicy().hasHeightForWidth())
        self.INFO_LABEL.setSizePolicy(sizePolicy)
        self.INFO_LABEL.setStyleSheet(u"font: 36pt \"ProggyClean CE Nerd Font\";\n"
"color: rgb(255, 243, 219);")
        self.INFO_LABEL.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.INFO_LABEL.setWordWrap(True)
        self.CYBERREFPIC = QLabel(self.central)
        self.CYBERREFPIC.setObjectName(u"CYBERREFPIC")
        self.CYBERREFPIC.setGeometry(QRect(0, 0, 1121, 301))
        self.CYBERREFPIC.setPixmap(QPixmap(u"CyberRefLogo.png"))
        self.CYBERREFPIC.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.BACK_BUTTON = QPushButton(self.central)
        self.BACK_BUTTON.setObjectName(u"BACK_BUTTON")
        self.BACK_BUTTON.setGeometry(QRect(20, 790, 141, 51))
        self.BACK_BUTTON.setStyleSheet(u"font: 36pt \"ProggyClean CE Nerd Font\";\n"
"background-color: rgb(255, 243, 219);\n"
"color: rgb(86, 53, 66);")
        self.LINKS_LABEL = QLabel(self.central)
        self.LINKS_LABEL.setObjectName(u"LINKS_LABEL")
        self.LINKS_LABEL.setGeometry(QRect(860, 750, 271, 111))
        sizePolicy.setHeightForWidth(self.LINKS_LABEL.sizePolicy().hasHeightForWidth())
        self.LINKS_LABEL.setSizePolicy(sizePolicy)
        self.LINKS_LABEL.setStyleSheet(u"font: 36pt \"ProggyClean CE Nerd Font\";\n"
"color: rgb(255, 243, 219);")
        self.LINKS_LABEL.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.LINKS_LABEL.setWordWrap(True)
        self.LINKS_LABEL.setOpenExternalLinks(True)
        self.NAME_LABEL = QLabel(self.central)
        self.NAME_LABEL.setObjectName(u"NAME_LABEL")
        self.NAME_LABEL.setGeometry(QRect(170, 770, 291, 91))
        sizePolicy.setHeightForWidth(self.NAME_LABEL.sizePolicy().hasHeightForWidth())
        self.NAME_LABEL.setSizePolicy(sizePolicy)
        self.NAME_LABEL.setStyleSheet(u"font: 36pt \"ProggyClean CE Nerd Font\";\n"
"color: rgb(255, 243, 219);")
        self.NAME_LABEL.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.NAME_LABEL.setWordWrap(True)
        self.CHECKSTUFF_LABEL = QLabel(self.central)
        self.CHECKSTUFF_LABEL.setObjectName(u"CHECKSTUFF_LABEL")
        self.CHECKSTUFF_LABEL.setGeometry(QRect(520, 780, 301, 31))
        sizePolicy.setHeightForWidth(self.CHECKSTUFF_LABEL.sizePolicy().hasHeightForWidth())
        self.CHECKSTUFF_LABEL.setSizePolicy(sizePolicy)
        self.CHECKSTUFF_LABEL.setStyleSheet(u"font: 36pt \"ProggyClean CE Nerd Font\";\n"
"color: rgb(255, 243, 219);")
        self.CHECKSTUFF_LABEL.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.CHECKSTUFF_LABEL.setWordWrap(True)
        self.WHISTLE1 = QLabel(self.central)
        self.WHISTLE1.setObjectName(u"WHISTLE1")
        self.WHISTLE1.setGeometry(QRect(910, 740, 31, 41))
        self.WHISTLE1.setPixmap(QPixmap(u"WhistleIcon.png"))
        self.WHISTLE2 = QLabel(self.central)
        self.WHISTLE2.setObjectName(u"WHISTLE2")
        self.WHISTLE2.setGeometry(QRect(900, 780, 31, 41))
        self.WHISTLE2.setPixmap(QPixmap(u"WhistleIcon.png"))
        self.WHISTLE3 = QLabel(self.central)
        self.WHISTLE3.setObjectName(u"WHISTLE3")
        self.WHISTLE3.setGeometry(QRect(830, 820, 31, 31))
        self.WHISTLE3.setPixmap(QPixmap(u"WhistleIcon.png"))
        CyberRef.setCentralWidget(self.central)

        self.retranslateUi(CyberRef)

        QMetaObject.connectSlotsByName(CyberRef)
    # setupUi

    def retranslateUi(self, CyberRef):
        CyberRef.setWindowTitle(QCoreApplication.translate("CyberRef", u"MainWindow", None))
        self.INFO_LABEL.setText(QCoreApplication.translate("CyberRef", u"<html><head/><body><p><span style=\" font-size:28pt;\">CyberRef is a learning project designed to explore the fundamentals of cybersecurity analysis, user interface design, and application development.</span></p><p><span style=\" font-size:28pt;\"><br/>It allows users to check website safety information using the VirusTotal API and view results in a simple, modern interface.</span></p><p><span style=\" font-size:28pt;\">This application was created for educational purposes to help me learn more about cybersecurity tools, Python programming, and UI creation with Qt.</span></p></body></html>", None))
        self.CYBERREFPIC.setText("")
        self.BACK_BUTTON.setText(QCoreApplication.translate("CyberRef", u"BACK", None))
        self.LINKS_LABEL.setText(QCoreApplication.translate("CyberRef", u"<html><head/><body><p><a href=\"https://github.com/PantelisZara\"><span style=\" font-size:24pt; text-decoration: underline; color:#5294e2;\">Github</span></a></p><p><a href=\"http://www.linkedin.com/in/panteleimon-zarakis-a15496339\"><span style=\" font-size:24pt; text-decoration: underline; color:#5294e2;\">LinkedIn</span></a></p><p><span style=\" font-size:24pt;\">zarakisp@gmail.com<br/></span></p></body></html>", None))
        self.NAME_LABEL.setText(QCoreApplication.translate("CyberRef", u"<html><head/><body><p><span style=\" font-size:18pt;\">CyberRef</span></p><p><span style=\" font-size:18pt;\">A project made by Pantelis Zarakis</span></p></body></html>", None))
        self.CHECKSTUFF_LABEL.setText(QCoreApplication.translate("CyberRef", u"<html><head/><body><p><span style=\" font-size:24pt;\">Check out my stuff -&gt;<br/></span></p></body></html>", None))
        self.WHISTLE1.setText("")
        self.WHISTLE2.setText("")
        self.WHISTLE3.setText("")
    # retranslateUi

