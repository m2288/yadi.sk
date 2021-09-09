#Yandexden fayl yukleme

import sys
import yadisk
id = input("id: ")
psw = input("password: ")
y = yadisk.YaDisk(id, psw)
url = y.get_code_url()

print("Bu linke tikle: %s" % url)
code = input("Tesdiq kodunu daxil et: ")

try:
    response = y.get_token(code)
except yadisk.exceptions.BadRequestError:
    print("Kod yoxlana bilmedi")
    sys.exit(1)

y.token = response.access_token

if y.check_token():
    print("token elde edildi")
    #print(y.token)
else:
    print("Sehv oldu...")
    

print(list(y.listdir("/")))
y.download(input("Yuklenecek fayl"), input("Hansi adla saxlansin"))