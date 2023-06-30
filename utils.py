import secrets
import hashlib


def gen_request_authenticator(shared_key='testing123'):
    # 生成随机数
    random_bytes = secrets.token_bytes(16)

    # 将密钥与随机数进行组合
    data = shared_key.encode() + random_bytes

    # 计算 MD5 哈希值
    md5_hash = hashlib.md5(data).hexdigest()

    authenticator_bytes = bytes.fromhex(md5_hash)

    return authenticator_bytes


def gen_user_password(password, shared_key='testing123', request_authenticator=gen_request_authenticator()):
    chunks = [password[i:i + 16] for i in range(0, len(password), 16)]
    chunks[-1] = chunks[-1].encode() + b'\x00' * (16 - len(chunks[-1]))

    intermediate_values = []

    for chunk in chunks:
        data = shared_key.encode() + request_authenticator + chunk
        intermediate_value = hashlib.md5(data).digest()
        intermediate_values.append(intermediate_value)

    user_password = b''

    for i in range(len(chunks)):
        user_password += bytes([a ^ b for a, b in zip(chunks[i], intermediate_values[i])])

    return user_password


