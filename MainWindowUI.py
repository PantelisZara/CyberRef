# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CyberRefUIGBFiOc.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_CyberRefMain(object):
    def setupUi(self, CyberRef):
        if not CyberRef.objectName():
            CyberRef.setObjectName(u"CyberRef")
        CyberRef.resize(1137, 861)
        CyberRef.setStyleSheet(u"background-color: rgb(36, 29, 50);")
        self.central = QWidget(CyberRef)
        self.central.setObjectName(u"central")
        self.APILabel = QLabel(self.central)
        self.APILabel.setObjectName(u"APILabel")
        self.APILabel.setGeometry(QRect(240, 120, 901, 39))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.APILabel.sizePolicy().hasHeightForWidth())
        self.APILabel.setSizePolicy(sizePolicy)
        self.APILabel.setStyleSheet(u"font: 36pt \"ProggyClean CE Nerd Font\";")
        self.APILabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.CYBERREFPIC = QLabel(self.central)
        self.CYBERREFPIC.setObjectName(u"CYBERREFPIC")
        self.CYBERREFPIC.setGeometry(QRect(0, 0, 231, 301))
        self.CYBERREFPIC.setPixmap(QPixmap(u"CyberRefLogo.png"))
        self.API_EDITBOX = QPlainTextEdit(self.central)
        self.API_EDITBOX.setObjectName(u"API_EDITBOX")
        self.API_EDITBOX.setGeometry(QRect(340, 180, 701, 41))
        self.API_EDITBOX.setStyleSheet(u"background-color: rgb(255, 243, 219);\n"
"color: rgb(0, 0, 0);\n"
"font: 500 16pt \"Noto Sans Arabic UI Md\";")
        self.URL_label = QLabel(self.central)
        self.URL_label.setObjectName(u"URL_label")
        self.URL_label.setGeometry(QRect(240, 270, 901, 39))
        sizePolicy.setHeightForWidth(self.URL_label.sizePolicy().hasHeightForWidth())
        self.URL_label.setSizePolicy(sizePolicy)
        self.URL_label.setStyleSheet(u"font: 36pt \"ProggyClean CE Nerd Font\";")
        self.URL_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.URL_EDITBOX = QPlainTextEdit(self.central)
        self.URL_EDITBOX.setObjectName(u"URL_EDITBOX")
        self.URL_EDITBOX.setGeometry(QRect(340, 330, 701, 41))
        self.URL_EDITBOX.setStyleSheet(u"background-color: rgb(255, 243, 219);\n"
"color: rgb(0, 0, 0);\n"
"font: 500 16pt \"Noto Sans Arabic UI Md\";")
        self.START_BUTTON = QPushButton(self.central)
        self.START_BUTTON.setObjectName(u"START_BUTTON")
        self.START_BUTTON.setGeometry(QRect(410, 680, 311, 91))
        self.START_BUTTON.setStyleSheet(u"font: 48pt \"ProggyClean CE Nerd Font\";\n"
"background-color: rgb(255, 243, 219);\n"
"color: rgb(86, 53, 66);")
        self.INFO_BUTTON = QPushButton(self.central)
        self.INFO_BUTTON.setObjectName(u"INFO_BUTTON")
        self.INFO_BUTTON.setGeometry(QRect(20, 790, 141, 51))
        self.INFO_BUTTON.setStyleSheet(u"font: 36pt \"ProggyClean CE Nerd Font\";\n"
"background-color: rgb(255, 243, 219);\n"
"color: rgb(86, 53, 66);")
        self.EXIT_BUTTON = QPushButton(self.central)
        self.EXIT_BUTTON.setObjectName(u"EXIT_BUTTON")
        self.EXIT_BUTTON.setGeometry(QRect(970, 790, 141, 51))
        self.EXIT_BUTTON.setStyleSheet(u"font: 36pt \"ProggyClean CE Nerd Font\";\n"
"background-color: rgb(255, 243, 219);\n"
"color: rgb(86, 53, 66);")
        CyberRef.setCentralWidget(self.central)

        self.retranslateUi(CyberRef)

        QMetaObject.connectSlotsByName(CyberRef)
    # setupUi

    def retranslateUi(self, CyberRef):
        CyberRef.setWindowTitle(QCoreApplication.translate("CyberRef", u"MainWindow", None))
        self.APILabel.setText(QCoreApplication.translate("CyberRef", u"<html><head/><body><p><span style=\" color:#fff3db;\">Enter your API key</span></p></body></html>", None))
        self.CYBERREFPIC.setText("")
        self.URL_label.setText(QCoreApplication.translate("CyberRef", u"<html><head/><body><p><span style=\" color:#fff3db;\">Paste preferred URL</span></p></body></html>", None))
        self.START_BUTTON.setText(QCoreApplication.translate("CyberRef", u"START", None))
        self.INFO_BUTTON.setText(QCoreApplication.translate("CyberRef", u"INFO", None))
        self.EXIT_BUTTON.setText(QCoreApplication.translate("CyberRef", u"EXIT", None))
    # retranslateUi

