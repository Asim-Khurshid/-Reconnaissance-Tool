import requests

def run(domain):
 try: return dict(requests.get('http://'+domain,timeout=5).headers)
 except: return {}
