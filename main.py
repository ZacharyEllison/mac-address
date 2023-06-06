import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Get API URL and API Key from environment variables
API_URL = os.getenv('API_URL')
API_KEY = os.getenv('API_KEY')

mac_address = input("Enter a MAC address: ")

# Clean the MAC address input by removing non-alphanumeric characters
clean_mac_address = ''.join(c for c in mac_address if c.isalnum() or c in ["."])

# Prompt the user for the return type option
return_type = input("Select return type:\n1. vendor (default)\n2. xml\n3. csv\n4. txt\nEnter your choice (1-4): ")
return_type_options = {
    '1': 'vendor',
    '2': 'xml',
    '3': 'csv',
    '4': 'txt'
}
selected_return_type = return_type_options.get(return_type, 'vendor')

# Prepare the parameters for the GET request
params = {
    'apiKey': API_KEY,
    'output': selected_return_type,
    'search': clean_mac_address
}

# Make the GET request
response = requests.get(API_URL, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Print the response content
    if selected_return_type == 'vendor':
        print(response.text)
    else:
        with open(f'mac-address.{selected_return_type}', 'a') as f:
            f.write(response.raw)
else:
    print(f"{response.status_code}:: Error occurred while making the request.")
