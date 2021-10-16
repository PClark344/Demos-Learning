import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((socket.gethostname(),4571))

s.listen(5)
print('Server is up and listening...')

client, address = s.accept()
print('\nConnected to: ',address)
print('\nClient object is: ',client)

msg = 'Hello World'
client.send(msg.encode())
#client.send(bytes(msg,'utf-8'))

s.close()
