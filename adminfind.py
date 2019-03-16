import sys
import requests
import time
url = sys.argv[1]
arg = open(sys.argv[2], 'r')
lines = arg.readlines()
live = []

arg.close
for line in lines:
    line = line.replace("\n", " ")
    request = url +  "/" + line
    
    http = requests.get(request)
    code = http.status_code
    if code != 301 and code != 404:
	if not "Page not Found" in http.content:
		print("[+] Page Found: " + request)
		print("##############")
	else:
		print("[-] Page Not Found: " + request)
		lives.append(request)
    else:
	print("[-] Page Not Found: " + request)

print("Finish!")
for live in lives:
    print(live)
