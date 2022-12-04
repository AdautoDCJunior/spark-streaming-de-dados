import os
import socket
from dotenv import load_dotenv, find_dotenv
from time import sleep

load_dotenv(find_dotenv())

host = os.getenv('HOST')
port = int(os.getenv('PORT'))

s = socket.socket()
s.bind((host, port))
print(f'Aguardando conexão na porta: {port}')

s.listen(5)
conn, address = s.accept()

print(f'Recebendo solicitação de {address}')

messages = [
  'Mensagem A',
  'Mensagem B',
  'Mensagem C',
  'Mensagem D',
  'Mensagem E',
  'Mensagem F',
  'Mensagem G',
]

for message in messages:
   message = bytes(message, 'utf-8')
   conn.send(message)
   sleep(4)

conn.close()