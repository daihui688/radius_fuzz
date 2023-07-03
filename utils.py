import os
import hmac
import config
import hashlib
import math


def gen_request_authenticator(shared_key=config.SHARED_KEY):
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


