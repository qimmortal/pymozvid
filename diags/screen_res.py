import win32api
#import wx
#from wx import *
from ctypes import *
import os


dm = win32api.EnumDisplaySettings(None, -1)

#print int(dm.PelsWidth), int(dm.PelsHeight)
print dm.DeviceName, dm.DriverData, dm.DisplayOrientation, dm.DisplayFrequency

#display =  wx.Display(0)
#print display.GetName()

user32 = windll.user32

print user32 
#dm1 = user32.EnumDisplaySettingsA(None, -1)

screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

print screensize

#print int(dm1.PelsWidth), int(dm1.PelsHeight)


