# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prodabel_geocoder_dialog_base.ui'
#
# Created: Fri Feb 02 01:39:04 2018
#      by: PyQt4 UI code generator 4.10.2
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

class Ui_GeocoderDialogBase(object):
    def setupUi(self, GeocoderDialogBase):
        GeocoderDialogBase.setObjectName(_fromUtf8("GeocoderDialogBase"))
        GeocoderDialogBase.resize(380, 327)
        self.button_box = QtGui.QDialogButtonBox(GeocoderDialogBase)
        self.button_box.setGeometry(QtCore.QRect(-70, 140, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.label = QtGui.QLabel(GeocoderDialogBase)
        self.label.setGeometry(QtCore.QRect(80, 20, 251, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEditCep = QtGui.QLineEdit(GeocoderDialogBase)
        self.lineEditCep.setGeometry(QtCore.QRect(70, 70, 113, 20))
        self.lineEditCep.setObjectName(_fromUtf8("lineEditCep"))
        self.lineEditNumero = QtGui.QLineEdit(GeocoderDialogBase)
        self.lineEditNumero.setGeometry(QtCore.QRect(70, 100, 113, 20))
        self.lineEditNumero.setObjectName(_fromUtf8("lineEditNumero"))
        self.label_2 = QtGui.QLabel(GeocoderDialogBase)
        self.label_2.setGeometry(QtCore.QRect(50, 70, 21, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(GeocoderDialogBase)
        self.label_3.setGeometry(QtCore.QRect(50, 100, 16, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.textBrowser = QtGui.QTextBrowser(GeocoderDialogBase)
        self.textBrowser.setGeometry(QtCore.QRect(70, 190, 241, 101))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        self.retranslateUi(GeocoderDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), GeocoderDialogBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), GeocoderDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(GeocoderDialogBase)

    def retranslateUi(self, GeocoderDialogBase):
        GeocoderDialogBase.setWindowTitle(_translate("GeocoderDialogBase", "Prodabel Geocoder", None))
        self.label.setText(_translate("GeocoderDialogBase", "Consulta ao serviço web geocoder.pbh.gov.br", None))
        self.label_2.setText(_translate("GeocoderDialogBase", "CEP", None))
        self.label_3.setText(_translate("GeocoderDialogBase", "Nº", None))

