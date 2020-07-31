# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(686, 645)
        Form.setStyleSheet(u"background-color:#eddfdf ;")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 40, 411, 41))
        font = QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet(u"background-color: #fff;")
        self.lineEdit.setReadOnly(False)
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(20, 100, 411, 41))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(u"background-color: #fff;")
        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(20, 160, 411, 41))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet(u"background-color: #fff;")
        self.lineEdit_4 = QLineEdit(Form)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(20, 220, 651, 41))
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet(u"background-color: #fff;")
        self.dateEdit = QDateEdit(Form)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(490, 40, 181, 41))
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet(u"background-color: #fff;")
        self.dateEdit_2 = QDateEdit(Form)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setGeometry(QRect(20, 280, 181, 41))
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setStyleSheet(u"background-color: #fff;")
        self.dateEdit_3 = QDateEdit(Form)
        self.dateEdit_3.setObjectName(u"dateEdit_3")
        self.dateEdit_3.setGeometry(QRect(20, 460, 181, 41))
        self.dateEdit_3.setFont(font)
        self.dateEdit_3.setStyleSheet(u"background-color: #fff;")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(460, 570, 211, 61))
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"background-color:#d6d2d2;\n"
"\n"
"border: 1px solid #c4c2c2;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:#e0dede;\n"
"\n"
"border: 1px solid #cccaca;\n"
"}")
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(250, 460, 91, 41))
        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 340, 581, 41))
        self.comboBox.setFont(font)
        self.comboBox.setContextMenuPolicy(Qt.NoContextMenu)
        self.comboBox.setStyleSheet(u"background-color: #fff;")
        self.comboBox.setEditable(False)
        self.add_pattern_edit = QLineEdit(Form)
        self.add_pattern_edit.setObjectName(u"add_pattern_edit")
        self.add_pattern_edit.setGeometry(QRect(20, 400, 581, 41))
        self.add_pattern_edit.setFont(font)
        self.add_pattern_edit.setStyleSheet(u"background-color: #fff;")
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(610, 400, 61, 41))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"background-color:#d6d2d2;\n"
"\n"
"border: 1px solid #c4c2c2;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:#e0dede;\n"
"\n"
"border: 1px solid #cccaca;\n"
"}")
        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(30, 570, 181, 31))
        self.checkBox.setFont(font)
        self.checkBox_2 = QCheckBox(Form)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(30, 610, 181, 21))
        self.checkBox_2.setFont(font)
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(250, 280, 91, 41))
        self.get_folder = QPushButton(Form)
        self.get_folder.setObjectName(u"get_folder")
        self.get_folder.setGeometry(QRect(600, 520, 71, 31))
        self.get_folder.setFont(font)
        self.get_folder.setStyleSheet(u"QPushButton {\n"
"background-color:#d6d2d2;\n"
"\n"
"border: 1px solid #c4c2c2;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:#e0dede;\n"
"\n"
"border: 1px solid #cccaca;\n"
"}")
        self.folder = QLabel(Form)
        self.folder.setObjectName(u"folder")
        self.folder.setGeometry(QRect(20, 520, 571, 31))
        self.folder.setFont(font)
        self.folder.setStyleSheet(u"background-color: #fff;")
        self.deleteButton = QPushButton(Form)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setGeometry(QRect(610, 340, 61, 41))
        self.deleteButton.setFont(font)
        self.deleteButton.setStyleSheet(u"QPushButton {\n"
"background-color:#d6d2d2;\n"
"\n"
"border: 1px solid #c4c2c2;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:#e0dede;\n"
"\n"
"border: 1px solid #cccaca;\n"
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"FastDocx", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u0424\u0430\u043c\u0456\u043b\u0456\u044f", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"\u0406\u043c'\u044f", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"\u041f\u043e-\u0431\u0430\u0442\u044c\u043a\u043e\u0432\u0456", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Form", u"\u041c\u0456\u0441\u0446\u0435 \u0440\u0435\u0454\u0441\u0442\u0440\u0430\u0446\u0456\u0457", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041f\u0456\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u0438", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u0414\u0456\u0439\u0441\u043d\u0435 \u0434\u043e", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0434\u0430\u0442\u0438", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"\u041f\u0441\u0438\u0445\u0456\u0430\u0442\u0440\u0438\u0447\u043d\u0438\u0439 \u043e\u0433\u043b\u044f\u0434", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0440\u043a\u043e\u043b\u043e\u0433\u0456\u0447\u043d\u0438\u0439 \u043e\u0433\u043b\u044f\u0434", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u043e\u0433\u043b\u044f\u0434\u0443", None))
        self.get_folder.setText(QCoreApplication.translate("Form", u"...", None))
        self.folder.setText("")
        self.deleteButton.setText(QCoreApplication.translate("Form", u"\u0412\u0438\u0434\u0430\u043b\u0438\u0442\u0438", None))
    # retranslateUi
