# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prodabel_geocoder_dialog_base.ui'
#
# Created: Fri Feb 23 16:15:01 2018
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
        GeocoderDialogBase.resize(380, 578)
        self.button_box = QtGui.QDialogButtonBox(GeocoderDialogBase)
        self.button_box.setGeometry(QtCore.QRect(30, 540, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.labelTitle = QtGui.QLabel(GeocoderDialogBase)
        self.labelTitle.setGeometry(QtCore.QRect(10, 20, 361, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelTitle.setFont(font)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName(_fromUtf8("labelTitle"))
        self.textBrowserResultado = QtGui.QTextBrowser(GeocoderDialogBase)
        self.textBrowserResultado.setEnabled(False)
        self.textBrowserResultado.setGeometry(QtCore.QRect(10, 370, 361, 101))
        self.textBrowserResultado.setObjectName(_fromUtf8("textBrowserResultado"))
        self.pesquisarButton = QtGui.QPushButton(GeocoderDialogBase)
        self.pesquisarButton.setEnabled(False)
        self.pesquisarButton.setGeometry(QtCore.QRect(150, 300, 75, 23))
        self.pesquisarButton.setObjectName(_fromUtf8("pesquisarButton"))
        self.labelResultado = QtGui.QLabel(GeocoderDialogBase)
        self.labelResultado.setGeometry(QtCore.QRect(10, 350, 61, 16))
        self.labelResultado.setObjectName(_fromUtf8("labelResultado"))
        self.comboBoxTipoConsulta = QtGui.QComboBox(GeocoderDialogBase)
        self.comboBoxTipoConsulta.setGeometry(QtCore.QRect(120, 70, 231, 22))
        self.comboBoxTipoConsulta.setAutoFillBackground(False)
        self.comboBoxTipoConsulta.setObjectName(_fromUtf8("comboBoxTipoConsulta"))
        self.line = QtGui.QFrame(GeocoderDialogBase)
        self.line.setGeometry(QtCore.QRect(10, 50, 361, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.labelConsulta = QtGui.QLabel(GeocoderDialogBase)
        self.labelConsulta.setGeometry(QtCore.QRect(10, 70, 111, 21))
        self.labelConsulta.setObjectName(_fromUtf8("labelConsulta"))
        self.line_2 = QtGui.QFrame(GeocoderDialogBase)
        self.line_2.setGeometry(QtCore.QRect(10, 100, 361, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_6 = QtGui.QLabel(GeocoderDialogBase)
        self.label_6.setGeometry(QtCore.QRect(10, 120, 61, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.frame = QtGui.QFrame(GeocoderDialogBase)
        self.frame.setGeometry(QtCore.QRect(10, 120, 361, 171))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.labelLogradouro = QtGui.QLabel(self.frame)
        self.labelLogradouro.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.labelLogradouro.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelLogradouro.setObjectName(_fromUtf8("labelLogradouro"))
        self.labelCep = QtGui.QLabel(self.frame)
        self.labelCep.setGeometry(QtCore.QRect(10, 50, 91, 16))
        self.labelCep.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelCep.setObjectName(_fromUtf8("labelCep"))
        self.labelNumero = QtGui.QLabel(self.frame)
        self.labelNumero.setGeometry(QtCore.QRect(10, 80, 91, 16))
        self.labelNumero.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelNumero.setObjectName(_fromUtf8("labelNumero"))
        self.labelBairro = QtGui.QLabel(self.frame)
        self.labelBairro.setGeometry(QtCore.QRect(10, 110, 91, 16))
        self.labelBairro.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelBairro.setObjectName(_fromUtf8("labelBairro"))
        self.labelIdEnderecoPbh = QtGui.QLabel(self.frame)
        self.labelIdEnderecoPbh.setGeometry(QtCore.QRect(10, 140, 91, 16))
        self.labelIdEnderecoPbh.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelIdEnderecoPbh.setObjectName(_fromUtf8("labelIdEnderecoPbh"))
        self.lineEditLogradouro = QtGui.QLineEdit(self.frame)
        self.lineEditLogradouro.setEnabled(False)
        self.lineEditLogradouro.setGeometry(QtCore.QRect(120, 20, 211, 20))
        self.lineEditLogradouro.setObjectName(_fromUtf8("lineEditLogradouro"))
        self.lineEditCep = QtGui.QLineEdit(self.frame)
        self.lineEditCep.setEnabled(False)
        self.lineEditCep.setGeometry(QtCore.QRect(120, 50, 211, 20))
        self.lineEditCep.setObjectName(_fromUtf8("lineEditCep"))
        self.lineEditNumero = QtGui.QLineEdit(self.frame)
        self.lineEditNumero.setEnabled(False)
        self.lineEditNumero.setGeometry(QtCore.QRect(120, 80, 211, 20))
        self.lineEditNumero.setObjectName(_fromUtf8("lineEditNumero"))
        self.lineEditBairro = QtGui.QLineEdit(self.frame)
        self.lineEditBairro.setEnabled(False)
        self.lineEditBairro.setGeometry(QtCore.QRect(120, 110, 211, 20))
        self.lineEditBairro.setObjectName(_fromUtf8("lineEditBairro"))
        self.lineEditIdEnderecoPbh = QtGui.QLineEdit(self.frame)
        self.lineEditIdEnderecoPbh.setEnabled(False)
        self.lineEditIdEnderecoPbh.setGeometry(QtCore.QRect(120, 140, 211, 20))
        self.lineEditIdEnderecoPbh.setObjectName(_fromUtf8("lineEditIdEnderecoPbh"))
        self.line_3 = QtGui.QFrame(GeocoderDialogBase)
        self.line_3.setGeometry(QtCore.QRect(10, 330, 361, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.mostrarNoMapaButton = QtGui.QPushButton(GeocoderDialogBase)
        self.mostrarNoMapaButton.setEnabled(False)
        self.mostrarNoMapaButton.setGeometr
        y(QtCore.QRect(140, 490, 101, 23))
        self.mostrarNoMapaButton.setObjectName(_fromUtf8("mostrarNoMapaButton"))
        self.line_4 = QtGui.QFrame(GeocoderDialogBase)
        self.line_4.setGeometry(QtCore.QRect(10, 520, 361, 16))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))

        self.retranslateUi(GeocoderDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), GeocoderDialogBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), GeocoderDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(GeocoderDialogBase)

    def retranslateUi(self, GeocoderDialogBase):
        GeocoderDialogBase.setWindowTitle(_translate("GeocoderDialogBase", "Prodabel Geocoder", None))
        self.labelTitle.setText(_translate("GeocoderDialogBase", "Geolocalização dos endereços de Belo Horizonte", None))
        self.pesquisarButton.setText(_translate("GeocoderDialogBase", "Pesquisar", None))
        self.labelResultado.setText(_translate("GeocoderDialogBase", "Resultado:", None))
        self.labelConsulta.setText(_translate("GeocoderDialogBase", "Selecione a consulta:", None))
        self.label_6.setText(_translate("GeocoderDialogBase", "Parâmetros:", None))
        self.labelLogradouro.setText(_translate("GeocoderDialogBase", "Logradouro", None))
        self.labelCep.setText(_translate("GeocoderDialogBase", "CEP", None))
        self.labelNumero.setText(_translate("GeocoderDialogBase", "Número", None))
        self.labelBairro.setText(_translate("GeocoderDialogBase", "Bairro", None))
        self.labelIdEnderecoPbh.setText(_translate("GeocoderDialogBase", "id_endereco_pbh", None))
        self.mostrarNoMapaButton.setText(_translate("GeocoderDialogBase", "Mostrar no mapa", None))

