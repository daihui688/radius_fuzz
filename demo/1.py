import hashlib
import hmac
import struct


def generate_message_authenticator(packet_data, shared_secret):
    # 将packet_data和共享密钥进行HMAC-MD5运算
    md5_hash = hmac.new(shared_secret.encode(), packet_data, hashlib.md5).digest()

    # 获取前16个字节作为Message-Authenticator字段
    message_authenticator = md5_hash[:16]

    return message_authenticator


# 示例使用
if __name__ == '__main__':
    shared_secret = 'testing123'
    packet_data = b'\x01\x02\x00\x10\x00\x00\x00\x00'  # 示例Radius报文数据

    message_authenticator = generate_message_authenticator(packet_data, shared_secret)
    print('Message-Authenticator:', message_authenticator.hex())
