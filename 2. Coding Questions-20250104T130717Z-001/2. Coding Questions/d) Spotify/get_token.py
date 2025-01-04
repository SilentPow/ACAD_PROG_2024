import requests
import json
import base64

CLIENT_ID = "06402034d0c144db97d7607d36a0fbf5"
CLIENT_SECRET = "202f88b2ede248bda33ca45fc2e72526"

def get_token():
   auth_string = CLIENT_ID + ":" + CLIENT_SECRET 
   auth_bytes = auth_string.encode("utf-8")
   auth_base64 = str(base64.b64encode(auth_bytes),"utf-8" )
   url= "https://accounts.spotify.com/api/token"
  
   headers = {
    "Authorization": "Basic " + auth_base64,
    "Content-Type": "application/x-www-form-urlencoded" 
    }
   data = {"grant_type": "client_credentials"}
   result = requests.post(url, headers=headers,data=data)
   json_result = json.loads(result.content) 
   token= json_result["access_token"]
   return token

def get_playlist(token):
    url = "https://api.spotify.com/v1/playlists/6TJ3H6q18yht8ae1Buai9U?market=CA"
    result = requests.get(url, headers=get_auth_token(token))

    with open('result.json', 'w') as f:
        json.dump(result.json(), f)
    return result

def get_auth_token(token):
    return {"Authorization": "Bearer " + token}

# def get_genres(file, token):
#     with open(file, 'r') as file:
#         data = json.load(file)
#         cnt = 0
#         for track in data["tracks"]["items"]:
#             if cnt  < 10:
#                 print(track["track"]["artists"][0]["external_urls"])
#                 url = "https://open.spotify.com/artist/27VhXJzIph9c75cBh1e8XM"
#                 result = requests.get(url, headers=get_auth_token(token))
#                 print(result)
#                 cnt+=1
  
token = get_token()


#print(token)
get_playlist(token)