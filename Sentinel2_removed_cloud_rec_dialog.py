# -*- coding: utf-8 -*-
"""
/***************************************************************************
 S2_vn_rectangleDialog
                                 A QGIS plugin
 Sentinel 2 removed cloud
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-07-11
        git sha              : $Format:%H$
        copyright            : (C) 2020 by GFD
        email                : hoa.lq@gfd.com.vn
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

from __future__ import absolute_import

from builtins import str
import os

from qgis.PyQt.QtWidgets import QDialog, QFileDialog, QMessageBox, QProgressBar
from qgis.PyQt import uic
from qgis.PyQt.QtCore import pyqtSlot, QThreadPool, Qt
from qgis.core import Qgis,QgsMessageLog,  QgsProject, QgsRasterLayer
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5 import QtCore
import ee
from ee_plugin import Map

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'Sentinel2_removed_cloud_rec_dialog_base.ui'))


class S2_vn_rectangleDialog(QDialog, FORM_CLASS):
    def __init__(self, iface, startX, startY, endX, endY, parent=None):
        """Constructor."""
        super(S2_vn_rectangleDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

        self.iface = iface

        self.setCoordinates(startX, startY, endX, endY)

        self.threadpool = QThreadPool()

        self.size = 0

        self.time1.setDate(QtCore.QDate.currentDate())
        self.time0.setDate(QtCore.QDate.currentDate().addDays(-15))
        #Type file name



    def setCoordinates(self, startX, startY, endX, endY):
        if startX < endX:
            minLong = startX
            maxLong = endX
        else:
            minLong = endX
            maxLong = startX

        if startY < endY:
            minLat = startY
            maxLat = endY
        else:
            minLat = endY
            maxLat = startY

        self.wEdit.setText(str(minLong))
        self.sEdit.setText(str(minLat))
        self.eEdit.setText(str(maxLong))
        self.nEdit.setText(str(maxLat))