#!/usr/bin/python
###########################################################################
#
#          FILE:  service.infocollector
#
#        AUTHOR:  Tobias D. Oestreicher
#
#       LICENSE:  GPLv3 <http://www.gnu.org/licenses/gpl.txt>
#       VERSION:  0.0.1
#       CREATED:  07.02.2018
#
###########################################################################
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, see <http://www.gnu.org/licenses/>.
#
###########################################################################
#     CHANGELOG:  (07.02.2018) TDOe - First Publishing
###########################################################################

import os,re,xbmc,xbmcgui,xbmcaddon,time

__addon__ = xbmcaddon.Addon()
__addonID__ = __addon__.getAddonInfo('id')
__addonname__ = __addon__.getAddonInfo('name')
__version__ = __addon__.getAddonInfo('version')
__path__ = __addon__.getAddonInfo('path')
__LS__ = __addon__.getLocalizedString
__icon__ = xbmc.translatePath(os.path.join(__path__, 'icon.png'))

OSD = xbmcgui.Dialog()

# Helpers #

def notifyOSD(header, message, icon=xbmcgui.NOTIFICATION_INFO, disp=4000, enabled=True):
    if enabled:
        OSD.notification(header.encode('utf-8'), message.encode('utf-8'), icon, disp)

def writeLog(message, level=xbmc.LOGNOTICE):
        xbmc.log('[%s %s]: %s' % (__addonID__, __version__,  message.encode('utf-8')), level)

# End Helpers #

class MyMonitor(xbmc.Monitor):
    def __init__(self, *args, **kwargs ):
        xbmc.Monitor.__init__(self)


class Starter():
    def start(self):
        monitor = MyMonitor()
        writeLog('Starting %s V.%s' % (__addonname__, __version__))
        #notifyOSD('Starting INFO Collector','Service is now active', __icon__)
        while not monitor.abortRequested():
            if monitor.waitForAbort(120):
                break
            writeLog('Updateing InfoCollector List (Service)', level=xbmc.LOGNOTICE)
	    xbmc.executebuiltin('XBMC.RunScript(service.infocollector,"?methode=refresh_container")')


if __name__ == '__main__':
    starter = Starter()
    starter.start()
    del starter
