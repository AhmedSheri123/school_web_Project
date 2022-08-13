#!/usr/bin/env python
"""
import asyncio
import websockets
dataHex = b'\x00\x01\x6d\x27\x0a\xef\x92\xa0\x92\x51\xd4\xdf\x3b\x6f\xa7\x2c\xa5\x78\xbb\x04\x96\x3e\xf4\x15\xa0\x53\x2a\x11\x66\x31\xae\x86\xeb\xb1\xf2\x91\xcb\x06\xd8\xeb\xd6\x5b\x1f\xea\xac\xf1\x03\xfe\x9e\x2e\xa8\xcb\xf3\x8b\xc1\x60\x77\x8d\xfc\xbb\xb8\xe9\xa5\xb4\x49\xa6\xdd\x0c\x93\x58\xd7\xa7\x8f\x3d\x33\xb3\xb5\x4c\xa7\x96\x35\x01\xf3\xb0\x17\xb5\xe8\x8d\x02\xe4\x64\xab\x92\x67\x7d\x2e\x91\x15\x41\x46\xdd\x15\x06\x1f\x89\x46\x6d\xd2\x71\xce\xa4\x19\xc3\x4d\xfc\x40\xdf\xe9\x7e\xa5\xac\xb6\xd4\xdf\x14\x76\x1d\xd1\x41\x30\x75\x25\x2d\xe5\x9a\x36\x2a\x5b\x2f\xc4\x99\x71\x57\x5f\x49\xc4\xc8\x93\x31\x1e\xe0\x81\x93\x18\x35\x1f\xd7\xb5\xce\x1b\xb8\xa9\x5a\x39\xcd\xc3\xff\xa6\x1a\x86\xa5\x5f\xd6\x68\x55\xc3\x38\x5d\x76\x33\x08\x0b\x21\x05\x2e\xca\x01\x1e\xe6\x1b\x02\x75\x43\xe5\x92\x5e\x86\x25\x17\x71\x67\xbf\x69\xac\x26\x60\xbe\x48\xd6\x19\xc1\x41\x2d\xad\x36\x1d\x16\x12\x6c\x96\xa8\x91\x73\xdf\x9b\xc6\xb2\xac\xa9\x1e\x40\x1f\x8d\x01\xf9\x4a\xc2\xd0\x36\x40\xdf\x65\xc9\x7f\xb0\xd5\xfe\x60\x02\xa8\x09\x5f\x72\x60\xa2\x00\xd0\xda\xe7\xb6\xe7\xe1\x6f\x6f\xb1\x6c\xf3\x1f\x3d\x7c\xe6\x85\xcb\x58\x73\xf0\xc3\x25\x58\xae\x4b\x2f\xa8\x2d\x3f\x1c\x62\x6a\x4b\x58\x1e\xfb\x27\x60\xf0\xf5\x5d\x3a\xf0\x95\xa2\x42\x27\xe0\xf7\x1d\x61\xfc\x65\x34\x0f\x30\xfd\x55\x4d\x50\xbf\xe8\xc6\xc2\x9b\x6e\xc1\xfb\x61\x1c\xcc\x94\x3d\x2c\x44\x2f\x01\x8a\x22\x4c\x22\x0f\x33\x9c\x9a\xbb\x38\xaf\x52\x87\x61\x89\xbc\x70\x1a\xd4\xc7\xe0\x1d\x20\x01\x74\x91\x93\x4d\x33\x2d\xa1\xa9\x06\xfa\x01'

#dataHex = bytearray(dataHex)
async def hello():
    async with websockets.connect("wss://web.whatsapp.com/ws/chat?ED=CAwIAg") as websocket:
        await websocket.send(dataHex)
        print(await websocket.recv())

asyncio.run(hello())

"""

# wa_automation.py
"""import pywhatkit

pywhatkit.sendwhatmsg("+9630995487022",
            "hi",
            23,
            6,
            15,
            True,
            3)"""
            
"start chrome https://web.whatsapp.com/send?phone=+9630995487022&text=hi"   


import pyautogui, time, os, pytz, datetime, sqlite3
import pyperclip
try:
    im2 = pyautogui.screenshot('my_screenshot.png')
    xx, yy = pyautogui.locateCenterOnScreen('my_screenshot.png')
except:
    pass

while True:

        
    conn = sqlite3.connect('db.sqlite3')

    date_time_now = datetime.datetime.now(pytz.timezone('Asia/Baghdad'))
    openBrowserWaiting = 10
    msgSendingWaiting = 1.5

    url = "https://web.whatsapp.com"

    msg = ""


    def check_ping():
        hostname = "web.whatsapp.com"
        response = os.system("ping -n 1 " + hostname)
        # and then check the response...
        if response == 0:
            pingstatus = True
        else:
            pingstatus = False
        
        return pingstatus

        


    def clickCenter():
        pyautogui.click(xx, yy)


    conn = sqlite3.connect('db.sqlite3')

    cur = conn.cursor()

    PassData = '''SELECT id, username, passDate, GuardianNumber FROM accounts_passdata WHERE is_sended=False'''

    PassData_Definded = '''SELECT number FROM accounts_defindednumbers'''

    PassData_Definded = cur.execute(PassData_Definded).fetchall()

    PassData = cur.execute(PassData).fetchall()

    #numbers = ['+963997915593']
    knownNumbers = []

    for known in PassData_Definded:
        knownNumbers.extend(known)
    #print(str(knownNumbers) + "---------")


    def insertIntoDefindedNumbers(num):
        if num not in knownNumbers:
            insert_query = f"""INSERT INTO accounts_defindednumbers
                                (number) 
                                VALUES 
                                ('{num}')"""
            cur.execute(insert_query)
            conn.commit()


    browserIsOpened = False
    networkConnection = False
    passDataLoopIndex = 0
    for id, username, pass_date, num in PassData:
        #print(str(pass_date))
        if num:
            while not networkConnection:    
                if check_ping() == True:
                    networkConnection = True
                    break
                else:
                    #print("noo")
                    networkConnection = False
                    time.sleep(3)
            
            try:
                pass_date = datetime.datetime.strptime(pass_date, "%Y-%m-%d %H:%M:%S")
            except:
                pass_date = datetime.datetime.strptime(pass_date, "%Y-%m-%d %H:%M:%S.%f")
            #print(id, username, pass_date, num)
            
            if str(pass_date.time()) >= "08:00:00" and str(pass_date.time()) <= "11:00:00":
                msg = """تم دخول الطالب  {username} الى المدرسة {date}"""
            elif str(pass_date.time()) >= "11:00:00" and str(pass_date.time()) <= "16:00:00":
                msg = """تم خروج الطالب {username} من المدرسة {date}"""
            else:
                msg = """تم خروج الطالب {username} من المدرسة {date} """
            new_date = str(pass_date.date()) + " | " + pass_date.strftime("%H:%M:%S") 
            
            msg = msg.format(date=new_date, username=username)
            pyperclip.copy(msg)
            
            
            #print(num)
            if num not in knownNumbers:
                if not browserIsOpened:
                    os.system(f"start chrome {url}/send?phone={num}")
                    browserIsOpened = True
                    time.sleep(openBrowserWaiting)

                #clickCenter()

                pyautogui.hotkey("ctrl", "v")
                #pyautogui.write(msg)
                time.sleep(.2)
                pyautogui.press('enter')
                time.sleep(msgSendingWaiting)
                
                try:
                    if PassData[passDataLoopIndex+1][3] not in knownNumbers:
                        pyautogui.hotkey('ctrl', 'w')
                        browserIsOpened = False
                        time.sleep(2)
                except:
                    pyautogui.hotkey('ctrl', 'w')
                    browserIsOpened = False
            else:
                if not browserIsOpened:
                    os.system(f"start chrome {url}")
                    time.sleep(openBrowserWaiting)
                    browserIsOpened = True

                pyautogui.hotkey('ctrl', 'alt', '/')
                time.sleep(.2)
                pyautogui.write(num)
                time.sleep(.5)
                pyautogui.press('enter')
                time.sleep(.3)
                #clickCenter()
                time.sleep(.2)
                pyautogui.hotkey("ctrl", "v")
                #pyautogui.write(msg)
                time.sleep(.2)
                pyautogui.press("enter")
                time.sleep(msgSendingWaiting)
                try:
                    #print(PassData[passDataLoopIndex+1][3])
                    if PassData[passDataLoopIndex+1][3] not in knownNumbers:
                        pyautogui.hotkey('ctrl', 'w')
                        browserIsOpened = False
                        time.sleep(2)
                except:
                    pyautogui.hotkey('ctrl', 'w')
                    browserIsOpened = False
            update_passData = f''' UPDATE accounts_passdata
                    SET is_sended=True WHERE id = {id}'''
            cur.execute(update_passData)
            conn.commit()
            insertIntoDefindedNumbers(num)
            passDataLoopIndex += 1
    time.sleep(3)
