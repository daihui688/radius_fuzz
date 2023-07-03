import socket
import random

from radius_data import *
from utils import *

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

code = 1
identifier = random.randint(0, 255)
authenticator = gen_request_authenticator()
user_name = TLV(1, 'testing')
user_password = TLV(2, gen_user_password('password', authenticator))
nas_ip_address = TLV(4, '127.0.1.1')
nas_port = TLV(5, 1812)

_struct = struct.Struct(f'>BBH16s')

length = _struct.size + user_name.length + user_password.length + nas_ip_address.length + nas_port.length
data = _struct.pack(code, identifier, length, authenticator) + user_name.pack() + user_password.pack() + \
       nas_ip_address.pack() + nas_port.pack()
# message_authenticator = TLV(80, gen_message_authenticator(data))
# data += message_authenticator.pack()

print(len(data), data)
client.sendto(data, ('127.0.0.1', 1812))
data, (host, port) = client.recvfrom(1024)
if data[0] == 2:
    print('Access-Accept')
elif data[0] == 3:
    print('Access-Reject')

client.close()

