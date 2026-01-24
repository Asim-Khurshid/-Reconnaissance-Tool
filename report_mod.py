import os, json
from datetime import datetime

def generate(domain,data,fmt):
 os.makedirs('reports',exist_ok=True)
 ts=str(datetime.utcnow())
 if fmt in ('txt','all'):
  open(f'reports/{domain}.txt','w').write(str(data))
 if fmt in ('json','all'):
  json.dump(data,open(f'reports/{domain}.json','w'),indent=2,default=str)
 if fmt in ('html','all'):
  with open(f'reports/{domain}.html','w') as f:
   f.write(f'<h1>Recon Report {domain}</h1><p>{ts}</p><pre>{data}</pre>')
 print('[+] Report generated')
