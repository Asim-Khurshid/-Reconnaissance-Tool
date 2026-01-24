import dns.resolver

def run(domain):
 d={}
 for r in ['A','MX','NS','TXT']:
  try: d[r]=[str(x) for x in dns.resolver.resolve(domain,r)]
  except: d[r]=[]
 return d
