# coding=utf-8

import sys
import time
import telepot
import re
from pprint import pprint
import markovify

def getMarkovSentence():
    # Get raw text as string.
    with open("Data/historic_messages") as f:
        text = f.read()
    text_model = markovify.NewlineText(text)
    sentence = text_model.make_sentence(tries=20)
    f.close()
    return sentence or "No tengo nada para decir."

def persistMessage(msg):
     f = open('Data/historic_messages', 'a+')
     f.write(msg)
     f.write("\n")
     f.close()



def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    pprint(msg)
    #print(content_type, chat_type, chat_id)

    if content_type == 'text':
    	matchObj = re.match("^padel (.*) *", msg['text'])
        if matchObj:
            command = matchObj.group(1)
            fromUser = msg['from']['username']
            print "[Command] ", command, " from ", fromUser
            if command == 'habla':
                messageToSend = getMarkovSentence()
                bot.sendMessage(chat_id, messageToSend)
        else:
            persistMessage(msg['text'])
        if msg['text'] == '/whoareyou':
            bot.sendMessage(chat_id, "I'm a Bot programmed in Python, and y'all suck.")

TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)