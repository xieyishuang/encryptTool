from Crypto.Cipher import AES
import base64
import time
import binascii
from binascii import a2b_hex

class aes():
    def __init__(self):
        # key值（密码）
        self.key = 'aaaaaaabbbbcccc1'.encode("utf-8")  # 因为在python3中AES传入参数的参数类型存在问题，需要更换为 bytearray , 所以使用encode编码格式将其转为字节格式（linux系统可不用指定编码）
        # vi偏移量
        self.iv = '1365127901262396'.encode("utf-8")  # 编码
        self.mode = AES.MODE_CBC
        self.BS = AES.block_size
        self.pad = lambda s: s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS)
        self.unpad = lambda s: s[0:-ord(s[-1])]


    # 加密
    def encrypt(self, text):
        text = self.pad(text).encode("utf-8")
        cryptor = AES.new(self.key, self.mode, self.iv)
        # 目前AES-128 足够目前使用(CBC加密)
        ciphertext = cryptor.encrypt(text)
        # 十六进制加密
        return binascii.b2a_hex(ciphertext).decode("utf-8")
        # base64加密
        # return base64.b64encode(bytes(ciphertext))

    # 解密
    def decrypt(self, text):
        # base64解密
        # text = base64.b64decode(text)
        # 十六进制解密
        text = binascii.a2b_hex(text)
        cryptor = AES.new(self.key, self.mode, self.iv)
        # CBC解密
        plain_text = cryptor.decrypt(text)
        # 去掉补足的空格用strip() 去掉
        return self.unpad(bytes.decode(plain_text).rstrip('\0'))    # 解密字节？？？
        # return self.unpad(bytes.decode(plain_text).rstrip('\ox20'))    # 解密字节？？？


if __name__ == '__main__':
    pc = aes()  # 初始化密钥 和 iv
    # text='access&a494fcbc-9aa1-4718-bd7d-a90d01211d97&0&2&'
    text = '19904240001'
    # text='access&a494fcbc-9aa1-4718-bd7d-a90d01211d97&1&1&'
    # text='access&a494fcbc-9aa1-4718-bd7d-a90d01211d97&1&2&'
    # text='update&a494fcbc-9aa1-4718-bd7d-a90d01211d97&0&2&'
    # text='update&a494fcbc-9aa1-4718-bd7d-a90d01211d98&0&2&'
    # text='logout&'
    # e = pc.encrypt(text + str(int(time.time() / 10)))  # 加密
    e = pc.encrypt(text)  # 加密
    d = pc.decrypt(e)  # 解密
    print("加密:%s" % e)
    print("解密:%s"% d)
    print("长度:%s"% len(d))