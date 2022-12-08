import os
from socket import socket
import tweepy
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

host = os.getenv('HOST')
port = int(os.getenv('PORT'))
token = os.getenv('TOKEN')

s = socket()
s.bind((host, port))
print(f'Aguardando conexão na porta: {port}')

s.listen(5)
connection, address = s.accept()
print(f'Recebendo solicitação de {address}')

keyword = 'copa'

class GetTweets(tweepy.StreamingClient):
  def on_tweet(self, tweet):
    print(tweet.text)
    print('='*50)
    connection.send(tweet.text.encode('utf-8', 'ignore'))

printer = GetTweets(token)
printer.add_rules(tweepy.StreamRule(keyword))
printer.filter()

connection.close()