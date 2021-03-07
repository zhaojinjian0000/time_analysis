import os
import win32api, win32gui, win32con
import argparse
def setWallPaper(pic):
    # open register
    regKey = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(regKey,"WallpaperStyle", 0, win32con.REG_SZ, "2")
    win32api.RegSetValueEx(regKey, "TileWallpaper", 0, win32con.REG_SZ, "0")
    # refresh screen
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,pic, win32con.SPIF_SENDWININICHANGE)
"""
   #mac #osascript -e 'tell application "System Events" to set picture of every desktop to "%s"'%pic_name)
"""
if __name__=="__main__":
    parser = argparse.ArgumentParser(description='A wallpaper change tool for IDP learning.')
    parser.add_argument('--wallpaper', type=str,default=r"wallpaper_new.png", help='wallpaper picture path')
    args = parser.parse_args()
    setWallPaper(os.path.join(os.getcwd(),args.wallpaper))
    print('already change wallpaper')