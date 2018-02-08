#!/usr/bin/python

import os
import sys
import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin
import json
import time
import urllib

__addon__ = xbmcaddon.Addon()
__addonID__ = __addon__.getAddonInfo('id')
__addonDir__            = __addon__.getAddonInfo("path")

__addonname__ = __addon__.getAddonInfo('name')
__version__ = __addon__.getAddonInfo('version')
__path__ = __addon__.getAddonInfo('path')
__LS__ = __addon__.getLocalizedString
__icon__ = xbmc.translatePath(os.path.join(__path__, 'icon.png'))
__addonUserDataFolder__ = xbmc.translatePath("special://profile/addon_data/"+__addonID__).decode('utf-8')
WINDOW                  = xbmcgui.Window( 10000 )




def parameters_string_to_dict(parameters):
    paramDict = {}
    if parameters:
        paramPairs = parameters[1:].split("&")
        for paramsPair in paramPairs:
            paramSplits = paramsPair.split('=')
            if (len(paramSplits)) == 2:
                paramDict[paramSplits[0]] = paramSplits[1]
    return paramDict


################################################
# Logging Function
################################################
def writeLog(message, level=xbmc.LOGNOTICE):
        try:
            xbmc.log('[%s %s]: %s' % ( __addonID__,__version__,message.encode('utf-8')), level)
        except Exception:
            xbmc.log('[%s %s]: Fatal: Message could not displayed' % (__addonID__,__version__), xbmc.LOGERROR)


################################################
# 
################################################
def item_create(pic,itemvar):
  url = '-'
  li = xbmcgui.ListItem(str(itemvar))
  li.setIconImage(pic)
  return li


################################################
#                   M A I N
################################################
if len(sys.argv)>=3:
    addon_handle = int(sys.argv[1])
    params = parameters_string_to_dict(sys.argv[2])
    methode = urllib.unquote_plus(params.get('methode', ''))
    updater = urllib.unquote_plus(params.get('updater', ''))
elif len(sys.argv)>1:
    params = parameters_string_to_dict(sys.argv[1])
    methode = urllib.unquote_plus(params.get('methode', ''))
    updater = urllib.unquote_plus(params.get('updater', ''))
else:
    methode = None




if methode=='get_container':
  writeLog('ReOpen JSON File', level=xbmc.LOGDEBUG)
  GetFile = '%s/infovars.json' % (__addonUserDataFolder__) 
  try:
      with open(GetFile, 'r') as toread:
              ConfigReads=toread.read().rstrip('\n')
  except:
      writeLog('Could not open configfile infoarea.json', level=xbmc.LOGNOTICE)
  
  allreads = json.loads(str(ConfigReads))
  
  
  Entries=allreads['entries']
  

  url='-'
  for Infovar in Entries:
      Var=Infovar['infovar']
      VarProperty=WINDOW.getProperty(Var)

      # issetpic -> if INFO-Variable has value
      if 'issetpic' in Infovar:
        writeLog('Checkmethode: issetpic', level=xbmc.LOGDEBUG)
        try:
          if VarProperty != '':
            writeLog('Activating Item for %s' % (Var), level=xbmc.LOGDEBUG)
            li=item_create(Infovar['issetpic'],Infovar['infovar'])
            xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
          else:
            writeLog('NOT activating Item for %s' % (Var), level=xbmc.LOGDEBUG)
        except:
          pass

      # isunsetpic -> if INFO-Variable has NO value
      if 'isunsetpic' in Infovar:
        writeLog('Checkmethode: isunsetpic', level=xbmc.LOGDEBUG)
        try:
          if VarProperty == '':
            writeLog('Activating Item for %s' % (Var), level=xbmc.LOGDEBUG)
            li=item_create(Infovar['isunsetpic'],Infovar['infovar'])
            xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
          else:
            writeLog('NOT activating Item for %s' % (Var), level=xbmc.LOGDEBUG)
        except:
          pass

      # gepic -> if INFO-Variable is greater or equal than comparative value (int)
      if 'gepic' in Infovar:
        writeLog('Checkmethode: gepic Compare: %s >= %s' % (VarProperty,Infovar['comparative']), level=xbmc.LOGDEBUG)
        try:
          if int(VarProperty) >= int(Infovar['comparative']):
            writeLog('Activating Item for %s' % (Var), level=xbmc.LOGDEBUG)
            li=item_create(Infovar['gepic'],Infovar['infovar'])
            xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
          else:
            writeLog('NOT activating Item for %s' % (Var), level=xbmc.LOGDEBUG)
        except:
          writeLog('Variable not proper set - NOT activating Item for %s' % (Var), level=xbmc.LOGDEBUG)
          pass

      # gpic -> if INFO-Variable is greater than comparative value (int)
      if 'gpic' in Infovar:
        writeLog('Checkmethode: gpic Compare: %s > %s' % (VarProperty,Infovar['comparative']), level=xbmc.LOGDEBUG)
        try:
          if int(VarProperty) > int(Infovar['comparative']):
            writeLog('Activating Item for %s' % (Var), level=xbmc.LOGDEBUG)
            li=item_create(Infovar['gpic'],Infovar['infovar'])
            xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
          else:
            writeLog('NOT activating Item for %s' % (Var), level=xbmc.LOGDEBUG)
        except:
          writeLog('Variable not proper set - NOT activating Item for %s' % (Var), level=xbmc.LOGDEBUG)
          pass

      # lepic -> if INFO-Variable is smaller or equal than comparative value (int)
      if 'lepic' in Infovar:
        writeLog('Checkmethode: lepic Compare: %s <= %s' % (VarProperty,Infovar['comparative']), level=xbmc.LOGDEBUG)
        try:
          if int(VarProperty) <= int(Infovar['comparative']):
            writeLog('Activating Item for %s' % (Var), level=xbmc.LOGDEBUG)
            li=item_create(Infovar['lepic'],Infovar['infovar'])
            xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
          else:
            writeLog('NOT activating Item for %s' % (Var), level=xbmc.LOGDEBUG)
        except:
          writeLog('Variable not proper set - NOT activating Item for %s' % (Var), level=xbmc.LOGDEBUG)
          pass

      # lpic -> if INFO-Variable is smaller than comparative value (int)
      if 'lpic' in Infovar:
        writeLog('Checkmethode: lpic Compare: %s < %s' % (VarProperty,Infovar['comparative']), level=xbmc.LOGDEBUG)
        try:
          if int(VarProperty) < int(Infovar['comparative']):
            writeLog('Activating Item for %s' % (Var), level=xbmc.LOGDEBUG)
            li=item_create(Infovar['lpic'],Infovar['infovar'])
            xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
          else:
            writeLog('NOT activating Item for %s' % (Var), level=xbmc.LOGDEBUG)
        except:
          writeLog('Variable not proper set - NOT activating for Item %s' % (Var), level=xbmc.LOGDEBUG)
          pass

      # ispic -> if INFO-Variable is comparative value 
      if 'ispic' in Infovar:
        writeLog('Checkmethode: ispic Compare: %s == %s' % (VarProperty,Infovar['comparative']), level=xbmc.LOGDEBUG)
        try:
          if WINDOW.getProperty(Var) == Infovar['comparative']:
            writeLog('Activating Item for %s' % (Var), level=xbmc.LOGDEBUG)
            li=item_create(Infovar['ispic'],Infovar['infovar'])
            xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
          else:
            writeLog('NOT activating Item for %s' % (Var), level=xbmc.LOGDEBUG)
        except:
          writeLog('Variable not proper set - NOT activating Item for %s' % (Var), level=xbmc.LOGDEBUG)
          pass
  
  xbmcplugin.endOfDirectory(addon_handle)

  writeLog('Check-Run finished' , level=xbmc.LOGDEBUG)


elif methode=='refresh_container':
  writeLog('Updateing InfoCollector List', level=xbmc.LOGDEBUG)
  WINDOW = xbmcgui.Window(10000)

  WINDOW.setProperty('InfoCollector.Updater',str(time.time()))

