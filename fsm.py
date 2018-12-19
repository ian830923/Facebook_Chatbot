from transitions.extensions import GraphMachine

from utils import send_text_message ,send_image_url
import requests
from selenium import webdriver
from bs4 import BeautifulSoup

from bottle import route, run, request, abort, static_file
from urllib.request import urlopen
import re


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}


url1 ='https://histock.tw/stock/public.aspx'
resp1=requests.get(url1, headers=headers)
soup1=BeautifulSoup(resp1.text, features='lxml')
catch_large=soup1.find('table',{"class":re.compile('gv')})
matrix=[[],[],[],[],[],[],[],[],[],[]]


print("---------------name-----------------")
stock_name=catch_large.find_all('a')

for h in range(10):
    #print(stock_name[h].get_text())
    #stock_name[h].get_text().strip().split()
    print(stock_name[h].get_text().strip().split()[0])
    num=stock_name[h].get_text().strip().split()[0]
    name=stock_name[h].get_text().strip().split()[1]

    matrix[h].append(num)
    matrix[h].append(name)



print("----------------date----------------")
stock_date=catch_large.find_all('td',{"style":re.compile('width:100px')})

for h in range(10):
    #print(stock_date[h].get_text().strip())
    matrix[h].append(stock_date[h].get_text().strip())

print("----------------reward----------------")
stock_reward=catch_large.find_all('td',{"style":re.compile('font-weight:bold;width:67px')})
count=0
data_index=0
for h in range(40):
    matrix[data_index].append(stock_reward[h].get_text().strip())
    count+=1
    if count==4:
        count=0
        data_index+=1
print(matrix)

print("--------------answer---------------")
print(matrix[0])
print(matrix[1])
print(matrix[2])
print(matrix[3])
print(matrix[4])
print(matrix[5])
print(matrix[6])
print(matrix[7])
print(matrix[8])
print(matrix[9])
str1="申購中"
for i in range(10):
    #print(matrix[i][5])
    if matrix[i][6] in str1:
        print(matrix[i][1])


print("--------------coin--------------")
matrix2=[[],[],[],[],[],[],[],[]]
uuuu='https://rate.bot.com.tw/xrt/all/day'
resp2=requests.get(uuuu, headers=headers)
soup2=BeautifulSoup(resp2.text, features='lxml')
catch_large=soup2.find_all('div',{"class":re.compile('visible')})
for h in range(8):
    print(catch_large[h].get_text().strip())
 
    num=catch_large[h].get_text().strip().split()[0]
    name=catch_large[h].get_text().strip().split()[1]
    matrix2[h].append(num)
    matrix2[h].append(name)
print(matrix2)
buy=soup2.find_all('td',{"data-table":re.compile('本行現金買入')})
for h in range(8):
    #print(buy[h].get_text())
    matrix2[h].append(buy[h].get_text().strip())
print(matrix2)

sell=soup2.find_all('td',{"data-table":re.compile('本行現金賣出')})
for h in range(8):
    #print(buy[h].get_text())
    matrix2[h].append(sell[h].get_text().strip())
print(matrix2)







input=""
dataNumber=""
input2=""
dataNumber2=""

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )


    def is_going_to_hellow(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '你好'
        return False

    def is_going_to_state1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '申購資訊'
        return False

    def is_going_to_state2(self, event):
        if event.get("message"):
            text = event['message']['text']
            for i in range(10):
                print("miss")
                if(text.lower()==matrix[i][0]):
                    global input
                    global dataNumber
                    input=matrix[i][0]
                    dataNumber=i
                    print("hit")
                    return True

            #return text.lower() == 'go to state2'
        return False

    def is_going_to_state3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '想知道更多'
        return False

    def is_going_to_state4(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '匯率查詢'
        return False

    def is_going_to_state5(self, event):
        if event.get("message"):
            text = event['message']['text']
            for i in range(8):
                print("miss")
                if(text.lower()==matrix2[i][0]):
                    global input2
                    global dataNumber2
                    input2=matrix2[i][0]
                    dataNumber2=i
                    print("hit")
                    return True
        return False

    def is_going_to_state6(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'k線教學'
        return False

    def is_going_to_state7(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '陽線'
        return False

    def is_going_to_state8(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '陰線'
        return False

    

    def on_enter_hellow(self,event):
        print("I'm entering hellow")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "請問需要什麼服務呢？")
        responese = send_text_message(sender_id, "申購資訊")
        responese = send_text_message(sender_id, "匯率查詢")
        responese = send_text_message(sender_id, "k線教學")
        responese = send_text_message(sender_id, "請鍵入所需要的服務")
        
        #self.go_back()


    def on_enter_state1(self, event):
        print("I'm entering state1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "以下是目前可申購或即將開放申購的股票")
        for i in range(10):
            if matrix[i][6] in str1:
                print(matrix[i][1])
                responese = send_text_message(sender_id, matrix[i][0]+" "+matrix[i][1])
        responese = send_text_message(sender_id, "請輸入欲查詢股票代號")
        #self.go_back()

    def on_exit_hellow(self,event):
        print('Leaving hellow')

    def on_exit_state1(self,event):
        print('Leaving state1')

    

    def on_enter_state2(self, event):
        print("I'm entering state2")
        sender_id = event['sender']['id']
        print("I'm entering state2")
        responese = send_text_message(sender_id, "您的查詢為:\n"+input+" "+matrix[dataNumber][1])
       
        temp="申購期間:"+matrix[dataNumber][2]+"\n市價:"+matrix[dataNumber][3]+"\n可獲利:"+matrix[dataNumber][4]+"\n報酬率:"+matrix[dataNumber][5]+"%"
        responese = send_text_message(sender_id, temp)
        

        """tag = input("請輸入定位元素，class前面加上.，id前面加上# ")"""
        tag = ".collap"
        res = requests.get('https://pala.tw/perfect-match/')
        soup = BeautifulSoup(res.text, "lxml")

        for drink in soup.select('{}'.format(tag)):
            print(drink.get_text())



        sender_id = event['sender']['id']
        send_text_message(sender_id, "I'm entering state2")
        #self.go_back()

    


    def on_enter_state3(self, event):
        print("I'm entering state3")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "I'm entering state3")
        responese = send_text_message(sender_id, "個股資訊:\n https://histock.tw/stock/"+matrix[dataNumber][0])
        self.go_back()

    


    def on_enter_state4(self, event):
        print("I'm entering state4")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "請問想查詢哪國貨幣？")
        send_text_message(sender_id, matrix2[0][0]+matrix2[0][1])
        send_text_message(sender_id, matrix2[1][0]+matrix2[1][1])
        send_text_message(sender_id, matrix2[2][0]+matrix2[2][1])
        send_text_message(sender_id, matrix2[3][0]+matrix2[3][1])
        send_text_message(sender_id, matrix2[4][0]+matrix2[4][1])
        send_text_message(sender_id, matrix2[5][0]+matrix2[5][1])
        send_text_message(sender_id, matrix2[6][0]+matrix2[6][1])
        send_text_message(sender_id, matrix2[7][0]+matrix2[7][1])
        send_text_message(sender_id, "請輸入想查詢的貨幣種類")

        #self.go_back()

    def on_exit_state4(self,event):
        print('Leaving state4')

    def on_enter_state5(self, event):
        sender_id = event['sender']['id']
        print("I'm entering state5")
        responese = send_text_message(sender_id, "您的查詢為:\n"+input2+" "+matrix2[dataNumber2][1])
       
        temp="現金買入價:"+matrix2[dataNumber2][2]+"\n現金賣出價:"+matrix2[dataNumber2][3]
        responese = send_text_message(sender_id, temp)

        self.go_back()

    def on_enter_state6(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id, "請想了解陽線還是陰線呢")
        print("I'm entering state6")
        
    def on_enter_state7(self, event):
        print("I'm entering state7")
        sender_id = event['sender']['id']
        send_text_message(sender_id, "紅K線是由開盤漲升所形成的，因此收盤＞開盤。 如某一支股票開盤時50元，盤中最低到48，然後衝高至55最高，最後以53收盤，這就是如上圖，留下上下影線的標準「紅K線」了")
        send_image_url(sender_id, "http://www.cmoney.tw/notes/cmstatic/notes/capture/114678/20140919112237467.jpg")
        print("I'm entering state7")
        self.go_back()
        
    def on_enter_state8(self, event):
        print("I'm entering state8")
        sender_id = event['sender']['id']
        send_text_message(sender_id, "黑 K線是由開盤後下跌所形成的，因此開盤＞收盤。\n如某一支股票開盤時53元，盤中最高到55，然後下跌至48最低，最後以50 元收盤，這就是如上圖，留下上下影線的標準「黑K線」了。 \n黑K線並不代表今天的股票一定是跌的，也有可能開在高盤，而收盤卻在平盤以上的黑K線，以K線的原理來說， \n黑K線的意義是代表股票在「弱勢」的一種表徵。 \n如果下影線愈長，代表雖賣壓強，但買盤更強，屬多方勝利。")
        send_image_url(sender_id, "http://www.cmoney.tw/notes/cmstatic/notes/capture/114678/20140919112443107_o.jpg")
        print("I'm entering state8")
        self.go_back()

    
