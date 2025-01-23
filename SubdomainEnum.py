import requests
import sys
subs=open("wordlist2.txt").read()
subs_domains=subs.splitlines()
for sub in subs_domains:
  domain= f"http://{sub}.{sys.argv[1]}"
  
  try:
    requests.get(domain)
  except requests.ConnectionError:
    pass
  else:
    print(domain)
