# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mw55c.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QLabel { font-size: 42px}")
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1281, 751))
        self.tabWidget.setContentsMargins(10, 10, 10, 10)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 30, 1029, 491))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setLineWidth(10)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.formFrame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.formFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.formFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.formFrame.setLineWidth(10)
        self.formFrame.setObjectName("formFrame")
        self.formLayout = QtWidgets.QFormLayout(self.formFrame)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.boardIDLabel = QtWidgets.QLabel(self.formFrame)
        self.boardIDLabel.setStyleSheet("")
        self.boardIDLabel.setObjectName("boardIDLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.boardIDLabel)
        self.boardIDLineEdit = QtWidgets.QLineEdit(self.formFrame)
        font = QtGui.QFont()
        font.setFamily("Nimbus Mono L")
        font.setPointSize(42)
        self.boardIDLineEdit.setFont(font)
        self.boardIDLineEdit.setStyleSheet("")
        self.boardIDLineEdit.setFrame(True)
        self.boardIDLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.boardIDLineEdit.setClearButtonEnabled(True)
        self.boardIDLineEdit.setObjectName("boardIDLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.boardIDLineEdit)
        self.horizontalLayout_3.addWidget(self.formFrame)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Scan Board QR Code"))
        self.boardIDLabel.setText(_translate("MainWindow", "Board ID"))
        self.boardIDLineEdit.setText(_translate("MainWindow", "A0001"))
        self.boardIDLineEdit.setPlaceholderText(_translate("MainWindow", "A0001"))
        self.label_3.setText(_translate("MainWindow", "Scan your RFID Key Tag "))
        self.label.setText(_translate("MainWindow", "Enjoy"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "AutoMagic"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "PowerUser"))
