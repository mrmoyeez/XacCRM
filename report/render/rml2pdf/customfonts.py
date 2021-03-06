# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 P. Christeas, Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################

from reportlab import rl_config
import os

CustomTTFonts = [ ('Helvetica',"DejaVu Sans", "DejaVuSans.ttf", 'normal'),
        ('Helvetica',"DejaVu Sans Bold", "DejaVuSans-Bold.ttf", 'bold'),
        ('Helvetica',"DejaVu Sans Oblique", "DejaVuSans-Oblique.ttf", 'italic'),
        ('Helvetica',"DejaVu Sans BoldOblique", "DejaVuSans-BoldOblique.ttf", 'bolditalic'),
        ('Times',"Liberation Serif", "LiberationSerif-Regular.ttf", 'normal'),
        ('Times',"Liberation Serif Bold", "LiberationSerif-Bold.ttf", 'bold'),
        ('Times',"Liberation Serif Italic", "LiberationSerif-Italic.ttf", 'italic'),
        ('Times',"Liberation Serif BoldItalic", "LiberationSerif-BoldItalic.ttf", 'bolditalic'),
        ('Times-Roman',"Liberation Serif", "LiberationSerif-Regular.ttf", 'normal'),
        ('Times-Roman',"Liberation Serif Bold", "LiberationSerif-Bold.ttf", 'bold'),
        ('Times-Roman',"Liberation Serif Italic", "LiberationSerif-Italic.ttf", 'italic'),
        ('Times-Roman',"Liberation Serif BoldItalic", "LiberationSerif-BoldItalic.ttf", 'bolditalic'),
        ('ZapfDingbats',"DejaVu Serif", "DejaVuSerif.ttf", 'normal'),
        ('ZapfDingbats',"DejaVu Serif Bold", "DejaVuSerif-Bold.ttf", 'bold'),
        ('ZapfDingbats',"DejaVu Serif Italic", "DejaVuSerif-Italic.ttf", 'italic'),
        ('ZapfDingbats',"DejaVu Serif BoldItalic", "DejaVuSerif-BoldItalic.ttf", 'bolditalic'),
        ('Courier',"FreeMono", "FreeMono.ttf", 'normal'),
        ('Courier',"FreeMono Bold", "FreeMonoBold.ttf", 'bold'),
        ('Courier',"FreeMono Oblique", "FreeMonoOblique.ttf", 'italic'),
        ('Courier',"FreeMono BoldOblique", "FreeMonoBoldOblique.ttf", 'bolditalic'),]

def SearchFontPath(font_file):    
    for dirname in rl_config.TTFSearchPath:
        for root, dirs, files in os.walk(os.path.abspath(dirname)):
            for file_name in files:
                filename = os.path.join(root, file_name)
                extension = os.path.splitext(filename)[1]
                if extension.lower() in ['.ttf']:
                      if file_name==font_file:
                            return True
    return False

def SetCustomFonts(rmldoc):
    for name, font, fname, mode in CustomTTFonts:
        if SearchFontPath(fname):
            rmldoc.setTTFontMapping(name, font,filename, mode)
    return True



#eof
