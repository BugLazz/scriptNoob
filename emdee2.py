import requests
import sys
import hashlib
import re

if len(sys.argv) < 2:
    print("usage: {} [port]".format(sys.argv[0]))
    exit(1)
    pass

URI = "http://docker.hackthebox.eu:{}".format(sys.argv[1])

r = requests.session()
data = r.get(URI).text
txt = re.findall(r"(?:<h3 align='center'>)(.+)(?:</h3)", data)[0]
md5 = hashlib.md5(txt.encode()).hexdigest()

data = r.post(URI, data={"hash": md5}).text
flag = re.findall(r"HTB\{.+\}", data)[0]
print(flag)
