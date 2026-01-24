import socket

def run(domain):
 b={}
 for p in [80,443]:
  try:
   s=socket.socket(); s.settimeout(1)
   s.connect((domain,p)); s.send(b'HEAD / HTTP/1.1\r\nHost:'+domain.encode()+b'\r\n\r\n')
   b[p]=s.recv(512).decode(errors='ignore'); s.close()
  except: b[p]='N/A'
 return b
