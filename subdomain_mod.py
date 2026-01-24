import requests

def run(domain):
 url=f'https://crt.sh/?q=%25.{domain}&output=json'
 subs=set()
 try:
  r=requests.get(url,timeout=15)
  if r.status_code==200:
   for e in r.json(): subs.add(e['name_value'])
 except: pass
 return list(subs)
