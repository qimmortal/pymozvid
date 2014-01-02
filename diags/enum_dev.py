import win32api

winDev = win32api.EnumDisplayDevices(DevNum=3)

print winDev.DeviceName
