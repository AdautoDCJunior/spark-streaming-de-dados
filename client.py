import os
import socket
from dotenv import load_dotenv, find_dotenv
from time import sleep

load_dotenv(find_dotenv())

host = os.getenv('HOST')
port = int(os.getenv('PORT'))

s = socket.socket()
s.connect((host, port))

while True:
  data = s.recv(1024)
  print(data.decode('utf-8'))
  sleep(2)