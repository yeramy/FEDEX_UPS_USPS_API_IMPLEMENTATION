import csv
import os
import requests
import json
from datetime import datetime


token = "l79a1e0c07acb84f40b77c72302f43ac1f"
def getBearerAuthorization():
    url = "https://apis-sandbox.fedex.com/oauth/token"

    key = "4dba4d248d0b4b3d8be0e20c1a7d011a"

    payload = 'grant_type=client_credentials&client_id=l79a1e0c07acb84f40b77c72302f43ac1f&client_secret=' + key
    headers = {
        'Content-Type': "application/x-www-form-urlencoded"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    return response.json()['access_token']

def trackPackage(tackingNum):

    #Get Token for Authorization of API calls
    auth = getBearerAuthorization()

    #URL for API Calls
    url = "https://apis-sandbox.fedex.com/track/v1/trackingnumbers"

    # Required Header Input
    headers = {
        'content-Type': "application/json",
        'authorization': "Bearer " + auth
    }
    payload = '{ "trackingInfo": [ { "trackingNumberInfo": { "trackingNumber": "' + tackingNum + '" } } ], "includeDetailedScans": true }'

    #Post call and save to res
    res = requests.post(url, data=payload, headers=headers).json()

    #Disregard unnecessary info
    scanEvent = res['output']['completeTrackResults'][0]['trackResults'][0]['scanEvents']
    print('Tracking number : ', tackingNum)
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



trackPackage(input("Please Enter Tracking Number : "))

def createShipment():
    accountNum = ''
    pickupType = ''
    serviceType = ''
    packageType = ''
    shipperInfo = ''
    recipientInfo = ''
    payerInfo = ''
    weight = ''
    labelSpec = ''

    return None


