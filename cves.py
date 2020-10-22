#!/usr/lib/zabbix/externalscripts/check-cves/venv/bin/python

#--------------------------------------------------------------------
# file:         cves.py
# comment:      Coletar informacoes das ultimas Cves descobertas
# author:       Lenon Corrêa <lenonac_@hotmail.com>
# date:         01-09-2020
# Last updated: 04-09-2020
#--------------------------------------------------------------------

import requests
import json
import urllib
from time import sleep
from dotenv import load_dotenv
import os
import socket

class Socket:
  def __init__(self):
    host = ""   #Nome ou endereço IP da máquina servidora
    port = 3000 #Porta que o servidor vai aguardar conexões
    createsock = self.create_socket(host,port)
    opensock = self.open_socket(createsock)
    
  def create_socket(self,host,port):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Cria um socket usando o protocolo TCP
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # Fecha o socket caso o programa seja interrompido, por exemplo, com CONTROL+C
    soc.bind((host,port))   # Associa a porta e o host ao socket
    return soc
  
  def open_socket(self,soc):
    soc.listen(100)   # Inicia uma thread que aguarda por uma conexão
    while True:   # Loop infinito que aguarda conexões, uma de cada vez
      print("Aguardando conexão na porta 3000")
      con, client = soc.accept()
      while True:
        msg = con.recv(1024).decode()
        print("Recebeu de " + str(client) + ": " + msg)
        print(">> " + str(client) + ": " + msg)
        cve = Cves()
        request = cve.requesting()
        last_result = []
        check = cve.check_cve(request,last_result)
        con.sendall('request'.encode())   #Envia para o cliente o conteúdo da variável resultado 
    

    # con.sendall(resultado.encode())   #Envia para o cliente o conteúdo da variável resultado
  # con.close()

class Bot:
  def __init__(self):
    load_dotenv()
    token = os.getenv("TOKEN")
    self.chat_id = os.getenv("CHAT_ID")
    self.baseUrl = "https://api.telegram.org/bot{}/".format(token)
    
  def get_url(self,url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

  def send_message(self,cve,summary,reference):
    cve = urllib.parse.quote_plus(cve)
    summary = urllib.parse.quote_plus(summary)
    url = self.baseUrl + "sendMessage?text={}\nSummary: {}\nReference: {}&chat_id={}&parse_mode=Markdown".format(cve,summary,reference,self.chat_id)
    self.get_url(url)

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
      return results
      # sleep (600)
      # request = self.requesting()
      # self.check_cve(request,last_result)
    else:
      for data in results:
        if data not in last_result:
          cve_id = data['id']
          cve_summary = data['summary']
          cve_link = 'https://cve.mitre.org/cgi-bin/cvename.cgi?name='+data['id']
          # bot = Bot()
          # bot.send_message(cve_id,cve_summary,cve_link)
      last_result = results
      # sleep (300)
      # request = self.requesting()
      # self.check_cve(request,last_result)
      return results

def main():
  socket = Socket()
  socket.create_socket()
  # cve = Cves()
  # request = cve.requesting()
  # last_result = []
  # check = cve.check_cve(request,last_result)
      
if __name__ == '__main__':
  result = main()
  