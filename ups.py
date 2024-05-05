import requests
import os
from dotenv import load_dotenv


load_dotenv()

url = "https://onlinetools.ups.com/security/v1/oauth/token"
client_id = os.getenv('ups_id')
client_pass = os.getenv('ups_pass')

def getToken():

  payload = {
    "grant_type": "client_credentials"
  }

  headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "x-merchant-id": "string"
  }

  response = requests.post(url, data=payload, headers=headers, auth=(client_id,client_pass))
  data = response.json()

  return data['access_token']

def trackshipment():

  token = getToken()
  inquiry_number = "1Z1202R66698804005"
  url = "https://onlinetools.ups.com/api/track/v1/details/" + inquiry_number

  query = {
    "locale": "en_US",
    "returnSignature": "false",
    "returnMilestones": "false",
    "returnPOD": "false"
  }

  headers = {
    "transId": "string",
    "transactionSrc": "testing",
    "Authorization": "Bearer " + token
  }

  response = requests.get(url, headers=headers, params=query)

  data = response.json()
  print(data)

trackshipment()