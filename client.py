import random
import socket
import threading
import time

import const
from data_pack import *
from utils import *


class RadiusClient:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.start_handle()

    def start_handle(self):
        t = threading.Thread(target=self.handle, daemon=True)
        t.start()

    def send_data(self, data, request_type='access_request'):
        port = config.SERVER_ACCESS_REQUEST_PORT
        if request_type == 'accounting_request':
            port = config.SERVER_ACCOUNTING_REQUEST_PORT
        self.client.sendto(data, (config.SERVER_HOST, port))
        time.sleep(0.1)

    def handle(self):
        while True:
            data, (host, port) = self.client.recvfrom(1024)
            print(f'from {host}:{port} received: {data}')
            if data[0] == 2:
                print('Access_Accept')
            elif data[0] == 3:
                print('Access_Reject')
            elif data[0] == 5:
                print('Accounting_Response')

    def access_request(self):
        authenticator = gen_access_request_request_authenticator()
        encrypted_password = gen_user_password('123', authenticator)
        params = {
            'code': const.Code_Access_Request,
            'identifier': random.randint(0, 255),
            'authenticator': authenticator,
            'user_name': TLV(const.AttributeType_User_Name, 'daihui'),
            'user_password': TLV(const.AttributeType_User_Password, encrypted_password),
            'nas_ip_address': TLV(const.AttributeType_NAS_IP_Address, config.SERVER_HOST),
            'nas_port': TLV(const.AttributeType_NAS_Port, config.SERVER_ACCESS_REQUEST_PORT),
            'service_type': TLV(const.AttributeType_Service_Type, 1),
            'framed_protocol': TLV(const.AttributeType_Framed_Protocol, 1),
            'framed_ip_address': TLV(const.AttributeType_Framed_IP_Address, '127.0.0.1')
        }
        data = RadiusDataPack(**params).pack()
        self.send_data(data)

    def accounting_request(self):
        code = const.Code_Accounting_Request
        identifier = random.randint(0, 255)
        acct_status_type = TLV(const.AttributeType_Acct_Status_Type, const.Acct_Status_Type_Start)
        acct_authentic = TLV(const.AttributeType_Acct_Authentic, 1)
        params = {
            'code': code,
            'identifier': identifier,
            'authenticator': b'\x00' * 16,
            'acct_status_type': acct_status_type,
            'acct_delay_time': TLV(const.AttributeType_Acct_Delay_Time, 1),
            'acct_authentic': acct_authentic
        }
        datapack = RadiusDataPack(**params)
        attributes = gen_accounting_request_attributes(params)
        authenticator = gen_accounting_request_request_authenticator(code, identifier, datapack.length,
                                                                     attributes)
        params['authenticator'] = authenticator
        data = RadiusDataPack(**params).pack()
        self.send_data(data, 'accounting_request')
