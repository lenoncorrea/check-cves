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
    text = urllib.parse.quote_plus(summary)
    url = self.baseUrl + "sendMessage?text={}+\nSummary:{}&chat_id={}&parse_mode=Markdown".format(cve,summary, self.chat_id)
    print(url)
    self.get_url(url)
    return None

class Cves:
  def __init__(self):
      self.baseUrl = 'https://cve.circl.lu/api/last'

  def requesting(self):
      response = requests.get(self.baseUrl)
      result = response.text.encode('utf8')
      results = json.loads(result)
      return results
  
  def check_cve(self,results):
      for data in results:
        cve_id = data['id']
        cve_summary = data['summary']
      return cve_id,cve_summary

def main(cve_id):
  cve = Cves()
  request = cve.requesting()
  last_cve = cve.check_cve(request)
  if (cve_id == last_cve[0]):
    sleep (300)
    main(cve_id)
  else:
    cve_id = last_cve[0]
    cve_summary = last_cve[1]
    bot = Bot()
    res = bot.send_message(cve_id,cve_summary)
    sleep(300)
    main(cve_id)
    
if __name__ == '__main__':
  cve_id = 0
  result = main(cve_id)
  