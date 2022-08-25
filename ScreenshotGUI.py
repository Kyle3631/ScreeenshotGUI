import os
from tkinter import *
import tkinter
import pyautogui
import time

window = Tk()


window.title('ScreenshotGUI')

# window.geometry("100x100+1758+940")
window.geometry("6x47-115-43")


window.attributes("-topmost", True)


count = 0


def screenshot():
    global count
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save('./'+time.strftime("%Y%m%d,%H_%M_%S",
                      time.localtime())+' {'+str(count)+'}.jpg')
    button.config(text="截圖"+str(count))
    count = count + 1


def getfile():
    os.startfile(os.path.abspath(os.getcwd()))


button = Button(text="截圖", font=("Arial", 13, "bold"), padx=1,
                pady=1, bg="blue", fg="light green", command=screenshot)
# button.pack(side=tkinter.LEFT)
button.grid(row=0, column=1)


button2 = Button(text="open", font=("Arial", 7), padx=1,
                 pady=1, bg="pink", fg="black", command=getfile)
button2.grid(row=0, column=3)

window.mainloop()


''' import win32gui
    import win32ui
    import win32con
    w = 1920  # set this
    h = 1080  # set this
    bmpfilenamename = 'D://mI//'+time.strftime("%Y%m%d,%H_%M_%S",
                                               time.localtime())+' {'+str(count)+'}.jpg'  # set this

    hwnd = win32gui.FindWindow(None, 'Microsoft Edge')
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (w, h), dcObj, (0, 0), win32con.SRCCOPY)
    dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)

    # Free Resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())'''
