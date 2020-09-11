import requests;
import json;


HEADER = {
    "Authorization": "Bearer BQC4d_fB_7ZkM2ELNCcGcGvXyJvbRO9hWwefAgEKmWUKqaxzPgABq5XRHC36knBoZotcdiIv65vEdOgVg4sF7SB4XY8QDPJQLLmS6nexHtEn2qQ84B6GoYckEwIkZToXR-5xeumQJ0w_d2avJ5Pq4iZYsd8QnPPg5CwQEw"
}

r = requests.get(url="https://api.spotify.com/v1/me/top/artists", headers=HEADER)
top_artists_albums = r.json()

print(top_artists_albums[0]['external_urls']['followers']['name'])
        