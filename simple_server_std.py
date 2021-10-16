import zmq

if __name__ == '__main__':

server = zmq.Context()
socket = server.socket(zmq.REP)
socket.bind('tcp://*:9000)

print('server started')
while True:
# server responds to client request
message = socket.recv_string()
if message == 'quit':
socket.sent_string('Bye Bye')
break
else:
socket.send_string(f'Hello, {message}!')

print('Server Closed')

