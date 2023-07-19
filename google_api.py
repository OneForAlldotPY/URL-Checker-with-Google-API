from coloring import color_text
import requests
import json
import re

class GoogleClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = 'https://safebrowsing.googleapis.com/v4/threatMatches:find'

    def check_website_reputation(self, website_url):
        payload = {
            'client': {
                'clientId': 'your-client-id',
                'clientVersion': '1.0.0'
            },
            'threatInfo': {
                'threatTypes': ['MALWARE', 'SOCIAL_ENGINEERING'],
                'platformTypes': ['ANY_PLATFORM'],
                'threatEntryTypes': ['URL'],
                'threatEntries': [{'url': website_url}]
            }
        }

        headers = {
            'Content-Type': 'application/json',
        }

        params = {
            'key': self.api_key
        }

        try:
            response = requests.post(self.api_url, headers=headers, params=params, json=payload)
            if response.status_code == 200:
                # The API key is valid, process the response data as per your requirements
                response_data = json.loads(response.text)
                return response_data
            else:
                print('Invalid API Key. Please insert a valid key.')
                return None

        except requests.exceptions.RequestException as e:
            print('Error occurred during API request:', e)
            return None

def is_valid_url(url):
    regex = re.compile(
        r'^(https?://)?(www\.)?([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,})(/[a-zA-Z0-9.-]*)*$'
    )
    return regex.match(url)

def get_final_status_code(url):
    try:
        response = requests.get(url, allow_redirects=True)
        final_url = response.url
        final_status_code = response.status_code

        if response.is_redirect:
            print(f"Redirected to: {final_url}")

        return final_status_code
    except requests.exceptions.RequestException:
        return None

def main():
    # Get the user's Google API key
    while True:
        api_key = input("Enter your Google API key: ")
        client = GoogleClient(api_key)
        test_reputation_data = client.check_website_reputation('http://testsafebrowsing.appspot.com/s/malware.html')
        if test_reputation_data is not None:
            print("Key successfully validated.")
            break
        else:
            print("Invalid API Key. Please insert a valid key.")

    # Get the website URL from the user and validate it
    while True:
        website_url = input("Enter the website URL you want to check: ")

        if not is_valid_url(website_url):
            print("Please insert a valid URL.")
        else:
            final_status_code = get_final_status_code(website_url)
            if final_status_code is not None and final_status_code == 200:
                break
            else:
                print(color_text(f"Website returned status code: {final_status_code}", 'yellow'))
    # Check the website reputation using the Google API
    reputation_data = client.check_website_reputation(website_url)

    if reputation_data is None:
        print('An error occurred during reputation check.')
    else:
        matches = reputation_data.get('matches', [])
        if matches:
            for match in matches:
                threat_type = match.get('threatType')
                platform_type = match.get('platformType')
                threat_entry_type = match.get('threatEntryType')
                print('Threat Type:', color_text(threat_type, 'red'))
                print('Platform Type:', color_text(platform_type, 'red'))
                print('Threat Entry Type:', color_text(threat_entry_type, 'red'))
                print('---')
        else:
            print('The website seems safe.')

#if __name__ == "__main__":
   # main()