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

pyPassGenVersion = '0.01alpha'

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

class Ui_pyPassGen(object):
	# generate the password using the given length and characters
	def generatePassword(self, length, seed, chars):
		random.seed = seed
		return '' . join(random.choice(chars) for i in range(length))
	
	def setStatus(self, str):
		self.lblStatus.setText(_translate('pyPassGen', str, None))
	
	def resetStatus(self):
		self.setStatus('Ready')
	
	# set the widgets to disabled
	def lockWidgets(self, unlock=True):
		self.chkMixedCase.setEnabled(unlock)
		self.chkNumbers.setEnabled(unlock)
		self.chkLetters.setEnabled(unlock)
		self.chkSpecial.setEnabled(unlock)
		self.chkSimilar.setEnabled(unlock)
		self.spnLength.setEnabled(unlock)
		self.spnQuantity.setEnabled(unlock)
		self.txtOutput.setEnabled(unlock)
		self.btnGenerate.setEnabled(unlock)
	
	# for toggling the letters
	def lettersChanged(self):
		self.chkMixedCase.setEnabled(self.chkLetters.isChecked())
	
	# generate the passwords
	def generate(self):
		
		# do some checks to make sure we have something to work with
		if not self.chkNumbers.isChecked() and not self.chkLetters.isChecked() and not self.chkSpecial.isChecked():
			QtGui.QMessageBox.critical(pyPassGen, 'pyPassGen', 'You have all of the types of characters disabled, silly!')
			return
		
		# prompt if they want REALLY long passwords
		if self.spnLength.value() > 32:
			response = QtGui.QMessageBox.question(pyPassGen,
							'Are you sure?', 'Are you sure you want to generate a <b>%d</b> character password?' % self.spnLength.value(),
							QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
			if response == QtGui.QMessageBox.No:
				self.lockWidgets(True)
				return
		
		# prompt if they want a LOT of passwords
		if self.spnQuantity.value() > 100:
			response = QtGui.QMessageBox.question(pyPassGen,
							'Are you sure?', 'Are you sure you want to generate <b>%d</b> passwords?' % self.spnQuantity.value(),
							QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
			if response == QtGui.QMessageBox.No:
				self.lockWidgets(True)
				return

		# lock the widgets so they aren't changed mid-run
		self.lockWidgets(False)				
			
		# generate the seed
		self.setStatus('Generating Seed')
		seed = (os.urandom(1024))
		
		# generate character string to use
		self.setStatus('Generating Character List')
		chars = ''
		
		# generate letters
		if self.chkLetters.isChecked() == True:
			# lowercase letters
			chars += string.ascii_lowercase
			# uppercase letters
			if self.chkMixedCase.isChecked() == True:
				chars += string.ascii_uppercase
		
		# add numbers
		if self.chkNumbers.isChecked() == True:
			chars += string.digits
		
		# add "special" characters
		if self.chkSpecial.isChecked() == True:
			chars += '!@#$%^&*?'
			
		# remove "similar" characters
		if self.chkSimilar.isChecked() == True:
			chars = chars.replace('i', '') # lowercase i
			chars = chars.replace('I', '') # uppercase i
			chars = chars.replace('l', '') # lowercase L
			chars = chars.replace('O', '') # uppercase o
			chars = chars.replace('0', '') # zero

		# open blank file
		txtFile = open(str(self.txtOutput.text()), 'w')
		if not txtFile:
			QtGui.QMessageBox.critical(pyPassGen, 'pyPassGen v%s' % pyPassGenVersion, 'Unable to open <b>%s</b> for writing.\n\nAborting.' % str(self.txtOutput.text()))
			self.lockWidgets(True)
			self.resetStatus()
			return
		
		# for loop to generate passwords
		for x in range(1, self.spnQuantity.value()):
			self.setStatus('Generating %d of %d' % (x, self.spnQuantity.value()))
			txtFile.write('%s\n' % self.generatePassword(self.spnLength.value(), seed, chars))
		
		# close text file and finish up
		txtFile.close()
		self.setStatus('Finished Generating %d Passwords' % self.spnQuantity.value())
		
		# query user to open the file
		response = QtGui.QMessageBox.question(pyPassGen,
						'pyPassGen v%s' % pyPassGenVersion, 'Finished generating <b>%d</b> password.\n\nWould you like to open the text file now?' % self.spnQuantity.value(),
						QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
		if response == QtGui.QMessageBox.Yes:
			os.system('start %s' % str(self.txtOutput.text()))
		
		# done!
		self.lockWidgets(True)
		self.resetStatus()

	def setupUi(self, pyPassGen):
		# main window
		pyPassGen.setObjectName(_fromUtf8('pyPassGen'))
		pyPassGen.resize(221, 220)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(pyPassGen.sizePolicy().hasHeightForWidth())
		pyPassGen.setSizePolicy(sizePolicy)
		pyPassGen.setMinimumSize(QtCore.QSize(221, 220))
		pyPassGen.setMaximumSize(QtCore.QSize(221, 220))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8('MS Shell Dlg 2'))
		font.setPointSize(9)
		pyPassGen.setFont(font)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8('password.ico')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		pyPassGen.setWindowIcon(icon)

		# central widget
		self.centralwidget = QtGui.QWidget(pyPassGen)
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
		self.spnLength.setProperty('value', 15)
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
		self.spnQuantity.setProperty('value', 10)
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
		
		# status label
		self.lblStatus = QtGui.QLabel(self.centralwidget)
		self.lblStatus.setGeometry(QtCore.QRect(10, 200, 201, 16))
		palette = QtGui.QPalette()
		brush = QtGui.QBrush(QtGui.QColor(0, 179, 0))
		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
		self.lblStatus.setPalette(palette)
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.lblStatus.setFont(font)
		self.lblStatus.setObjectName(_fromUtf8("lblStatus"))
		
		# set the central widget
		pyPassGen.setCentralWidget(self.centralwidget)

		# setup the default text and slots
		self.retranslateUi(pyPassGen)
		QtCore.QMetaObject.connectSlotsByName(pyPassGen)
		pyPassGen.connect(self.btnGenerate, QtCore.SIGNAL('clicked()'), self.generate)
		pyPassGen.connect(self.chkLetters, QtCore.SIGNAL('stateChanged(int)'), self.lettersChanged)

	def retranslateUi(self, pyPassGen):
		pyPassGen.setWindowTitle(_translate('pyPassGen', 'pyPassGen v%s' % pyPassGenVersion, None))
		self.chkMixedCase.setText(_translate('pyPassGen', 'Mixed Case Letters', None))
		self.chkNumbers.setText(_translate('pyPassGen', 'Digits', None))
		self.chkSpecial.setText(_translate('pyPassGen', 'Special Characters', None))
		self.chkLetters.setText(_translate('pyPassGen', 'Letters', None))
		self.chkSimilar.setText(_translate('pyPassGen', 'No Similar Characters', None))
		self.lblLength.setText(_translate('pyPassGen', 'Character Length:', None))
		self.lblQuantity.setText(_translate('pyPassGen', 'Quantity:', None))
		self.lblOutput.setText(_translate('pyPassGen', 'Output File:', None))
		self.txtOutput.setText(_translate('pyPassGen', 'generated.txt', None))
		self.btnGenerate.setText(_translate('pyPassGen', 'Generate!', None))
		self.lblStatus.setText(_translate('pyPassGen', 'Ready', None))


if __name__ == '__main__':
	import sys
	app = QtGui.QApplication(sys.argv)
	pyPassGen = QtGui.QMainWindow()
	ui = Ui_pyPassGen()
	ui.setupUi(pyPassGen)
	pyPassGen.show()
	sys.exit(app.exec_())