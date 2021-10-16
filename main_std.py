# From Standard Answer
# not finished yet

import zmq
import time

if __name__ == '__main__':
    client = zmq.Context()
    socket = client.socket(zmq.REQ)

    socket.connect('tcp://localhost:9000')

