#!/usr/bin/env python3
from pathlib import Path
from bs4 import BeautifulSoup

current_path = Path(__file__).parent
file_path = (current_path / "./Data/messages.html").resolve()

with open(file_path) as fp:
    soup = BeautifulSoup(fp)

#print(soup.div.div.prettify())
#print(soup.find(attrs={"class" : "message default clearfix"}).prettify())

raw_messages = soup.find_all(attrs = {"class" : "message default clearfix"})

def extractMessage(html_message):
    msg = {
        "message_id" : html_message['id'],
        "time" : html_message.find(attrs = {"class" : "date"})['title'],
        "user" : html_message.find(attrs = {"class" : "from_name"}).string,
        "message" :  html_message.find(attrs = {"class" : "text"}).string
    }
    
    try:
        msg["user"] = msg["user"].strip()
        msg["message"] = msg["message"].strip()
    except:
        print(msg)
    return msg

msg_list = [extractMessage(items) for items in raw_messages]
msg_list[13]
#raw_messages

#need to handle cases with a hashtag, there seem to be problem with the parsing algorithm for them
strange = soup.find(attrs={"id" : "message175714"})
strange
strange.find(attrs = {"class" : "from_name"}).next_sibling.next_sibling

