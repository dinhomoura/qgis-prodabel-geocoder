# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Geocoder
                                 A QGIS plugin
 bla bla bla
                             -------------------
        begin                : 2018-01-29
        copyright            : (C) 2018 by José Ricardo Ferreira Moura
        email                : dinhomoura@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Geocoder class from file Geocoder.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .prodabel_geocoder import Geocoder
    return Geocoder(iface)
