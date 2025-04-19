import time
import requests
import json
import os
from pprint import pprint

SPOTIFY_ACCESS_TOKEN = 'BQDE-PAyV1VJOOWcbPdICoFEgRVql9jx6_EN3ae08Qz3ztAUb-ZUTD_7kje7TAWTnKyujwZDz9384ao962xjR6DI34ZI_3NnHx8bMPIJXO8yBkzAVKAeJnL0eL0yKh9vdMIlWhJToje33Ngh9KPexDutvbCRLzdQcGZY5YF3kQ98yh2GKEzSQCSrfyVIlFb1t32kkYhuRqr61f0MxxjdXo5FaZaFA-yP5uzVY_1KWLLJsI4'
SPOTIFY_GET_RECENTLY_PLAYED_URL = 'https://api.spotify.com/v1/me/player/recently-played?limit=1'

def get_current_track(access_token):
    response = requests.get(
        SPOTIFY_GET_RECENTLY_PLAYED_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    print("STATUS:", response.status_code)
    resp_json = response.json()

    if 'items' not in resp_json or not resp_json['items']:
        print("No recent tracks found.")
        return None

    item = resp_json['items'][0]['track']

    return {
        "id": item['id'],
        "name": item['name'],
        "artists": ', '.join([artist['name'] for artist in item['artists']]),
        "link": item['external_urls']['spotify']
    }

def save_to_json(data):
    output_path = os.path.join(os.path.dirname(__file__), '../public/data/spotify.json')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"✅ Saved to {output_path}\n")

def main():
    while True:
        print("🔁 Refreshing current track...")
        track = get_current_track(SPOTIFY_ACCESS_TOKEN)
        if track:
            pprint(track)
            save_to_json(track)
        else:
            print("No track found or error.")

        # Wait 3 minutes (180 seconds)
        time.sleep(180)

if __name__ == '__main__':
    main()
