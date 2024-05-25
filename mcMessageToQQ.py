# encoding:utf-8

import win32gui
import win32con
import win32clipboard as w
import time
import os



#创建配置文件
def createConfigFile():
    groupName = input("QQ群窗口名:")
    serverLatestLog = input("服务器latest.log路径(用正斜杠表示路径):")
    waitTime = input("检查服务器消息的间隔(设置过高可能会漏掉部分消息):")

    with open("config.txt",'a',encoding='utf-8') as f:

        f.write(groupName + "\n" + serverLatestLog + "\n" + waitTime )
        checkConfigFile()
#检查是否存在配置文件
def checkConfigFile():
    if os.path.exists("config.txt"):
        print("1")

    else:
        print("0")
        createConfigFile()
checkConfigFile()
configFile = open('config.txt', 'r', encoding='utf-8')
configFileName = 'config.txt'
with open(configFileName, 'r', encoding='utf-8',errors='ignore') as f:  
    configlatestLines = f.readlines()
    groupName = configlatestLines[0] 
    serverLatestLog = configlatestLines[1]
    waitTime = configlatestLines[2]

latestMsg = ""

while True:
    def sendMsg(msg):
        name = groupName.replace("\n","") 
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
        w.CloseClipboard()

        handle = win32gui.FindWindow(None, name)
        win32gui.SendMessage(handle, win32con.WM_PASTE,0,0)
        win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        return
    
    log_file = open(serverLatestLog.replace("\n",""), 'r')
    latestLogName = serverLatestLog.replace("\n","")
    
    with open(latestLogName, 'r', encoding='utf-8') as f:  
        latestLines = f.readlines()  
    
        latestLastLine = latestLines[-1]  
   
        print('文件' + latestLogName + '最新消息：' + latestLastLine)
    if "joined the game" in latestLastLine and latestLastLine != latestMsg or "left the game" in latestLastLine and latestLastLine != latestMsg or "<" in latestLastLine and latestLastLine != latestMsg:
        sendMsg(latestLastLine)
        print("发送消息:" + latestLastLine)
        latestMsg = latestLastLine
    else:
        print("未获取到有效信息")
    
    time.sleep(float(waitTime.replace("\n","")))