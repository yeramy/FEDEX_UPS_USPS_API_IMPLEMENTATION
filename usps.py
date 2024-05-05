import dotenv
import requests
from dotenv import load_dotenv
import os

dotenv.load_dotenv()
user_id = os.getenv('usps_id')
user_pass = os.getenv('usps_pass')

def getToken():
    url = 'https://api.usps.com/oauth2/v3/token'

    data = {
        "grant_type": "client_credentials",
        "client_id": user_id,
        "client_secret": user_pass
        }
    response = requests.post(url,data).json()
    print(response['access_token'])
    return response['access_token']


def trackPackage():
    trakingNumber = '92612903261227000016785568'

    url = 'https://api.usps.com/tracking/v3/tracking/' + trakingNumber
    token = getToken()
    header = {
        'Authorization': "Bearer " + token,
    }

    response = requests.get(url, headers=header).json()

    print(trakingNumber)
    print(response)
    for i in response['eventSummaries']:
        print(i)



    return None

trackPackage()