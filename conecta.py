
#!/usr/bin/python

import socket

ip = int(input("Digite o ip "))
porta = int(input("Digite a porta "))

meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if meusocket.connect_ex((ip, porta)):
	print "porta fechada"
else:
	print "porta aberta"


