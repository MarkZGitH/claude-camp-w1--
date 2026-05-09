# 简单密码生成器
import random
import string

length = int(input("请输入密码长度: "))

characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(characters) for _ in range(length))

print(f"生成的密码: {password}")