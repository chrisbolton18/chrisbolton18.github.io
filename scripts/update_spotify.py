import requests
import json
import os

CLIENT_ID = 'ce362fdaf1ea4fec9153e2d434f795be'
CLIENT_SECRET = 'cb2d5f4adc8240579e6759b22f25c193'
REFRESH_TOKEN = 'AQBtunntXkU-OhCc2jF15i9zHvyuOlOdkG8XWsy2f2uuk2HDb8CE59T7ha-oiPIpBG6L89Y-jzwjaa4mt3uGMnWsnW6jlvEmZFLKoj05xjDM1vJ-OF2VVLCcLt5pjukdZ5c'

def refresh_access_token():
    response = requests.post(
        'https://accounts.spotify.com/api/token',
        data={
            'grant_type': 'refresh_token',
            'refresh_token': REFRESH_TOKEN,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        },
        headers={
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    )

    if response.status_code != 200:
        print("Failed to refresh token:", response.text)
        return None

    return response.json().get('access_token')

def get_latest_track(access_token):
    response = requests.get(
        'https://api.spotify.com/v1/me/player/recently-played?limit=1',
        headers={
            'Authorization': f'Bearer {access_token}'
        }
    )

    if response.status_code != 200:
        print("ailed to get track:", response.text)
        return None

    data = response.json()
    if not data.get('items'):
        print("No recent tracks found.")
        return None

    item = data['items'][0]['track']
    return {
        'id': item['id'],
        'name': item['name'],
        'artists': ', '.join([artist['name'] for artist in item['artists']]),
        'link': item['external_urls']['spotify']
    }

def save_to_json(track_data):
    output_path = os.path.join(os.path.dirname(__file__), '../public/data/spotify.json')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(track_data, f, indent=4)
    print("Saved to:", output_path)

# === MAIN ===
def main():
    access_token = refresh_access_token()
    if not access_token:
        return

    track = get_latest_track(access_token)
    if track:
        save_to_json(track)

if __name__ == '__main__':
    main()
