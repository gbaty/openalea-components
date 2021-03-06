# -*- coding: utf-8 -*-
# -*- python -*-
#
#       Copyright 2015 INRIA - CIRAD - INRA
#
#       File author(s): Guillaume Baty <guillaume.baty@inria.fr>
#
#       File contributor(s):
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
###############################################################################


class StackViewer(object):
    name = 'StackViewer'
    label = 'Image Stack Viewer'
    implement = 'IApplet'
    __plugin__ = True

    def __call__(self):
        from openalea.image.gui.oalab.applet import ImageStackViewer
        return ImageStackViewer
