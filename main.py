import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv('API_URL')
API_KEY = os.getenv('API_KEY')

mac_address = input("Enter a MAC address: ")

clean_mac_address = ''.join(c for c in mac_address if c.isalnum() or c in ["."])

return_type = input("Select return type:\n1. vendor (default)\n2. xml\n3. csv\n4. txt\nEnter your choice (1-4): ")
return_type_options = {
    '1': 'vendor',
    '2': 'xml',
    '3': 'csv',
    '4': 'txt'
}
selected_return_type = return_type_options.get(return_type, 'vendor')

params = {
    'apiKey': API_KEY,
    'output': selected_return_type,
    'search': clean_mac_address
}

response = requests.get(API_URL, params=params)

if response.status_code == 200:
    if selected_return_type == 'vendor':
        print(response.text)
    else:
        with open(f'mac-address.{selected_return_type}', 'a') as f:
            f.write(response.raw)
else:
    print(f"{response.status_code}:: Error occurred while making the request.")
