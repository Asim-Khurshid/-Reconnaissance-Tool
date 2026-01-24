import socket

def run(domain):
 ports=[21,22,23,25,53,80,110,139,143,443,445,3306,3389]
 open_ports=[]
 for p in ports:
  try:
   s=socket.socket(); s.settimeout(0.5)
   s.connect((domain,p)); open_ports.append(p); s.close()
  except: pass
 return open_ports
