from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import win32api
import win32gui
import win32con
from urllib import request
import os

# set your temp path to save background image here
bgImgPath = "C:\\Users\\xiezibuyongbi\\Desktop\\temp\\today_background.bmp"

# reserver the downloaded picture until next launch
if os._exists(bgImgPath):
    os.remove(bgImgPath)

chromeOptions = Options()
chromeOptions.add_argument('headless')
browser = webdriver.Chrome(chrome_options=chromeOptions)
browser.get("https://cn.bing.com/")
bgImgLabel = browser.find_element_by_id("bgImgProgLoad")
bgImgUrl = "https://cn.bing.com/" + \
    bgImgLabel.get_attribute("data-ultra-definition-src")
with request.urlopen(bgImgUrl) as response:
    img = open(bgImgPath, "wb")
    img.write(response.read())
    img.close()
browser.quit()

reg_key = win32api.RegOpenKeyEx(
    win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
win32api.RegSetValueEx(reg_key, "TileWallpaper", 0, win32con.REG_SZ, "0")
win32gui.SystemParametersInfo(
    win32con.SPI_SETDESKWALLPAPER, bgImgPath, win32con.SPIF_SENDWININICHANGE)
