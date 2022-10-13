"""
现有一个字符串,该字符串为加密后的一个密码,
具体情况如下:
●该字符串是: "ixo678"，其中o是字母
●现猜测其加密码规则是:在其ASCII码的值上再加了5
●现要求将该字符串进行解密，得到真正的密码
解密前需了解ord函数和chr函数
"""
password = "ixo678"
psw_true = ""
for p in range(len(password)):
    psw_true += chr(ord(password[p]) - 5)
print("真正的密码是："+psw_true)

