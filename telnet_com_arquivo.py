#!/usr/bin/python
import getpass
import telnetlib
import time

HOST = "xxx"
user = "xxx"
password = "xxx"

arquivo = open('comandos.txt', 'r')

tn = telnetlib.Telnet(HOST, 23, 20)

tn.write(user.encode('ascii') + b"\n")
tn.write(password.encode('ascii') + b"\n")
tn.write(b"\n")

for line in arquivo:
  tn.write(line)
  time.sleep(1)
  tn.write(b"\r\n")
  time.sleep(3)

exit = tn.read_very_eager()

arquivo.close()

print (exit)

arquivo_saida = open('log.txt', 'w')
arquivo_saida.write(exit)
arquivo_saida.close()
