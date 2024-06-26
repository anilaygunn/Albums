from dotenv import load_dotenv
import os
import base64
from requests import post,get
import json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_str = client_id + ":" + client_secret
    auth_bytes = auth_str.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token



def get_auth_header(token):
    return {"Authorization": "Bearer "+token}

def search_for_users(token,artist_name):
    url= "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query= f"?q={artist_name}&type=artist&limit=2"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result)== 0:
        print("No artists")
        return None
    return json_result[0]


def get_songs_by_artist(token,artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/albums?country=TR"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["items"]

    return json_result
token = get_token()
result= search_for_users(token,"Drake")

artist_id = result["id"]
songs = get_songs_by_artist(token,artist_id)

for i , song in enumerate(songs):
    print(f"{i+1}. {song['name']}")