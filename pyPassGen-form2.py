# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyPassGen.ui'
#
# Created: Mon Apr 28 16:44:34 2014
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_frmMain(object):
    def setupUi(self, frmMain):
        frmMain.setObjectName(_fromUtf8("frmMain"))
        frmMain.resize(221, 220)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(frmMain.sizePolicy().hasHeightForWidth())
        frmMain.setSizePolicy(sizePolicy)
        frmMain.setMinimumSize(QtCore.QSize(221, 220))
        frmMain.setMaximumSize(QtCore.QSize(221, 220))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(9)
        frmMain.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("password.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmMain.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(frmMain)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.chkMixedCase = QtGui.QCheckBox(self.centralwidget)
        self.chkMixedCase.setGeometry(QtCore.QRect(90, 90, 131, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.chkMixedCase.setFont(font)
        self.chkMixedCase.setChecked(True)
        self.chkMixedCase.setObjectName(_fromUtf8("chkMixedCase"))
        self.chkNumbers = QtGui.QCheckBox(self.centralwidget)
        self.chkNumbers.setGeometry(QtCore.QRect(10, 90, 101, 17))
        self.chkNumbers.setChecked(True)
        self.chkNumbers.setObjectName(_fromUtf8("chkNumbers"))
        self.chkSpecial = QtGui.QCheckBox(self.centralwidget)
        self.chkSpecial.setGeometry(QtCore.QRect(90, 70, 121, 17))
        self.chkSpecial.setChecked(True)
        self.chkSpecial.setObjectName(_fromUtf8("chkSpecial"))
        self.chkLetters = QtGui.QCheckBox(self.centralwidget)
        self.chkLetters.setGeometry(QtCore.QRect(10, 70, 121, 17))
        self.chkLetters.setChecked(True)
        self.chkLetters.setObjectName(_fromUtf8("chkLetters"))
        self.chkSimilar = QtGui.QCheckBox(self.centralwidget)
        self.chkSimilar.setGeometry(QtCore.QRect(10, 110, 141, 17))
        self.chkSimilar.setChecked(True)
        self.chkSimilar.setObjectName(_fromUtf8("chkSimilar"))
        self.lblLength = QtGui.QLabel(self.centralwidget)
        self.lblLength.setGeometry(QtCore.QRect(10, 10, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblLength.setFont(font)
        self.lblLength.setObjectName(_fromUtf8("lblLength"))
        self.spinBox = QtGui.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(130, 10, 42, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(1024)
        self.spinBox.setProperty("value", 12)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 40, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.spinBox_2 = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(130, 40, 42, 22))
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(64)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.lblOutput = QtGui.QLabel(self.centralwidget)
        self.lblOutput.setGeometry(QtCore.QRect(10, 140, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblOutput.setFont(font)
        self.lblOutput.setObjectName(_fromUtf8("lblOutput"))
        self.txtOutput = QtGui.QLineEdit(self.centralwidget)
        self.txtOutput.setGeometry(QtCore.QRect(90, 140, 121, 20))
        self.txtOutput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtOutput.setObjectName(_fromUtf8("txtOutput"))
        self.btnGenerate = QtGui.QPushButton(self.centralwidget)
        self.btnGenerate.setGeometry(QtCore.QRect(10, 170, 201, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnGenerate.setFont(font)
        self.btnGenerate.setObjectName(_fromUtf8("btnGenerate"))
        frmMain.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(frmMain)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        frmMain.setStatusBar(self.statusbar)

        self.retranslateUi(frmMain)
        QtCore.QMetaObject.connectSlotsByName(frmMain)

    def retranslateUi(self, frmMain):
        frmMain.setWindowTitle(_translate("frmMain", "pyPassGen v%s by Adam Koch", None))
        self.chkMixedCase.setText(_translate("frmMain", "Mixed Case Letters", None))
        self.chkNumbers.setText(_translate("frmMain", "Numbers", None))
        self.chkSpecial.setText(_translate("frmMain", "Special Characters", None))
        self.chkLetters.setText(_translate("frmMain", "Letters", None))
        self.chkSimilar.setText(_translate("frmMain", "No Similar Characters", None))
        self.lblLength.setText(_translate("frmMain", "Character Length:", None))
        self.label.setText(_translate("frmMain", "Quantity:", None))
        self.lblOutput.setText(_translate("frmMain", "Output File:", None))
        self.txtOutput.setText(_translate("frmMain", "generated.txt", None))
        self.btnGenerate.setText(_translate("frmMain", "Generate!", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    frmMain = QtGui.QMainWindow()
    ui = Ui_frmMain()
    ui.setupUi(frmMain)
    frmMain.show()
    sys.exit(app.exec_())

