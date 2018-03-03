# -*- coding: utf-8 -*-
# !/usr/bin/env python
import wx
import cv, cv2
import wx.lib.filebrowsebutton

class MainWindow(wx.Panel):
    def __init__(self, parent,capture):
        wx.Panel.__init__(self, parent)
        mainSizer = wx.BoxSizer(wx.VERTICAL)

        self.inputBox = wx.TextCtrl(self)
        mainSizer.Add(self.inputBox, 0, wx.ALL, 5)


        # video
        # 视频的灰色背景
        videoWarper = wx.StaticBox(self, label="Video",size=(1280,580))
        videoBoxSizer = wx.StaticBoxSizer(videoWarper, wx.VERTICAL)
        # 视频显示的尺寸！！！！改动视频显示的尺寸和所有尺寸要同步
        videoFrame = wx.Panel(self, -1,size=(1280,580))
        cap = ShowCapture(videoFrame, capture)
        videoBoxSizer.Add(videoFrame,0)
        mainSizer.Add(videoBoxSizer,0)

        parent.Centre()
        self.Show()
        self.SetSizerAndFit(mainSizer)


class ShowCapture(wx.Panel):
    def __init__(self, parent, capture, fps=24):
        wx.Panel.__init__(self, parent, wx.ID_ANY, (0,0), (1280,580))


        self.capture = capture
        ret, frame = self.capture.read()

        height, width = frame.shape[:2]

        parent.SetSize((width, height))

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        self.bmp = wx.BitmapFromBuffer(width, height, frame)

        self.timer = wx.Timer(self)
        self.timer.Start(1000./fps)

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_TIMER, self.NextFrame)


    def OnPaint(self, evt):
        dc = wx.BufferedPaintDC(self)
        dc.DrawBitmap(self.bmp, 0, 0)

    def NextFrame(self, event):
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.bmp.CopyFromBuffer(frame)
            self.Refresh()



# class catch(path):
if(12<>3):
    print(3)

capture = cv2.VideoCapture('/Users/zhoubowen/Desktop/my_programmeV2.0/2.MP4')

app = wx.App(False)
frame = wx.Frame(None,-1,'HGA Count',size=(1280, 580))
panel = MainWindow(frame,capture)
frame.Show()
app.MainLoop()