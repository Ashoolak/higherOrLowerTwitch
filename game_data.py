import requests

client_id = 'Enter your api id'
client_secret = 'Enter your api secret'
streamers = {'KINGSLEAGUE': 0, 'XQC': 0, 'ESL_CSGO': 0, 'AURONPLAY': 0, 'GAULES': 0, 'IBAI': 0, 'PAULINHOLOKOBR': 0,
             'KAICENAT': 0, 'ELSPREEN': 0, 'LOUD_CORINGA': 0, 'LOLTYLER1': 0, 'BRUCEDROPEMOFF': 0, 'Ninja': 0,
             'Tfue': 0, 'TheGrefg': 0, 'shroud': 0, 'pokimane': 0, 'tommyinnit': 0, 'Dream': 0,
             'SypherPK': 0, 'Bugha': 0, 'Dakotaz': 0, 'Philza': 0, 'Squeezie': 0, 'juansguarnizo': 0, 'Myth': 0,
             'NICKMERCS': 0, 'AMOURANTH': 0, 'alanzoka': 0, 'WilburSoot': 0, 'RanbooLive': 0, 'NickEh30': 0}

# Get OAuth token
oauth_url = 'https://id.twitch.tv/oauth2/token'
oauth_payload = {
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'client_credentials',
}
oauth_response = requests.post(oauth_url, data=oauth_payload)
access_token = oauth_response.json()['access_token']

# Get user ID
headers = {
    'Client-ID': client_id,
    'Authorization': f'Bearer {access_token}',
}
for streamer in streamers.keys():
    user_url = f'https://api.twitch.tv/helix/users?login={streamer}'
    user_response = requests.get(user_url, headers=headers)
    data = user_response.json()['data']
    if not data:
        print(f"No user data found for streamer: {streamer}")
        continue

    user_id = data[0]['id']

    # Get follower count
    followers_url = f'https://api.twitch.tv/helix/users/follows?to_id={user_id}'
    followers_response = requests.get(followers_url, headers=headers)
    follower_count = followers_response.json()['total']
    follower_count = (follower_count // 1000) * 1000
    streamers[streamer] = follower_count
