# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CyberRefUIResultsBhmIkr.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_CyberRefResults(object):
    def setupUi(self, CyberRef):
        if not CyberRef.objectName():
            CyberRef.setObjectName(u"CyberRef")
        CyberRef.resize(1137, 877)
        CyberRef.setStyleSheet(u"background-color: rgb(36, 29, 50);")
        self.central = QWidget(CyberRef)
        self.central.setObjectName(u"central")
        self.SCANRESULTS_LABEL = QLabel(self.central)
        self.SCANRESULTS_LABEL.setObjectName(u"SCANRESULTS_LABEL")
        self.SCANRESULTS_LABEL.setGeometry(QRect(240, 70, 901, 91))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SCANRESULTS_LABEL.sizePolicy().hasHeightForWidth())
        self.SCANRESULTS_LABEL.setSizePolicy(sizePolicy)
        self.SCANRESULTS_LABEL.setStyleSheet(u"font: 36pt \"ProggyClean CE Nerd Font\";\n"
"color: rgb(255, 243, 219);")
        self.SCANRESULTS_LABEL.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.CYBERREFPIC = QLabel(self.central)
        self.CYBERREFPIC.setObjectName(u"CYBERREFPIC")
        self.CYBERREFPIC.setGeometry(QRect(0, 0, 231, 301))
        self.CYBERREFPIC.setPixmap(QPixmap(u"CyberRefLogo.png"))
        self.BACK_BUTTON = QPushButton(self.central)
        self.BACK_BUTTON.setObjectName(u"BACK_BUTTON")
        self.BACK_BUTTON.setGeometry(QRect(20, 800, 141, 51))
        self.BACK_BUTTON.setStyleSheet(u"font: 36pt \"ProggyClean CE Nerd Font\";\n"
"background-color: rgb(255, 243, 219);\n"
"color: rgb(86, 53, 66);")
        self.EXIT_BUTTON = QPushButton(self.central)
        self.EXIT_BUTTON.setObjectName(u"EXIT_BUTTON")
        self.EXIT_BUTTON.setGeometry(QRect(970, 800, 141, 51))
        self.EXIT_BUTTON.setStyleSheet(u"font: 36pt \"ProggyClean CE Nerd Font\";\n"
"background-color: rgb(255, 243, 219);\n"
"color: rgb(86, 53, 66);")
        self.MAINHARMLESS_LABEL = QLabel(self.central)
        self.MAINHARMLESS_LABEL.setObjectName(u"MAINHARMLESS_LABEL")
        self.MAINHARMLESS_LABEL.setGeometry(QRect(240, 170, 421, 41))
        sizePolicy.setHeightForWidth(self.MAINHARMLESS_LABEL.sizePolicy().hasHeightForWidth())
        self.MAINHARMLESS_LABEL.setSizePolicy(sizePolicy)
        self.MAINHARMLESS_LABEL.setStyleSheet(u"font: 36pt \"ProggyClean CE Nerd Font\";\n"
"color: rgb(38, 255, 0);")
        self.MAINHARMLESS_LABEL.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.MAINMALICIOUS_LABEL = QLabel(self.central)
        self.MAINMALICIOUS_LABEL.setObjectName(u"MAINMALICIOUS_LABEL")
        self.MAINMALICIOUS_LABEL.setGeometry(QRect(670, 170, 461, 41))
        sizePolicy.setHeightForWidth(self.MAINMALICIOUS_LABEL.sizePolicy().hasHeightForWidth())
        self.MAINMALICIOUS_LABEL.setSizePolicy(sizePolicy)
        self.MAINMALICIOUS_LABEL.setStyleSheet(u"font: 36pt \"ProggyClean CE Nerd Font\";\n"
"color: rgb(255, 0, 0);")
        self.MAINMALICIOUS_LABEL.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.MAINSUSPICIOUS_LABEL = QLabel(self.central)
        self.MAINSUSPICIOUS_LABEL.setObjectName(u"MAINSUSPICIOUS_LABEL")
        self.MAINSUSPICIOUS_LABEL.setGeometry(QRect(240, 230, 891, 41))
        sizePolicy.setHeightForWidth(self.MAINSUSPICIOUS_LABEL.sizePolicy().hasHeightForWidth())
        self.MAINSUSPICIOUS_LABEL.setSizePolicy(sizePolicy)
        self.MAINSUSPICIOUS_LABEL.setStyleSheet(u"font: 36pt \"ProggyClean CE Nerd Font\";\n"
"color: rgb(255, 255, 0);")
        self.MAINSUSPICIOUS_LABEL.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.MORERESULTS_LABEL = QLabel(self.central)
        self.MORERESULTS_LABEL.setObjectName(u"MORERESULTS_LABEL")
        self.MORERESULTS_LABEL.setGeometry(QRect(0, 310, 391, 481))
        sizePolicy.setHeightForWidth(self.MORERESULTS_LABEL.sizePolicy().hasHeightForWidth())
        self.MORERESULTS_LABEL.setSizePolicy(sizePolicy)
        self.MORERESULTS_LABEL.setStyleSheet(u"font: 36pt \"ProggyClean CE Nerd Font\";\n"
"color: rgb(255, 243, 219);")
        self.MORERESULTS_LABEL.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.VOTEHARMLESS_LABEL = QLabel(self.central)
        self.VOTEHARMLESS_LABEL.setObjectName(u"VOTEHARMLESS_LABEL")
        self.VOTEHARMLESS_LABEL.setGeometry(QRect(400, 360, 301, 111))
        sizePolicy.setHeightForWidth(self.VOTEHARMLESS_LABEL.sizePolicy().hasHeightForWidth())
        self.VOTEHARMLESS_LABEL.setSizePolicy(sizePolicy)
        self.VOTEHARMLESS_LABEL.setStyleSheet(u"font: 36pt \"ProggyClean CE Nerd Font\";\n"
"color: rgb(38, 255, 0);")
        self.VOTEHARMLESS_LABEL.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.VOTEMALICIOUS_LABEL = QLabel(self.central)
        self.VOTEMALICIOUS_LABEL.setObjectName(u"VOTEMALICIOUS_LABEL")
        self.VOTEMALICIOUS_LABEL.setGeometry(QRect(700, 360, 421, 111))
        sizePolicy.setHeightForWidth(self.VOTEMALICIOUS_LABEL.sizePolicy().hasHeightForWidth())
        self.VOTEMALICIOUS_LABEL.setSizePolicy(sizePolicy)
        self.VOTEMALICIOUS_LABEL.setStyleSheet(u"font: 36pt \"ProggyClean CE Nerd Font\";\n"
"color: rgb(255, 0, 0);")
        self.VOTEMALICIOUS_LABEL.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.REDCARD_LABEL = QLabel(self.central)
        self.REDCARD_LABEL.setObjectName(u"REDCARD_LABEL")
        self.REDCARD_LABEL.setGeometry(QRect(880, 70, 81, 81))
        self.REDCARD_LABEL.setPixmap(QPixmap(u"RedCardIcon.png"))
        self.REDCARD_LABEL.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.FANS_LABEL = QLabel(self.central)
        self.FANS_LABEL.setObjectName(u"FANS_LABEL")
        self.FANS_LABEL.setGeometry(QRect(150, 310, 121, 81))
        self.FANS_LABEL.setPixmap(QPixmap(u"FansIcon.png"))
        self.OUTGOINGLINKS_PIC_LABEL = QLabel(self.central)
        self.OUTGOINGLINKS_PIC_LABEL.setObjectName(u"OUTGOINGLINKS_PIC_LABEL")
        self.OUTGOINGLINKS_PIC_LABEL.setGeometry(QRect(150, 450, 91, 91))
        self.OUTGOINGLINKS_PIC_LABEL.setPixmap(QPixmap(u"OutgoingLinksIcon.png"))
        self.WEBTRACKERS_LABEL = QLabel(self.central)
        self.WEBTRACKERS_LABEL.setObjectName(u"WEBTRACKERS_LABEL")
        self.WEBTRACKERS_LABEL.setGeometry(QRect(150, 590, 101, 91))
        self.WEBTRACKERS_LABEL.setPixmap(QPixmap(u"TrackersIcon.png"))
        self.widget = QWidget(self.central)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(400, 480, 731, 311))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(13)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.OUTGOINGLINKS_EDITXT = QPlainTextEdit(self.widget)
        self.OUTGOINGLINKS_EDITXT.setObjectName(u"OUTGOINGLINKS_EDITXT")
        self.OUTGOINGLINKS_EDITXT.setStyleSheet(u"font: 36pt \"ProggyClean CE Nerd Font\";\n"
"color: rgb(255, 243, 219);")
        self.OUTGOINGLINKS_EDITXT.setReadOnly(True)

        self.verticalLayout.addWidget(self.OUTGOINGLINKS_EDITXT)

        self.TRACKERS_EDITXT = QPlainTextEdit(self.widget)
        self.TRACKERS_EDITXT.setObjectName(u"TRACKERS_EDITXT")
        self.TRACKERS_EDITXT.setStyleSheet(u"font: 36pt \"ProggyClean CE Nerd Font\";\n"
"color: rgb(255, 243, 219);")
        self.TRACKERS_EDITXT.setReadOnly(True)

        self.verticalLayout.addWidget(self.TRACKERS_EDITXT)

        CyberRef.setCentralWidget(self.central)

        self.retranslateUi(CyberRef)

        QMetaObject.connectSlotsByName(CyberRef)
    # setupUi

    def retranslateUi(self, CyberRef):
        CyberRef.setWindowTitle(QCoreApplication.translate("CyberRef", u"MainWindow", None))
        self.SCANRESULTS_LABEL.setText(QCoreApplication.translate("CyberRef", u"<html><head/><body><p><span style=\" font-size:48pt; color:#fff3db;\">Scan Results</span></p></body></html>", None))
        self.CYBERREFPIC.setText("")
        self.BACK_BUTTON.setText(QCoreApplication.translate("CyberRef", u"BACK", None))
        self.EXIT_BUTTON.setText(QCoreApplication.translate("CyberRef", u"EXIT", None))
        self.MAINHARMLESS_LABEL.setText(QCoreApplication.translate("CyberRef", u"<html><head/><body><p>Harmless : 50</p></body></html>", None))
        self.MAINMALICIOUS_LABEL.setText(QCoreApplication.translate("CyberRef", u"<html><head/><body><p>Malicious : 47</p></body></html>", None))
        self.MAINSUSPICIOUS_LABEL.setText(QCoreApplication.translate("CyberRef", u"<html><head/><body><p>Suspicious : 33</p></body></html>", None))
        self.MORERESULTS_LABEL.setText(QCoreApplication.translate("CyberRef", u"<html><head/><body><p align=\"right\"><br/></p><p align=\"right\">Community Votes -&gt;</p><p align=\"right\"><br/></p><p align=\"right\">Outgoing Links -&gt;</p><p align=\"right\"><br/></p><p align=\"right\">Web Trackers -&gt;</p><p align=\"right\"><br/></p><p align=\"right\"><br/></p><p align=\"right\"><br/></p><p align=\"right\"><br/></p></body></html>", None))
        self.VOTEHARMLESS_LABEL.setText(QCoreApplication.translate("CyberRef", u"<html><head/><body><p>Harmless : 50</p></body></html>", None))
        self.VOTEMALICIOUS_LABEL.setText(QCoreApplication.translate("CyberRef", u"<html><head/><body><p>Malicious : 47</p></body></html>", None))
        self.REDCARD_LABEL.setText("")
        self.FANS_LABEL.setText("")
        self.OUTGOINGLINKS_PIC_LABEL.setText("")
        self.WEBTRACKERS_LABEL.setText("")
        self.OUTGOINGLINKS_EDITXT.setPlainText(QCoreApplication.translate("CyberRef", u"https://example.com\n"
"https://example2.com\n"
"https://example3.com\n"
"https://example4.com", None))
        self.TRACKERS_EDITXT.setPlainText(QCoreApplication.translate("CyberRef", u"Example1\n"
"Example2\n"
"Example3\n"
"Example4\n"
"Example5", None))
    # retranslateUi

