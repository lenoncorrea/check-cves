#!/usr/lib/zabbix/externalscripts/check-cves/venv/bin/python

#--------------------------------------------------------------------
# file:         cves.py
# comment:      Coletar informacoes das ultimas Cves descobertas
# author:       Lenon Corrêa <lenonac_@hotmail.com>
# date:         01-09-2020
# Last updated: 02-09-2020 17:13:00
#--------------------------------------------------------------------

import requests
import json
import urllib
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()


class Bot:
  def __init__(self):
    token = os.getenv("TOKEN")
    self.chat_id = os.getenv("CHAT_ID")
    self.baseUrl = "https://api.telegram.org/bot{}/".format(token)
    
  def get_url(self,url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

  def send_message(self,cve,summary):
    cve = urllib.parse.quote_plus(cve)
    summary = urllib.parse.quote_plus(summary)
    url = self.baseUrl + "sendMessage?text={}\nSummary: {}&chat_id={}&parse_mode=Markdown".format(cve,summary,self.chat_id)
    self.get_url(url)
    return True

class Cves:
  def __init__(self):
      self.baseUrl = 'https://cve.circl.lu/api/last'

  def requesting(self):
      response = requests.get(self.baseUrl)
      result = response.text.encode('utf8')
      results = json.loads(result)
      return results
  
  def check_cve(self,results,last_result):
    if (results == last_result):
      sleep (300)
      request = self.requesting()
      self.check_cve(request,last_result)
    else:
      for data in results:
        if data not in last_result:
          cve_id = data['id']
          cve_summary = data['summary']
          bot = Bot()
          bot.send_message(cve_id,cve_summary)
        last_result = results
      sleep (300)
      request = self.requesting()
      self.check_cve(request,last_result)

def main():
  cve = Cves()
  request = cve.requesting()
  last_result = []
  check = cve.check_cve(request,last_result)
      
if __name__ == '__main__':
  result = main()
  