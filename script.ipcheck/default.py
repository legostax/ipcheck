import os
import sys
import urllib
import xbmc
import xbmcaddon
import xbmcgui


addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
url         = "http://checkip.amazonaws.com/"

ip = urllib.urlopen(url).read()[:-1]

line1 = "External IP: "
line1 += ip

xbmcgui.Dialog().ok(addonname, line1)
