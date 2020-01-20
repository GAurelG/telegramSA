#!/usr/bin/env python3
from pathlib import Path
from bs4 import BeautifulSoup
import psycopg2
import sys

current_path = Path(__file__).parent
file_path = (current_path / "./Data/messages.html").resolve()

with open(file_path) as fp:
    soup = BeautifulSoup(fp)

#print(soup.div.div.prettify())
#print(soup.find(attrs={"class" : "message default clearfix"}).prettify())

raw_messages = soup.find_all(attrs = {"class" : "message default clearfix"})

def cleanHashtags(html_message_list):
    try:
        ret = [hashtag.string.strip("#") for hashtag in html_message_list]
    except:
        ret = html_message_list
    return ret

def cleanLinks(html_links_list):
    ret = [link["href"] for link in html_links_list]
    return ret

def extractMessage(html_message):
    msg = { "message_id" : html_message['id'],
            "time" : html_message.find(attrs = {"class" : "date"})['title'],
            "user" : html_message.find(attrs = {"class" : "from_name"}).string,
            "message" :  None,
            "hashtag" : cleanHashtags(html_message.find_all(attrs = {"onclick" : re.compile("ShowHashtag(.*)")})),
            "links" : cleanLinks(html_message.find_all(href=re.compile("."))),
            "raw_message" : html_message
    }
    if html_message.find(attrs = {"class" : "text"}):
        msg["message"] = html_message.find(attrs = {"class" : "text"}).next_element
        # using the fact that .next_element return the inside of the message which is empty before 
        # the next <a> tag inside (for cases of link/hashtags)
    else:
        msg["message"] = "not found"
    try:
        msg["user"] = msg["user"].strip()
        msg["message"] = msg["message"].strip()
    except:
        pass
    return msg

# could None the hashtags, message, links when empty, but could also do it when integrating results somewhere else
# need to document the functions + use cases covered.

msg_list = [extractMessage(items) for items in raw_messages]
msg_list[13]
#raw_messages

strange = soup.find(attrs={"id" : "message175714"})
strange
strange.find(attrs = {"class" : "from_name"}).next_sibling.next_sibling

def save_message(message, dbconn):
    # function that saves one message at a time?
    pass

def db_setup():

#example db setup from doc

con = None
try
    con = psycopg2.connect("host='localhost' dbname='testdb' password='password'")
    cur = con.cursor()
    cur = cur.execute("CREATE TABLE Products(Id INTEGER PRIMARY KEY, Name VARCHAR(20), Price INT)")
    cur = cur.execute(INSERT INTO Products VALUES(2,'Sugar',7)")
    cur.execute("INSERT INTO Products VALUES(3,'Coffee',3)")
    cur.execute("INSERT INTO Products VALUES(4,'Bread',5)")
    cur.execute("INSERT INTO Products VALUES(5,'Oranges',3)")
    con.commit()
except psycopg2.DatabaseError, e:
    if con:
         con.rollback()
     print 'Error %s' % e    
    sys.exit(1)
    
finally:   
    if con:
        con.close()
