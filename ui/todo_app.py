# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'todo_app.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_TODO(object):
    def setupUi(self, TODO):
        if not TODO.objectName():
            TODO.setObjectName(u"TODO")
        TODO.resize(800, 600)
        font = QFont()
        font.setBold(True)
        TODO.setFont(font)
        self.centralwidget = QWidget(TODO)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(70, 120, 251, 141))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.listWidget = QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setSelectionMode(QAbstractItemView.MultiSelection)

        self.verticalLayout.addWidget(self.listWidget)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(70, 20, 160, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(310, 29, 160, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(70, 329, 160, 31))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.horizontalLayoutWidget_4 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(310, 329, 160, 31))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)

        self.horizontalLayout_4.addWidget(self.pushButton_3)

        TODO.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(TODO)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        self.menuTODO = QMenu(self.menubar)
        self.menuTODO.setObjectName(u"menuTODO")
        TODO.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(TODO)
        self.statusbar.setObjectName(u"statusbar")
        TODO.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuTODO.menuAction())

        self.retranslateUi(TODO)

        QMetaObject.connectSlotsByName(TODO)
    # setupUi

    def retranslateUi(self, TODO):
        TODO.setWindowTitle(QCoreApplication.translate("TODO", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("TODO", u"Lista de Tareas", None))
        self.lineEdit.setText(QCoreApplication.translate("TODO", u"Indicar tarea", None))
        self.pushButton.setText(QCoreApplication.translate("TODO", u"Agregar tarea", None))
        self.pushButton_2.setText(QCoreApplication.translate("TODO", u"Completada", None))
        self.pushButton_3.setText(QCoreApplication.translate("TODO", u"Eliminar", None))
        self.menuTODO.setTitle(QCoreApplication.translate("TODO", u"TODO", None))
    # retranslateUi

