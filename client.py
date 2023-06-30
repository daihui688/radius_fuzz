import socket

from radius_data import *
from utils import *

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

code = 1
identifier = 1
authenticator = gen_request_authenticator()
user_name = TLV(1,'daihui')
user_password = TLV(2,gen_user_password('123'))
nas_ip_address = TLV(4,'127.0.0.1')
nas_port = TLV(5,1812)
message_authenticator = TLV(80,b'\x8e\x48\x93\x19\x2d\x25\x49\x5c\x7c\x84\xba\xc8\xba\x23\x75\xe5')
_struct = struct.Struct(f'BBH16s')
length = _struct.size + user_name.length + user_password.length + nas_ip_address.length + nas_port.length + \
message_authenticator.length


data = _struct.pack(code,identifier,length,authenticator)+user_name.pack()+user_password.pack() +nas_ip_address.pack()\
       + nas_port.pack() +message_authenticator.pack()
print(data,len(data))
client.sendto(data, ('127.0.0.1', 1812))
data, (host, port) = client.recvfrom(1024)
print(data.decode('utf-8'))

client.close()