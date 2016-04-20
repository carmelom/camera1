# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Wed Apr 20 19:29:58 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1016, 733)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/basic-ui/icons/111267-basic-ui/svg/eye-close-up.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.odWidget = QtGui.QWidget(self.centralwidget)
        self.odWidget.setObjectName(_fromUtf8("odWidget"))
        self.odLayout = QtGui.QVBoxLayout(self.odWidget)
        self.odLayout.setMargin(0)
        self.odLayout.setObjectName(_fromUtf8("odLayout"))
        self.verticalLayout.addWidget(self.odWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1016, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuPlot = QtGui.QMenu(self.menubar)
        self.menuPlot.setObjectName(_fromUtf8("menuPlot"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.framesDockWidget = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.framesDockWidget.sizePolicy().hasHeightForWidth())
        self.framesDockWidget.setSizePolicy(sizePolicy)
        self.framesDockWidget.setObjectName(_fromUtf8("framesDockWidget"))
        self.framesWidget = QtGui.QWidget()
        self.framesWidget.setObjectName(_fromUtf8("framesWidget"))
        self.framesLayout = QtGui.QVBoxLayout(self.framesWidget)
        self.framesLayout.setObjectName(_fromUtf8("framesLayout"))
        self.framesDockWidget.setWidget(self.framesWidget)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.framesDockWidget)
        self.actionHome = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/basic-ui/icons/111267-basic-ui/svg/home-button.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHome.setIcon(icon1)
        self.actionHome.setObjectName(_fromUtf8("actionHome"))
        self.actionRefresh = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/basic-ui/icons/111267-basic-ui/svg/refresh-arrow.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRefresh.setIcon(icon2)
        self.actionRefresh.setObjectName(_fromUtf8("actionRefresh"))
        self.actionInfo = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/basic-ui/icons/111267-basic-ui/svg/left-justification-button.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInfo.setIcon(icon3)
        self.actionInfo.setObjectName(_fromUtf8("actionInfo"))
        self.menuFile.addAction(self.actionHome)
        self.menuPlot.addAction(self.actionRefresh)
        self.menuHelp.addAction(self.actionInfo)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuPlot.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionHome)
        self.toolBar.addAction(self.actionRefresh)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ELENA", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuPlot.setTitle(_translate("MainWindow", "Plot", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.framesDockWidget.setWindowTitle(_translate("MainWindow", "Raw frames", None))
        self.actionHome.setText(_translate("MainWindow", "Home", None))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh", None))
        self.actionRefresh.setShortcut(_translate("MainWindow", "F5", None))
        self.actionInfo.setText(_translate("MainWindow", "Info", None))
        self.actionInfo.setShortcut(_translate("MainWindow", "F11", None))

import resources_rc
