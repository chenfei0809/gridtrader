import base64
from pyDes import *

def Encode(str,key='ilovejin',iv='*xiaoqi*'):
    k = des(key,iv, padmode=PAD_PKCS5)
    return base64.b64encode(k.encrypt(str))
 
# 解密
def Decode(str,key='ilovejin',iv='*xiaoqi*'):
    k = des(key, iv, padmode=PAD_PKCS5)
    return k.decrypt(base64.b64decode(str))