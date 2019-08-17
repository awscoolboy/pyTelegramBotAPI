import telebot
import os
import requests
import json
import urllib.parse
from flask import Flask
import time

from telebot import types


from telebot import util
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

app = Flask(__name__)


TOKEN = "982194297:AAE42Miio1m6OI_3KD3QErr9AIJNnZ_tFdg"
#TOKEN = "831127829:AAFhNrcczj3MvqfTn3Br2L5F8qiDBz6cgzo"
bot = telebot.AsyncTeleBot(TOKEN)
headers ={}

status_channel = "@realtimedataresult"
#status_channel = "@bzappsgroup"

add_request_link = "https://mobogram-a636b.firebaseio.com/advertizment/bot/exam_bot.json"


headers["Content-Type"]='application/x-www-form-urlencoded; charset=UTF-8'
headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
headers["Referer"] = "http://app.neaea.gov.et/"
headers["Cookie"] = "__RequestVerificationToken=0rxDFg0_Ofd1iF4uI46SFynayOQDI5RXSxVF1hSK6Tk0UBI7rc396UcGomh_phNXelqqnyJmiC9Zhe2yv15zW5tiD-TeiaP0R4avo27N48g1; _gid=GA1.3.967631655.1565681521; _ga=GA1.1.1101697647.1565502014; _ga_KVM895P5HM=GS1.1.1565706743.7.1.1565707915.0"
headers["X-Requested-With"] = "XMLHttpRequest"
endpoint = 'http://app.neaea.gov.et/Home/result/'



add_image= "https://lh3.googleusercontent.com/gr7Ked11EsnSvh824Pn7k4pZKZc7jCDieP2FDi-6SqiMdcMIs1o2pyJ9drK1C75MxeY=s360-rw"
app_link = "https://play.google.com/store/apps/details?id=com.liteplus.messenger"
app_desc = "Lite:Plus Messenger is an unofficial messaging app that uses Telegram's API."



# def download_image_and_send(url, name,synop,chat_id,num):
#     fullname = str(name) + ".jpg"
#     r = requests.get(url, allow_redirects=True)
#     open(fullname, 'wb').write(r.content)
#     photo = open(fullname, 'rb')
#
#     #start
#
#     keyboard = types.InlineKeyboardMarkup()
#     callback_button = types.InlineKeyboardButton(text="Downlod", callback_data="")
#     types.InlineKeyboardButton(text="Hello", callback_data="")
#
#     keyboard.add(callback_button)
#
#     bot.send_message(chat_id,"You hart for take away",reply_markup=keyboard)
#
#     #end
#


    # bot.send_photo(chat_id, photo, caption=synop,reply_markup=reply_markup)
    # if os.path.isfile(fullname):
    #     os.remove(fullname)
    # else:
    #     print("Error: %s file not found")
    # file1 = open("statics.txt", "w+")
    # file1.write(url + ",chat_id_" + str(chat_id) + ",reg_num_" + str(num))
    # bot.send_message(status_channel,url + ",chat_id_" + str(chat_id) + ",reg_num_" + str(num))
    # file1.write("\n")
    # file1.close()





def doRequest(number,chat_id):
    try:
       params = {'Registration_Number': str(number),
          '__RequestVerificationToken': '2TJSVSh_-Vn_WIHE-Pa6HMmjJcJLto67qEZuc9oSmG7q7waDoh_DMOb0gHWveUy0j-KFaBtSrwFly8-kLBF8EseYQ2u1chslGjsNp2mlR1U1'}
       data = urllib.parse.urlencode(params, doseq=True)
       r = requests.post(url=endpoint, data=data, headers=headers)
       d = json.loads(r.text)
       sex = d["s"]["s"]
       if sex == "Female":
           sex += " 👧"
       elif sex == "Male":
           sex += " 👦"
       school = d['s']['sc'] + " 🏫"
       keyboard = types.InlineKeyboardMarkup(row_width=2)
       keyboard.add(
           types.InlineKeyboardButton(text="Name", callback_data="1"),
           types.InlineKeyboardButton(text=d["s"]["fn"], callback_data="2"),
           types.InlineKeyboardButton(text="Sex", callback_data="3"),
           types.InlineKeyboardButton(text=sex, callback_data="4"),
           types.InlineKeyboardButton(text="School", callback_data="5"),
           types.InlineKeyboardButton(text=school, callback_data="6"),
           types.InlineKeyboardButton(text="Stream", callback_data="7"),
           types.InlineKeyboardButton(text=d["s"]["st"], callback_data="8")
       )
       mark = d['m']
       im_link = "http://app.neaea.gov.et" + str(d['s']['ph']).replace("~", "").strip().replace(" ","%20")
       total=0
       for k, v in mark.items():
         total += v
         keyboard.add(
         types.InlineKeyboardButton(text=str(k), callback_data=str(k)),
         types.InlineKeyboardButton(text=str(v), callback_data=(str(v))))

       keyboard.add(
          types.InlineKeyboardButton(text="Total 🔥🔥🔥", callback_data="100"),
          types.InlineKeyboardButton(text=str(total), callback_data="102")
       )


       moti_message = ""
       if total >= 600:
          moti_message ="😱 Genius"
       elif total<600 and total>=500:
           moti_message = "😄 Intelligent"
       elif total <500 and total>=400:
           moti_message = "👍 Great"
       elif total < 400 and total >= 300:
           moti_message = "😏 Not bad"
       elif total < 300 and total >= 200:
           moti_message = "😢"
       elif total < 200:
           moti_message = "😜"




       types.InlineKeyboardMarkup(row_width=1)
       keyboard.add(types.InlineKeyboardButton(text=moti_message, callback_data="1006"))
       keyboard.add(types.InlineKeyboardButton(text="YOUR RANK IN SCHOOL", callback_data="1006",url= "https://t.me/ShillionerBot?start=r0952840102"))


       # types.InlineKeyboardMarkup(row_width=2)
       keyboard.add(types.InlineKeyboardButton(text="SPONSOR 1", callback_data="1008",url= "https://t.me/joinchat/AAAAAEdAo9uAHlnBbjKdxg"))
       keyboard.add(types.InlineKeyboardButton(text="SPONSOR 2", callback_data="1009",url= "https://t.me/joinchat/AAAAAEHerPG0OpTJJM-WxA"))

       keyboard.add(types.InlineKeyboardButton(text="For Advertisement 😎", callback_data="156",url= "https://t.me/awscoolboy"))
       # keyboard.add(types.InlineKeyboardButton(text="Admin 😎", callback_data="15678",url= "https://t.me/awscoolboy"))


       name = "photo"
       fullname = str(name) + ".jpg"
       r = requests.get(im_link, allow_redirects=True)
       open(fullname, 'wb').write(r.content)
       photo = open(fullname, 'rb')
       bot.send_photo(chat_id, photo, reply_markup=keyboard)
       if os.path.isfile(fullname):
           os.remove(fullname)
       else:
           print("Error: %s file not foun")



       #download_image_and_send(im_link,"photo",str(final_mess),chat_id,number)
       #download_image_and_send_add(add_image,chat_id)
    except:
        pass


def is_number(s):
    try:
        float(s) # for int, long and float
    except ValueError:
        try:
            complex(s) # for complex
        except ValueError:
            return False

    return True


def sendAddVertizment(chat_id,message):
    # reqest for add
    r = requests.get(add_request_link, allow_redirects=True)
    d = json.loads(r.text)

    app_name = d['app_name']
    app_link = d['app_link']
    bot_text = d['bot_text']
    app_desc = d['app_desc']
    app_logo = d['app_logo']

    add_message = app_name + "\n\n" + app_desc

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text=bot_text, callback_data="89", url=app_link))

    name = "addphoto"
    fullname = name
    r = requests.get(app_logo, allow_redirects=True)
    open(fullname, 'wb').write(r.content)
    photo = open(fullname, 'rb')
    bot.send_photo(chat_id=chat_id, caption=add_message, photo=photo, reply_markup=keyboard)
    if os.path.isfile(fullname):
        os.remove(fullname)
    else:
        print("Error: %s file not foun")


    bot.send_message(status_channel, "chat_id_" + str(message.chat.id) + ",reg_num_" + str(message.text))
    time.sleep(10)
    bot.send_message(message.chat.id, "Getting your result ... ")
    doRequest(message.text, message.chat.id)


def parseResult(message):
    sendAddVertizment(message.chat.id,message)




@bot.message_handler(func=lambda m: True)
def sendReutl(message):
    if message.text == "/start" or message.text == "/help":
        bot.send_message(message.chat.id, "Send me your admission number")
    elif(is_number(message.text)) and len(message.text)==6:
        parseResult(message)
    else:
        bot.send_message(message.chat.id,"Wrong input! Send the correct admission number!")







#removed


#bot.polling()



if __name__ == "__main__":
    app.run()
else:
    application = app

@app.route('/start/thisissdtupid10134557')
def hello():
    while True:
        bot.polling()
        time.sleep(5)
