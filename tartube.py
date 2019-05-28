#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 A S Lewis
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.


"""Tartube main file."""


# Import Gtk modules
#   ...


# Import other modul6es
import sys


# Import our modules
from lib import mainapp


# 'Global' variables
__packagename__ = 'tartube'
__version__ = '0.1.007'
__date__ = '28 May 2019'
__copyright__ = 'Copyright \xc2\xa9 2019 A S Lewis'
__license__ = """
Copyright \xc2\xa9 2019 A S Lewis.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""
__author_list__ = [
    'A S Lewis',
]
__description__ = 'A front-end GUI for youtube-dl,\n' \
+ 'partly based on youtube-dl-gui\n' \
+ 'and written in Python 3 / Gtk 3'
__website__ = 'http://tartube.sourceforge.io'
__app_id__ = 'io.sourceforge.tartube'


# Start Tartube
app = mainapp.TartubeApp()
app.run(sys.argv)