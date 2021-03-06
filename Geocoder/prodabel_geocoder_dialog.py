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

"""
import os
"""

from PyQt4 import QtGui, QtCore
from qgis.core import QgsProject, QgsLayerTreeGroup, QgsVectorLayer
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
        QtCore.QObject.connect(self.comboBoxTipoConsulta, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")),
                               self.setParametersInput)
        QtCore.QObject.connect(self.lineEditCep, QtCore.SIGNAL(_fromUtf8("cursorPositionChanged(int,int)")),
                               self.statusPesquisarButton)
        QtCore.QObject.connect(self.lineEditNumero, QtCore.SIGNAL(_fromUtf8("cursorPositionChanged(int,int)")),
                               self.statusPesquisarButton)
        QtCore.QObject.connect(self.lineEditLogradouro, QtCore.SIGNAL(_fromUtf8("cursorPositionChanged(int,int)")),
                               self.statusPesquisarButton)
        QtCore.QObject.connect(self.lineEditBairro,  QtCore.SIGNAL(_fromUtf8("cursorPositionChanged(int,int)")),
                               self.statusPesquisarButton)
        QtCore.QObject.connect(self.lineEditIdEnderecoPbh,  QtCore.SIGNAL(_fromUtf8("cursorPositionChanged(int,int)")),
                               self.statusPesquisarButton)
        QtCore.QObject.connect(self.mostrarNoMapaButton, QtCore.SIGNAL(_fromUtf8("clicked()")),
                               self.addFeatureToWorkspace)
        self.grupo = QgsLayerTreeGroup()
        self.layer = QgsVectorLayer()

    def updateTextBrowserResultado(self):
        QtGui.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        geo = WsGeocoder()

        js = None

        try:

            # logradouro
            if self.comboBoxTipoConsulta.currentIndex() == 0:
                self.textBrowserResultado.setText(unicode(self.lineEditLogradouro.text()).encode('utf-8'))
                js = geo.pesqlograd(unicode(self.lineEditLogradouro.text()).encode('utf-8'))
            # logradouro e numero
            elif self.comboBoxTipoConsulta.currentIndex() == 1:
                js = geo.pesqlogradnum(unicode(self.lineEditLogradouro.text()).encode('utf-8'),
                                       unicode(self.lineEditNumero.text()).encode('utf-8'))
            # logradouro numero e bairro
            elif self.comboBoxTipoConsulta.currentIndex() == 2:
                pass
            # cep
            elif self.comboBoxTipoConsulta.currentIndex() == 3:
                js = geo.pesqcep(_translate("GeocoderDialogBase",self.lineEditCep.text(),None))
            # cep e numero
            elif self.comboBoxTipoConsulta.currentIndex() == 4:
                js = geo.pesqcepnum(_translate("GeocoderDialogBase",self.lineEditCep.text(),None),
                                    _translate("GeocoderDialogBase",self.lineEditNumero.text(),None))
            # bairro
            elif self.comboBoxTipoConsulta.currentIndex() == 5:
                pass
            # id_endereco_pbh
            elif self.comboBoxTipoConsulta.currentIndex() == 6:
                pass

            self.textBrowserResultado.setText(json.dumps(js, indent=2, ensure_ascii=False))
            self.textBrowserResultado.setDisabled(False)
            self.mostrarNoMapaButton.setDisabled(False)
            QtGui.QApplication.restoreOverrideCursor()

        except:
            QtGui.QApplication.restoreOverrideCursor()
            raise

    def loadComboBoxTipoConsulta(self):
        self.comboBoxTipoConsulta.clear()
        self.comboBoxTipoConsulta.insertItem(0, _translate("GeocoderDialogBase",'Logradouro',None))
        self.comboBoxTipoConsulta.insertItem(1, _translate("GeocoderDialogBase","Logradouro e Número",None))
        self.comboBoxTipoConsulta.insertItem(2, _translate("GeocoderDialogBase",'Logradouro, Número e Bairro',None))
        self.comboBoxTipoConsulta.insertItem(3, _translate("GeocoderDialogBase",'CEP', None))
        self.comboBoxTipoConsulta.insertItem(4, _translate("GeocoderDialogBase",'CEP e Número', None))
        self.comboBoxTipoConsulta.insertItem(5, _translate("GeocoderDialogBase",'Bairro', None))
        self.comboBoxTipoConsulta.insertItem(6, _translate("GeocoderDialogBase",'id_endereco_pbh', None))
        self.comboBoxTipoConsulta.setCurrentIndex(0)

    def setParametersInput(self):

        # logradouro
        if self.comboBoxTipoConsulta.currentIndex() == 0:
            self.lineEditBairro.setDisabled(True)
            self.lineEditCep.setDisabled(True)
            self.lineEditIdEnderecoPbh.setDisabled(True)
            self.lineEditLogradouro.setDisabled(False)
            self.lineEditNumero.setDisabled(True)
            self.lineEditNumero.setText(None)
            self.lineEditCep.setText(None)
            self.lineEditIdEnderecoPbh.setText(None)
            self.lineEditBairro.setText(None)
            self.textBrowserResultado.setText(None)
        # logradouro e numero
        elif self.comboBoxTipoConsulta.currentIndex() == 1:
            self.lineEditBairro.setDisabled(True)
            self.lineEditCep.setDisabled(True)
            self.lineEditIdEnderecoPbh.setDisabled(True)
            self.lineEditLogradouro.setDisabled(False)
            self.lineEditNumero.setDisabled(False)
            self.lineEditCep.setText(None)
            self.lineEditIdEnderecoPbh.setText(None)
            self.lineEditBairro.setText(None)
            self.textBrowserResultado.setText(None)
        # logradouro, numero e bairro
        elif self.comboBoxTipoConsulta.currentIndex() == 2:
            self.lineEditBairro.setDisabled(False)
            self.lineEditCep.setDisabled(True)
            self.lineEditIdEnderecoPbh.setDisabled(True)
            self.lineEditLogradouro.setDisabled(False)
            self.lineEditNumero.setDisabled(False)
            self.lineEditCep.setText(None)
            self.lineEditIdEnderecoPbh.setText(None)
            self.textBrowserResultado.setText(None)
        # cep
        elif self.comboBoxTipoConsulta.currentIndex() == 3:
            self.lineEditBairro.setDisabled(True)
            self.lineEditCep.setDisabled(False)
            self.lineEditIdEnderecoPbh.setDisabled(True)
            self.lineEditLogradouro.setDisabled(True)
            self.lineEditNumero.setDisabled(True)
            self.lineEditNumero.setText(None)
            self.lineEditLogradouro.setText(None)
            self.lineEditIdEnderecoPbh.setText(None)
            self.lineEditBairro.setText(None)
            self.textBrowserResultado.setText(None)
        # cep e numero
        elif self.comboBoxTipoConsulta.currentIndex() == 4:
            self.lineEditBairro.setDisabled(True)
            self.lineEditCep.setDisabled(False)
            self.lineEditIdEnderecoPbh.setDisabled(True)
            self.lineEditLogradouro.setDisabled(True)
            self.lineEditNumero.setDisabled(False)
            self.lineEditLogradouro.setText(None)
            self.lineEditIdEnderecoPbh.setText(None)
            self.lineEditBairro.setText(None)
            self.textBrowserResultado.setText(None)
        # bairro
        elif self.comboBoxTipoConsulta.currentIndex() == 5:
            self.lineEditBairro.setDisabled(False)
            self.lineEditCep.setDisabled(True)
            self.lineEditIdEnderecoPbh.setDisabled(True)
            self.lineEditLogradouro.setDisabled(True)
            self.lineEditNumero.setDisabled(True)
            self.lineEditNumero.setText(None)
            self.lineEditCep.setText(None)
            self.lineEditLogradouro.setText(None)
            self.lineEditIdEnderecoPbh.setText(None)
            self.textBrowserResultado.setText(None)
        # id_endereco_pbh
        elif self.comboBoxTipoConsulta.currentIndex() == 6:
            self.lineEditBairro.setDisabled(True)
            self.lineEditCep.setDisabled(True)
            self.lineEditIdEnderecoPbh.setDisabled(False)
            self.lineEditLogradouro.setDisabled(True)
            self.lineEditNumero.setDisabled(True)
            self.lineEditNumero.setText(None)
            self.lineEditCep.setText(None)
            self.lineEditLogradouro.setText(None)
            self.lineEditBairro.setText(None)
            self.textBrowserResultado.setText(None)

    def statusPesquisarButton(self):
        # logradouro
        if self.comboBoxTipoConsulta.currentIndex() == 0:
            if len(self.lineEditLogradouro.text()) > 0:
                self.pesquisarButton.setDisabled(False)
            else:
                self.pesquisarButton.setDisabled(True)
        # logradouro e numero
        elif self.comboBoxTipoConsulta.currentIndex() == 1:
            if len(self.lineEditLogradouro.text()) > 0 and len(self.lineEditNumero.text()) > 0:
                self.pesquisarButton.setDisabled(False)
            else:
                self.pesquisarButton.setDisabled(True)
        # logradouro, numero e bairro
        elif self.comboBoxTipoConsulta.currentIndex() == 2:
            if len(self.lineEditLogradouro.text()) > 0 and len(self.lineEditNumero.text()) > 0 and len(self.lineEditBairro.text()) > 0:
                self.pesquisarButton.setDisabled(False)
            else:
                self.pesquisarButton.setDisabled(True)
        # cep
        elif self.comboBoxTipoConsulta.currentIndex() == 3:
            if len(self.lineEditCep.text()) > 0:
                self.pesquisarButton.setDisabled(False)
            else:
                self.pesquisarButton.setDisabled(True)
        # cep e numero
        elif self.comboBoxTipoConsulta.currentIndex() == 4:
            if len(self.lineEditCep.text()) > 0 and len(self.lineEditNumero.text()) > 0:
                self.pesquisarButton.setDisabled(False)
            else:
                self.pesquisarButton.setDisabled(True)
        # bairro
        elif self.comboBoxTipoConsulta.currentIndex() == 5:
            if len(self.lineEditBairro.text()) > 0:
                self.pesquisarButton.setDisabled(False)
            else:
                self.pesquisarButton.setDisabled(True)
        # id_endereco_pbh
        elif self.comboBoxTipoConsulta.currentIndex() == 6:
            if len(self.lineEditIdEnderecoPbh.text()) > 0:
                self.pesquisarButton.setDisabled(False)
            else:
                self.pesquisarButton.setDisabled(True)

    def clearInputFields(self):
        self.lineEditNumero.setText(None)
        self.lineEditCep.setText(None)
        self.lineEditLogradouro.setText(None)
        self.lineEditIdEnderecoPbh.setText(None)
        self.lineEditBairro.setText(None)
        self.textBrowserResultado.setText(None)

    def addFeatureToWorkspace(self):
        # verificar grupo de layers
        root = QgsProject.instance().layerTreeRoot()
        criaGrupo = True
        criaLayer = True

        for child in root.children():
            if isinstance(child, QgsLayerTreeGroup):
                if child.name() == "Prodabel_Geocoder":
                    criaGrupo = False
                    self.grupo = child

                    for subChild in child.children():
                        if isinstance(child, QgsVectorLayer):
                            if child.name() == "enderecos_pesquisados":
                                criaLayer = False
                                self.layer = child

        if criaGrupo:
            self.grupo = root.addGroup('Prodabel_Geocoder')
            if criaLayer:
                self.layer = QgsVectorLayer("Point", "enderecos_pesquisados", "memory")
                self.grupo.addLayer(self.layer)









