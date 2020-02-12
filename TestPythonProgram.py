import os
os.system("color 3") 
os.system("title League of Legends CLH Ver1.0")
import math
import getpass
import random
import time
import linecache
import codecs
import psutil
import threading
import ctypes



FileName_rand = str(random.randint(1,50000))
Computer_user = getpass.getuser()
FileName = "C:\\Users\\"+Computer_user+"\\AppData\\Local\\Temp\\LOLHelper-"+FileName_rand+".tmp"

def get_lang(text_token):
           if "--locale=zh_TW" in text_token:
             return str("繁體中文(台灣)")
           elif "--locale=en_US" in text_token:
             return str("英文")
           elif "--locale=zh_CN" in text_token:
             return str("中文(簡體)")
           elif "--locale=en_GB" in text_token:
             return "英文"
           elif "--locale=en_AU" in text_token:
             return "英文"
           elif "--locale=ja_JP" in text_token:
             return "日文"
           elif "--locale=ko_KR" in text_token:
             return "韓文"
           elif "--locale=en_GB" in text_token:
             return str("英文")
           else:
             return "未知"



def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                   return False
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return True;

def get_status(token_outtt):
     print('目前執行的是'+get_lang(token_outtt))
     print('LeagueClient is running!!')
     scan_lol(token_outtt)
     while checkIfProcessRunning('LeagueClient.exe')==False:    
                time.sleep(1)
     else:
        print('LeagueClient was closed')
        time.sleep(1)
        os.system("exit")

def show_messange( msg_name , msg_msg ):
    ctypes.windll.user32.MessageBoxW(0, msg_msg, msg_name, 0)

def scan_lol(token_outt): 
    os.system("wmic process where 'name like 'LeagueClient.exe'' get commandline > "+FileName+"3")
    get_file24 = codecs.open(FileName+"3",'r','utf-16')
    get_token24 = get_file24.read()
    token_step124= get_token24.replace("\r","")
    token_step224 = token_step124.replace("\n","")
    token_out24 = token_step224.replace("CommandLine","")
    get_file24.close()
    os.system("del "+FileName+"3")
    print('目前執行的是'+get_lang(token_out24))
    change_to  = input("更換為 1.中文(繁體) 2.中文(簡體) 3.韓文 4.日文 5.英文")
    while str.isdigit(change_to)==False and change_to <=5 and change_to >= 1 :

        change_to  = input("更換為 1.中文(繁體) 2.中文(簡體) 3.韓文 4.日文 5.英文")
    else:    
        if(change_to=="1"):
            if"--locale=zh_CN" in token_outt:       
             Command = token_outt.replace("--locale=zh_CN","--locale=zh_TW").lstrip()
            elif"--locale=ko_KR" in token_outt:       
             Command = token_outt.replace("--locale=ko_KR","--locale=zh_TW").lstrip()
            elif"--locale=ja_JP" in token_outt:
             Command = token_outt.replace("--locale=ja_JP","--locale=zh_TW").lstrip()
            elif"--locale=en_US" in token_outt:
             Command = token_outt.replace("--locale=en_US","--locale=zh_TW").lstrip()
            else:
             Command = token_outt.replace("--locale=zh_TW","--locale=zh_TW").lstrip()
            os.system("taskkill /f /im LeagueClient.exe")
            time.sleep(1)
            os.system("start /b cmd /c "+Command)
            time.sleep(1)
        elif(change_to=="2"):
            if"--locale=zh_TW" in token_outt:       
             Command = token_outt.replace("--locale=zh_TW","--locale=zh_CN").lstrip()
            elif"--locale=ko_KR" in token_outt:       
             Command = token_outt.replace("--locale=ko_KR","--locale=zh_CN").lstrip()
            elif"--locale=ja_JP" in token_outt:
             Command = token_outt.replace("--locale=ja_JP","--locale=zh_CN").lstrip()
            elif"--locale=en_US" in token_outt:
             Command = token_outt.replace("--locale=en_US","--locale=zh_CN").lstrip()
            else:
             Command = token_outt.replace("--locale=zh_CN","--locale=zh_CN").lstrip()
            os.system("taskkill /f /im LeagueClient.exe")
            time.sleep(1)
            os.system("start /b cmd /c "+Command)
            time.sleep(1)
        elif(change_to=="3"):
             if"--locale=zh_TW" in token_outt:       
              Command = token_outt.replace("--locale=zh_TW","--locale=ko_KR").lstrip()
             elif"--locale=zh_CN" in token_outt:       
              Command = token_outt.replace("--locale=zh_CN","--locale=ko_KR").lstrip()
             elif"--locale=ja_JP" in token_outt:
              Command = token_outt.replace("--locale=ja_JP","--locale=ko_KR").lstrip()
             elif"--locale=en_US" in token_outt:
              Command = token_outt.replace("--locale=en_US","--locale=ko_KR").lstrip()
             else:
              Command = token_outt.replace("--locale=ko_KR","--locale=ko_KR").lstrip()
             os.system("taskkill /f /im LeagueClient.exe")
             time.sleep(1)
             os.system("start /b cmd /c "+Command)
             time.sleep(1)
        elif(change_to=="4"):
              if"--locale=zh_TW" in token_outt:       
               Command = token_outt.replace("--locale=zh_TW","--locale=ja_JP").lstrip()
              elif"--locale=zh_CN" in token_outt:       
               Command = token_outt.replace("--locale=zh_CN","--locale=ja_JP").lstrip()
              elif"--locale=ja_JP" in token_outt:
               Command = token_outt.replace("--locale=ja_JP","--locale=ja_JP").lstrip()
              elif"--locale=en_US" in token_outt:
               Command = token_outt.replace("--locale=en_US","--locale=ja_JP").lstrip()
              else:
               Command = token_outt.replace("--locale=ko_KR","--locale=ja_JP").lstrip()
              os.system("taskkill /f /im LeagueClient.exe")
              time.sleep(1)
              os.system("start /b cmd /c "+Command)
              time.sleep(1)
        elif(change_to=="5"):
              if"--locale=zh_TW" in token_outt:       
               Command = token_outt.replace("--locale=zh_TW","--locale=en_US").lstrip()
              elif"--locale=zh_CN" in token_outt:       
               Command = token_outt.replace("--locale=zh_CN","--locale=en_US").lstrip()
              elif"--locale=ja_JP" in token_outt:
               Command = token_outt.replace("--locale=ja_JP","--locale=en_US").lstrip()
              elif"--locale=en_US" in token_outt:
               Command = token_outt.replace("--locale=en_US","--locale=en_US").lstrip()
              else:
               Command = token_outt.replace("--locale=ko_KR","--locale=en_US").lstrip()
              os.system("taskkill /f /im LeagueClient.exe")
              time.sleep(1)
              os.system("start /b cmd /c "+Command)
              time.sleep(1)
        else:
            print("錯誤")
            scan_lol(token_outt)
    
showrunning = 0 

while checkIfProcessRunning('LeagueClient.exe'):
    if (showrunning==0):
        showrunning = 1
        print('等待[LeagueClient]執行中...')
    else:
        None
    time.sleep(1)
else:
    os.system("wmic process where 'name like 'LeagueClient.exe'' get commandline > "+FileName+"2")
    get_file2 = codecs.open(FileName+"2",'r','utf-16')
    get_token2 = get_file2.read()
    token_step12= get_token2.replace("\r","")
    token_step22 = token_step12.replace("\n","")
    token_out2 = token_step22.replace("CommandLine","")
    get_file2.close()
    os.system("del "+FileName+"2")

    if len(token_out2) >40:
           t2=[]
           t2 = threading.Thread(target=get_status(token_out2))
           t2.start()
           t2.join()
    elif len(token_out2) ==15:
        msgbox=[]
        msgbox = threading.Thread(target=show_messange("信息","權限不足!請使用管理員模式開啟!"))
        msgbox.start()
    else:
         Lang_text="未啟動"
    
     
        

