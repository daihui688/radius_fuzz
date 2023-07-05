import os
import hmac
from typing import Dict

import config
import hashlib
import math
import struct


def gen_access_request_request_authenticator(shared_key=config.SHARED_KEY):
    # 生成随机数作为请求认证字
    request_authenticator = os.urandom(16)

    # 将共享密钥和请求认证字进行组合
    data = shared_key.encode() + request_authenticator

    # 计算 MD5 哈希值
    md5_hash = hashlib.md5(data).digest()

    return md5_hash


def gen_user_password(password: str, request_authenticator: bytes, shared_secret: str = config.SHARED_KEY) -> bytes:
    if len(password) > 128:
        raise ValueError("Password length cannot exceed 128 characters")

    password = password.encode()
    shared_secret = shared_secret.encode()

    # 使用空字节将密码填充为16的倍数
    password_padded = password.ljust(int(math.ceil(len(password) / 16.0) * 16), b'\x00')

    # 初始化结果缓冲区
    user_password = b''

    # 迭代 16 个字节的密码块
    for i in range(0, len(password_padded), 16):
        if i == 0:
            prev_block = request_authenticator
        else:
            prev_block = user_password[i - 16:i]

        # 计算MD5哈希值
        md5_input = shared_secret + prev_block
        md5_hash = hashlib.md5(md5_input).digest()

        # 将密码块与MD5哈希进行异或
        xor_result = bytes(x ^ y for x, y in zip(password_padded[i:i + 16], md5_hash))

        # 将异或结果附加到user_password缓冲区
        user_password += xor_result

    return user_password


def gen_message_authenticator(packet_data, shared_secret=config.SHARED_KEY):
    # 将packet_data和共享密钥进行HMAC-MD5运算
    md5_hash = hmac.new(shared_secret.encode(), packet_data, hashlib.md5).digest()

    # 获取前16个字节作为Message-Authenticator字段
    message_authenticator = md5_hash[:16]

    return message_authenticator


def gen_accounting_request_request_authenticator(code, identifier, length, attributes=b'', shared_secret=config.SHARED_KEY):
    # 创建一个包含 16 个值为 0 的字节的占位符
    placeholder = b'\x00' * 16

    # 将 Code、Identifier 和 Length 转换为字节
    code_bytes = struct.pack('B', code)
    identifier_bytes = struct.pack('B', identifier)
    length_bytes = struct.pack('>H', length)

    # 将所有部分连接在一起
    data = code_bytes + identifier_bytes + length_bytes + placeholder + attributes + shared_secret.encode()

    # 计算 MD5 哈希值
    md5_hash = hashlib.md5(data).digest()

    return md5_hash


def gen_accounting_request_attributes(params: Dict):
    attributes = b''
    for k, v in params.items():
        if k not in ['code', 'identifier', 'authenticator']:
            attributes += v.pack()
    return attributes
