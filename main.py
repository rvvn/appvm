import requests
import os
import sys

print("test")

#test medium vuln
response = requests.get("http://www.google.com", insecurewarning= false)

#test high vuln
user_input = sys.argv[1]  # Get input from command-line argument
os.system("ls " + user_input)

#test critical vuln
url = input("Enter the URL: ")
response = requests.get(url, verify=False)  # Disables SSL verification
print(response.content)

#test duplicate vuln - same id?
user_input = sys.argv[1]  # Get input from command-line argument
os.system("ls " + user_input)
