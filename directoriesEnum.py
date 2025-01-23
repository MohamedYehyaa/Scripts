import requests
import sys
dir=open('wordlist2.txt').read()
dir_list=dir.splitlines()
for d in dir_list:
  r=f"http://{sys.argv[1]}/{d}.html"
  r_status=requests.get(r)
  if r_status.status_code==404:
    pass
  else:
    print("valid"+r)
