#!/usr/bin/env python
'''
	pyPassGen v0.01alpha
	By: Adam Koch <crackpot.mytouch@gmail.com>
	http://github.com/adamjkoch/pyPassGen
'''

'''
	pyPassGen: A simple secure password generator written in Python.
	Copyright (C) 2014  Adam Koch

	This program is free software; you can redistribute it and/or
	modify it under the terms of the GNU General Public License
	as published by the Free Software Foundation; either version 2
	of the License, or (at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program; if not, write to the Free Software
	Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
'''
import os, random, string
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
	# generate the password using the given length and characters
	def genpwd(length, chars):
		random.seed = (os.urandom(1024))
		return '' . join(random.choice(chars) for i in range(length))

	def setupUi(self, frmMain):
		# main window
		frmMain.setObjectName(_fromUtf8('frmMain'))
		frmMain.resize(221, 220)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(frmMain.sizePolicy().hasHeightForWidth())
		frmMain.setSizePolicy(sizePolicy)
		frmMain.setMinimumSize(QtCore.QSize(221, 220))
		frmMain.setMaximumSize(QtCore.QSize(221, 220))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8('MS Shell Dlg 2'))
		font.setPointSize(9)
		frmMain.setFont(font)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8('password.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		frmMain.setWindowIcon(icon)

		# central widget
		self.centralwidget = QtGui.QWidget(frmMain)
		self.centralwidget.setObjectName(_fromUtf8('centralwidget'))

		# mixed case checkbox
		self.chkMixedCase = QtGui.QCheckBox(self.centralwidget)
		self.chkMixedCase.setGeometry(QtCore.QRect(90, 90, 131, 17))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.chkMixedCase.setFont(font)
		self.chkMixedCase.setChecked(True)
		self.chkMixedCase.setObjectName(_fromUtf8('chkMixedCase'))

		# numbers checkbox
		self.chkNumbers = QtGui.QCheckBox(self.centralwidget)
		self.chkNumbers.setGeometry(QtCore.QRect(10, 90, 101, 17))
		self.chkNumbers.setChecked(True)
		self.chkNumbers.setObjectName(_fromUtf8('chkNumbers'))

		# letters checkbox
		self.chkLetters = QtGui.QCheckBox(self.centralwidget)
		self.chkLetters.setGeometry(QtCore.QRect(10, 70, 121, 17))
		self.chkLetters.setChecked(True)
		self.chkLetters.setObjectName(_fromUtf8('chkLetters'))

		# special characters checkbox
		self.chkSpecial = QtGui.QCheckBox(self.centralwidget)
		self.chkSpecial.setGeometry(QtCore.QRect(90, 70, 121, 17))
		self.chkSpecial.setChecked(True)
		self.chkSpecial.setObjectName(_fromUtf8('chkSpecial'))

		# similar characters checkbox
		self.chkSimilar = QtGui.QCheckBox(self.centralwidget)
		self.chkSimilar.setGeometry(QtCore.QRect(10, 110, 141, 17))
		self.chkSimilar.setChecked(True)
		self.chkSimilar.setObjectName(_fromUtf8('chkSimilar'))

		# password length label
		self.lblLength = QtGui.QLabel(self.centralwidget)
		self.lblLength.setGeometry(QtCore.QRect(10, 10, 111, 16))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.lblLength.setFont(font)
		self.lblLength.setObjectName(_fromUtf8('lblLength'))

		# label length spinbox
		self.spnLength = QtGui.QSpinBox(self.centralwidget)
		self.spnLength.setGeometry(QtCore.QRect(130, 10, 42, 22))
		self.spnLength.setMinimum(1)
		self.spnLength.setMaximum(128)
		self.spnLength.setProperty('value', 12)
		self.spnLength.setObjectName(_fromUtf8('spnLength'))

		# quantity label
		self.lblQuantity = QtGui.QLabel(self.centralwidget)
		self.lblQuantity.setGeometry(QtCore.QRect(60, 40, 61, 16))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.lblQuantity.setFont(font)
		self.lblQuantity.setObjectName(_fromUtf8('lblQuantity'))

		# quantity spinbox
		self.spnQuantity = QtGui.QSpinBox(self.centralwidget)
		self.spnQuantity.setGeometry(QtCore.QRect(130, 40, 42, 22))
		self.spnQuantity.setMinimum(1)
		self.spnQuantity.setMaximum(1024)
		self.spnQuantity.setObjectName(_fromUtf8('spnQuantity'))

		# output file label
		self.lblOutput = QtGui.QLabel(self.centralwidget)
		self.lblOutput.setGeometry(QtCore.QRect(10, 140, 71, 16))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.lblOutput.setFont(font)
		self.lblOutput.setObjectName(_fromUtf8('lblOutput'))

		# output file line edit
		self.txtOutput = QtGui.QLineEdit(self.centralwidget)
		self.txtOutput.setGeometry(QtCore.QRect(90, 140, 121, 20))
		self.txtOutput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.txtOutput.setObjectName(_fromUtf8('txtOutput'))

		# generate push button
		self.btnGenerate = QtGui.QPushButton(self.centralwidget)
		self.btnGenerate.setGeometry(QtCore.QRect(10, 170, 201, 23))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.btnGenerate.setFont(font)
		self.btnGenerate.setObjectName(_fromUtf8('btnGenerate'))

		# set the central widget
		frmMain.setCentralWidget(self.centralwidget)

		# statusbar
		self.statusbar = QtGui.QStatusBar(frmMain)
		self.statusbar.setSizeGripEnabled(False)
		self.statusbar.setObjectName(_fromUtf8('statusbar'))
		frmMain.setStatusBar(self.statusbar)

		# setup the default text and slots
		self.retranslateUi(frmMain)
		QtCore.QMetaObject.connectSlotsByName(frmMain)

	def retranslateUi(self, frmMain):
		frmMain.setWindowTitle(_translate('frmMain', 'pyPassGen v%s by Adam Koch', None))
		self.chkMixedCase.setText(_translate('frmMain', 'Mixed Case Letters', None))
		self.chkNumbers.setText(_translate('frmMain', 'Numbers', None))
		self.chkSpecial.setText(_translate('frmMain', 'Special Characters', None))
		self.chkLetters.setText(_translate('frmMain', 'Letters', None))
		self.chkSimilar.setText(_translate('frmMain', 'No Similar Characters', None))
		self.lblLength.setText(_translate('frmMain', 'Character Length:', None))
		self.lblQuantity.setText(_translate('frmMain', 'Quantity:', None))
		self.lblOutput.setText(_translate('frmMain', 'Output File:', None))
		self.txtOutput.setText(_translate('frmMain', 'generated.txt', None))
		self.btnGenerate.setText(_translate('frmMain', 'Generate!', None))


if __name__ == '__main__':
	import sys
	app = QtGui.QApplication(sys.argv)
	frmMain = QtGui.QMainWindow()
	ui = Ui_frmMain()
	ui.setupUi(frmMain)
	frmMain.show()
	sys.exit(app.exec_())

