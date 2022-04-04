import sys
sys.path.insert(0, r"C:\Users\61422\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.7_qbz5n2kfra8p0\LocalCache\local-packages\Python37\site-packages")
import discord
from discord.ext import commands

#629341858170142720 bot id
#token
#75776 PERMISSIONS INTEGER
#https://discordapp.com/oauth2/authorize?client_id=629341858170142720&scope=bot&permissions=75776

poop = "D"
client = commands.Bot(command_prefix = "*")

@client.event 
async def on_ready():
    print("Hello ")

#@client.event
#async def on_message(message):
 #   author = message.author 
  #  content = message.content
   # channel = message.channel
    #if author == client.user:
     #   return

    #print("{}:{}".format(author, content)) #prints on terminal username and what they said

    #if content.startswith("declan"):
     #   await channel.send( "Did you  say Declan @{}".format(author) + " I fucking hate that guy")


#        await channel.send(content) #replys back with what they said
    #if author.name == "Notch": #when in server change to declans name
     #   await channel.send("what up gamer")


      #  messages = []
       # async for message in clinet.logs_from(channel, limit = 1):
        #    messages.append(message)
        #await clinet.delete_messages(message)
        #await client.say("Message/s deleted")
    













import argparse
import json
import itertools
import logging
import re
import os
import uuid
from urllib.request import urlopen, Request

from bs4 import BeautifulSoup




REQUEST_HEADER = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}


def get_soup(url, header):
    response = urlopen(Request(url, headers=header))
    return BeautifulSoup(response, 'html.parser')


def get_query_url(query):
    return "https://www.google.co.in/search?q=%s&source=lnms&tbm=isch" % query


def extract_images_from_soup(soup):
    image_elements = soup.find_all("div", {"class": "rg_meta"})
    metadata_dicts = (json.loads(e.text) for e in image_elements)
    link_type_records = ((d["ou"], d["ity"]) for d in metadata_dicts)
    return link_type_records


def extract_images(query, num_images):
    url = get_query_url(query)
    soup = get_soup(url, REQUEST_HEADER)
    link_type_records = extract_images_from_soup(soup)
    return itertools.islice(link_type_records, num_images)


def get_raw_image(url):
    req = Request(url, headers=REQUEST_HEADER)
    resp = urlopen(req)
    return resp.read()





def main():
    parser = argparse.ArgumentParser(description='Scrape Google images')
    parser.add_argument('-s', '--search', default='bananas', type=str, help='search term')
    parser.add_argument('-n', '--num_images', default=100, type=int, help='num images to save')
    parser.add_argument('-d', '--directory', default='G:\__main__\tf_files\flower_photos', type=str, help='save directory')
    args = parser.parse_args()
    run(args.search, args.directory, args.num_images)

if __name__ == '__main__':
    main()

client.run("NjI5MzQxODU4MTcwMTQyNzIw.XZYWdQ.JycuFW1feS28tDelXItIZ19pu8M")