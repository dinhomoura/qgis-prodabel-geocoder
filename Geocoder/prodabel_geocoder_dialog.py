# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeocoderDialog
                                 A QGIS plugin
 bla bla bla
                             -------------------
        begin                : 2018-01-29
        git sha              : $Format:%H$
        copyright            : (C) 2018 by José Ricardo Ferreira Moura
        email                : dinhomoura@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import QtGui, QtCore
from prodabel_geocoder_dialog_base import Ui_GeocoderDialogBase

from ws_geocoder import WsGeocoder
import json

"""
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'prodabel_geocoder_dialog_base.ui'))
"""

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


class GeocoderDialog(QtGui.QDialog, Ui_GeocoderDialogBase):
    def __init__(self, parent=None):
        """Constructor."""
        super(GeocoderDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        QtCore.QObject.connect(self.pesquisarButton, QtCore.SIGNAL(_fromUtf8("clicked()")),
                               self.updateTextBrowserResultado)

    def updateTextBrowserResultado(self):
        QtGui.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        geo = WsGeocoder()
        js = geo.pesqcepnum(self.lineEditCep.text(), self.lineEditNumero.text())
        self.textBrowserResultado.setText(json.dumps(js['endereco'], indent=2, ensure_ascii=False))
        QtGui.QApplication.restoreOverrideCursor()

    def loadComboBoxTipoConsulta(self):
        self.comboBoxTipoConsulta.clear()
        self.comboBoxTipoConsulta.insertItem(0, '')
        self.comboBoxTipoConsulta.insertItem(1, 'Logradouro')
        self.comboBoxTipoConsulta.insertItem(2, _fromUtf8("Logradouro e Número"))
        self.comboBoxTipoConsulta.insertItem(3, _fromUtf8('Logradouro, Número e Bairro'))
        self.comboBoxTipoConsulta.insertItem(4, 'CEP')
        self.comboBoxTipoConsulta.insertItem(5, _fromUtf8('CEP e Número'))
        self.comboBoxTipoConsulta.insertItem(6, 'Bairro')
        self.comboBoxTipoConsulta.insertItem(7, 'id_endereco_pbh')
