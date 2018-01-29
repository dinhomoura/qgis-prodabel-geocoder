# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prodabel_geocoder_dialog_base.ui'
#
# Created: Mon Jan 29 00:54:13 2018
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
        GeocoderDialogBase.resize(400, 300)
        self.button_box = QtGui.QDialogButtonBox(GeocoderDialogBase)
        self.button_box.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))

        self.retranslateUi(GeocoderDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), GeocoderDialogBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), GeocoderDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(GeocoderDialogBase)

    def retranslateUi(self, GeocoderDialogBase):
        GeocoderDialogBase.setWindowTitle(_translate("GeocoderDialogBase", "Prodabel Geocoder", None))

