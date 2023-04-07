#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 06:55:07 2023

@author: britney
"""

## Pop Genre 

from dotenv import load_dotenv
import os
import base64
import requests 
from requests import post, get
import json
import pandas as pd

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = requests.post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


def get_top_artists(token):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    params = {
        "q": "genre:pop",
        "type": "artist",
        "limit": 50
    }
    result = requests.get(url, headers=headers, params=params)
    json_result = json.loads(result.content)["artists"]["items"]
    artists = []
    for artist in json_result:
        artist_id = artist["id"]
        artist_name = artist["name"]
        artist_genres = artist["genres"]
        
        # Get the number of followers for the artist
        url = f"https://api.spotify.com/v1/artists/{artist_id}"
        result = requests.get(url, headers=headers)
        json_result = json.loads(result.content)
        artist_followers = json_result["followers"]["total"]
        
        artists.append({
            "id": artist_id,
            "name": artist_name,
            "genres": artist_genres,
            "followers": artist_followers
        })
    return artists


def get_top_tracks(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks"
    headers = get_auth_header(token)
    params = {"country": "US"}
    result = requests.get(url, headers=headers, params=params)
    json_result = json.loads(result.content)
    tracks = []
    for track in json_result["tracks"]:
        track_info = {
            "id": track["id"],
            "name": track["name"],
            "popularity": track["popularity"],
            "release_date": track["album"]["release_date"],
            "duration": track["duration_ms"]/1000, 
            "track_genre": "pop" # Add the track_genre variable with the value of "pop"
        }
        tracks.append(track_info)
    return tracks



def get_track_features(token, track_id):
    url = f"https://api.spotify.com/v1/audio-features/{track_id}"
    headers = get_auth_header(token)
    result = requests.get(url, headers=headers)
    json_result = json.loads(result.content)
    features = {
        "acousticness": json_result["acousticness"],
        "danceability": json_result["danceability"],
        "energy": json_result["energy"],
        "instrumentalness": json_result["instrumentalness"],
        "key": json_result["key"],
        "liveness": json_result["liveness"],
        "loudness": json_result["loudness"],
        "mode": json_result["mode"],
        "speechiness": json_result["speechiness"],
        "tempo": json_result["tempo"],
        "time_signature": json_result["time_signature"],
        "valence": json_result["valence"]
    }
    return features


token = get_token()
top_artists = get_top_artists(token)

data = []
for idx, artist in enumerate(top_artists):
    print(f"{idx + 1}. {artist['name']}")
    top_tracks = get_top_tracks(token, artist["id"])
    for track in top_tracks:
        track_features = get_track_features(token, track["id"])
        data.append({
            "artist_name": artist["name"],
            "track_name": track["name"],
            "genres": artist["genres"],
            "followers": artist["followers"],
            "popularity": track["popularity"], 
            "duration": track["duration"],
            "release_date": track["release_date"],
            "danceability": track_features["danceability"],
            "energy": track_features["energy"],
            "speechiness": track_features["speechiness"],
            "acousticness": track_features["acousticness"],
            "instrumentalness": track_features["instrumentalness"],
            "liveness": track_features["liveness"],
            "valence": track_features["valence"],
            "tempo": track_features["tempo"], 
            "track_genre": track["track_genre"] # Include the "track_genre" variable
        })

pop = pd.DataFrame(data)
print(pop)

pop.to_csv('pop_data.csv', index=False)


