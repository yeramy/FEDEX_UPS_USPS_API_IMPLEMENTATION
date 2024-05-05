import os
from dotenv import load_dotenv

import requests
import json
from datetime import datetime
def getBearerAuthorizationTracking():
    url = "https://apis-sandbox.fedex.com/oauth/token"

    load_dotenv()

    id = os.getenv('fedex_client_id_tracking')
    key = os.getenv('fedex_client_secret_tracking')

    payload = 'grant_type=client_credentials&client_id=' + id + '&client_secret=' + key
    headers = {
        'Content-Type': "application/x-www-form-urlencoded"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    return response.json()['access_token']
def getBearerAuthorizationShipping():
    url = "https://apis-sandbox.fedex.com/oauth/token"

    load_dotenv()

    id = os.getenv('fedex_client_id_shipping')
    key = os.getenv('fedex_client_secret_shipping')

    payload = 'grant_type=client_credentials&client_id=l7bfa46a244ae54a378d86092b207f92b7&client_secret=' + key
    headers = {
        'Content-Type': "application/x-www-form-urlencoded"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    return response.json()['access_token']
def trackPackage(tackingNum):

    #Get Token for Authorization of API calls
    auth = getBearerAuthorizationTracking()

    #URL for API Calls
    url = "https://apis-sandbox.fedex.com/track/v1/trackingnumbers"

    # Required Header Input
    headers = {
        'content-Type': "application/json",
        'authorization': "Bearer " + auth
    }


    testTrackingNum = '231300687629630'
    payload = '{ "trackingInfo": [ { "trackingNumberInfo": { "trackingNumber": "' + testTrackingNum + '" } } ], "includeDetailedScans": true }'

    #Post call and save to res
    res = requests.post(url, data=payload, headers=headers).json()

    #Disregard unnecessary info
    scanEvent = res['output']['completeTrackResults'][0]['trackResults'][0]['scanEvents']
    print()

    for i in scanEvent :
        # Readable date, time format
        date = i['date'].replace('T', ' ')[0:-6]
        print(date)

        print(i['eventDescription'])
        # When Order is created, It does not contain city key and value pair on JSON object
        if i['eventType'] != 'OC':
            print(i['scanLocation']['city'],',',i['scanLocation']['stateOrProvinceCode'])

        print(i['derivedStatus'])
        print()
    return None




def createShipment():

    auth = getBearerAuthorizationShipping()
    headers = {
        'content-Type': "application/json",
        'authorization': "Bearer " + auth
    }
    url = "https://apis-sandbox.fedex.com/ship/v1/shipments"

    #payload = '{ "requestedShipment": { "shipper": { "address" : "746 S Burlington Ave, APT#123", ""} } }'

    payload = json.dumps(json.load(open('shipment_payload.json')))
    res = requests.post(url, data=payload, headers=headers).json()
    print(res)
    print(res['output'])

    print()
    return None

#trackPackage(input("Please Enter Tracking Number : "))
trackPackage("")


