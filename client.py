import random
import socket

import const
from data_pack import *
from utils import *


class RadiusClient:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_data(self, data):
        self.client.sendto(data, (config.SERVER_HOST, config.SERVER_PORT))

    def handle(self):
        data, (host, port) = self.client.recvfrom(1024)
        print(host, port)
        if data[0] == 2:
            print('Access-Accept')
        elif data[0] == 3:
            print('Access-Reject')

    def access_request(self):
        authenticator = gen_request_authenticator()
        encrypted_password = gen_user_password('123',authenticator)
        params = {
            'code': const.Code_Access_Request,
            'identifier': random.randint(0, 255),
            'authenticator': authenticator,
            'user_name': TLV(const.AttributeType_User_Name, 'daihui'),
            'user_password': TLV(const.AttributeType_User_Password, encrypted_password),
            'nas_ip_address': TLV(const.AttributeType_NAS_IP_Address, config.SERVER_HOST),
            'nas_port': TLV(const.AttributeType_NAS_Port, config.SERVER_PORT),
        }
        data = RadiusDataPack(**params).pack()
        self.send_data(data)
        self.handle()
