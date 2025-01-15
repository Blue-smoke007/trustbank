import requests
url = "https://v3.api.termii.com/api/sms/send"
payload = {
          "to": "2348082182438",
           "from": "2348082182438",
           "sms": "Hi there, testing Termii ",
           "type": "plain",
           "channel": "generic",
           "api_key": "TLUTVlsRUDVTkWRfKoBHgeHWwDlulhwFdjFUtpowBZWeZlhYgfDdJIsbWsHhMT",
            
       }
headers = {
'Content-Type': 'application/json',
}
response = requests.request("POST", url, headers=headers, json=payload)
print(response.text)