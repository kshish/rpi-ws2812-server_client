import socket
from time import sleep

delay = 1
HOST = '192.168.1.18' # Enter IP or Hostname of your server
PORT = 9999 # Pick an open Port (1000+ recommended), must match the server port

loops = 10
i = 0
while i < loops

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST,PORT))

    #command = ';'
    command =  'random 1,0,300,RGBWL;fade 1,255,0,' + str(delay) +',0,300;'
    server_thread = 'thread_start;' + command + ';thread_stop;'
    #command = raw_input('Enter your command: ')
    print command
    #s.send(command)
    s.send(server_thread)
    #reply = s.recv(1024)
    sleep(1)
    s.close()
    sleep(1)
    loops = loops + 1
