import json
import requests


SPOTIFY_API_BASE_URL = 'https://api.spotify.com'
API_VERSION = "v1"
SPOTIFY_API_URL = f"{SPOTIFY_API_BASE_URL}/{API_VERSION}"

try:
    import urllib.request
    import urllib.error
    import urllib.parse as urllibparse
except ImportError:
    import urllib as urllibparse

# ----------------- 1. USER AUTHORIZATION ----------------

# spotify endpoints
SPOTIFY_AUTH_BASE_URL = "https://accounts.spotify.com/{}"
SPOTIFY_AUTH_URL = SPOTIFY_AUTH_BASE_URL.format('authorize')
SPOTIFY_TOKEN_URL = SPOTIFY_AUTH_BASE_URL.format('api/token')

# client keys
with open('config.json') as c:
    config = json.load(c)
CLIENT_ID = config['id']
CLIENT_SECRET = config['secret']

# server side parameter
REDIRECT_URI = 'http://127.0.0.1:5000/callback/'
SCOPE = 'playlist-modify-public user-read-private user-read-email'

auth_query_parameters = {
    "response_type": "code",
    "redirect_uri": REDIRECT_URI,
    "scope": SCOPE,
    "client_id": CLIENT_ID
}

URL_ARGS = "&".join([f"{key}={urllibparse.quote(val)}" for key,
                     val in list(auth_query_parameters.items())])

# ---------------- auth request
AUTH_URL = f"{SPOTIFY_AUTH_URL}/?{URL_ARGS}"


def authorize(auth_token):

    code_payload = {
        "grant_type": "authorization_code",
        "code": str(auth_token),
        "redirect_uri": REDIRECT_URI
    }

    base64encoded = base64.b64encode((f"{CLIENT_ID}:{CLIENT_SECRET}").encode())
    headers = {"Authorization": f"Basic {base64encoded.decode()}"}

    post_request = requests.post(
        SPOTIFY_TOKEN_URL, data=code_payload, headers=headers)

    # tokens are returned to the app
    response_data = json.loads(post_request.text)
    access_token = response_data["access_token"]

    # use the access token to access Spotify API
    auth_header = {"Authorization": "Bearer {}".format(access_token)}
    return auth_header


# ---------------- 2. ME REQUEST ------------------------
ME = f'{SPOTIFY_API_URL}/me'


def get_username(auth_header):
    resp = requests.get(ME, headers=auth_header)
    return resp.json()['id']


# ---------------- 3. CREATE PLAYLIST REQUEST ------------------------
CREATE_PLAYLIST = f'{SPOTIFY_API_URL}/users'


def create_playlist(auth_header, country):
    title = "Weltfy: Top local tracks from " + country
    username = get_username(auth_header)
    url = f'{CREATE_PLAYLIST}/{username}/playlists'
    request_body = json.dumps({"name": title})
    resp = requests.post(url, request_body, headers=auth_header)
    return resp.json()['id']


# ---------------- 4. FILL PLAYLIST REQUEST ------------------------
FILL_PLAYLIST = f'{SPOTIFY_API_URL}/playlists'


def fill_playlist(track_list, id, auth_header):
    url = f'{FILL_PLAYLIST}/{id}/tracks?uris='
    for index, track in track_list.iterrows():
        url = f"{url}spotify%3Atrack%3A{track_list.at[index, 'URL']}%2C"
    url = url[:len(url)-3]
    resp = requests.post(url, headers=auth_header)
    return resp
