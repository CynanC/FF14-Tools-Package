import win32gui, win32ui, win32con, win32api
import numpy as np
import time

def window_capture(filename):
  hwnd = 0 # 窗口的编号，0号表示当前活跃窗口
  # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
  hwndDC = win32gui.GetWindowDC(hwnd)
  # 根据窗口的DC获取mfcDC
  mfcDC = win32ui.CreateDCFromHandle(hwndDC)
  # mfcDC创建可兼容的DC
  saveDC = mfcDC.CreateCompatibleDC()
  # 创建bigmap准备保存图片
  saveBitMap = win32ui.CreateBitmap()
  # 获取监控器信息
  MoniterDev = win32api.EnumDisplayMonitors(None, None)
  w = MoniterDev[0][2][2]
  h = MoniterDev[0][2][3]
  # print w,h　　　#图片大小
  # 为bitmap开辟空间
  saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
  # 高度saveDC，将截图保存到saveBitmap中
  saveDC.SelectObject(saveBitMap)
  # 截取从左上角（0，0）长宽为（w，h）的图片
  saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
  saveBitMap.SaveBitmapFile(saveDC, filename)


def get_screen_arry(size):
    width=size[2]-size[0]
    height=size[3]-size[1]

    hwnd = win32gui.GetDesktopWindow()
    hdc = win32gui.GetWindowDC(hwnd)
    dc = win32ui.CreateDCFromHandle(hdc)
    memdc = dc.CreateCompatibleDC()
    bitmap = win32ui.CreateBitmap()
    bitmap.CreateCompatibleBitmap(dc, width, height)
    oldbmp = memdc.SelectObject(bitmap)
    memdc.BitBlt((0,0), (width,height), dc, (size[0],size[1]), win32con.SRCCOPY)
    bits = bitmap.GetBitmapBits(False)
    memdc.SelectObject(oldbmp)
    win32gui.DeleteObject(bitmap.GetHandle())
    memdc.DeleteDC()
    win32gui.ReleaseDC(hwnd, hdc)


    array=np.zeros((width,height)).tolist() 
    for y in range(height):
        for x in range(width):
            p = (y * width + x) * 4
            blu=bits[p+0]&255
            grn=bits[p+1]&255
            red=bits[p+2]&255
            array[x][y]=[red,grn,blu]

    return array

if __name__=="__main__":
  window_capture('test5.jpg')