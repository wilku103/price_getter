# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QDoubleSpinBox,
    QLabel, QListView, QMainWindow, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.currencies = QListView(self.centralwidget)
        self.currencies.setObjectName(u"currencies")
        self.currencies.setGeometry(QRect(60, 150, 256, 192))
        self.currencies.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.input = QDoubleSpinBox(self.centralwidget)
        self.input.setObjectName(u"input")
        self.input.setGeometry(QRect(460, 230, 62, 23))
        self.input.setFrame(True)
        self.input.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.input.setMaximum(999999999.990000009536743)
        self.input.setValue(1.000000000000000)
        self.out = QDoubleSpinBox(self.centralwidget)
        self.out.setObjectName(u"out")
        self.out.setGeometry(QRect(590, 230, 62, 23))
        self.out.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.out.setMaximum(999999999.990000009536743)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(590, 210, 58, 14))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.currency_code = QLabel(self.centralwidget)
        self.currency_code.setObjectName(u"currency_code")
        self.currency_code.setGeometry(QRect(460, 210, 58, 14))
        self.currency_code.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(530, 230, 58, 14))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PLN", None))
        self.currency_code.setText(QCoreApplication.translate("MainWindow", u"USD", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"=", None))
    # retranslateUi

