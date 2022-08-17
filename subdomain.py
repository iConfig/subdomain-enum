
import requests
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--domain','-d', type=str, help="Provide a domain name ")
args= parser.parse_args()

Domain = args.domain

list = open('domainlist.txt')
file_content = list.read()
subdomains = file_content.splitlines()
for subdomain in subdomains:
    if Domain:
        try:
            url = f"http://{subdomain}.{Domain}"
            connect = requests.get(url)
            connection_code = connect.status_code
            connection_code_str = str(connection_code)
            if connection_code_str.startswith('2'):
                print("[Live Subdomain Found ] " + url )
                with open('live.txt','a') as live:
                    live.write(url + '\n')
                    live.close()
            elif connection_code_str.startswith('5'):
                print("[Filtered Subdomain Found ] " + url )
                with open('500_code.txt','a') as internal_error:
                    internal_error.write(url + '\n' )
                    internaL_error.close()
            else:
                pass
        except KeyboardInterrupt:
            print("Session Interrupted with a key")
            sys.exit()
        except requests.ConnectionError:
            pass
    else:
        print("You must enter a domain name ")
print("Scanning Completed")
    
            




    






    

