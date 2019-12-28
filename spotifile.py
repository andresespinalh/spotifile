import spotipy
import json
import spotipy.util as util

# Fetch application settings from settings.json
spotifile_settings_json = open( 'settings.json', 'r' ).read()
spotifile_settings = json.loads( spotifile_settings_json )

# Parse values from json file
username = spotifile_settings[ 'username' ]
scope = spotifile_settings[ 'scope' ]
client_id = spotifile_settings[ 'client_id' ]
client_secret = spotifile_settings[ 'client_secret' ]
redirect_uri = spotifile_settings[ 'redirect_uri' ]

# Acquire authorization token through user prompt
token = util.prompt_for_user_token( username, scope, client_id, client_secret, redirect_uri )

print( token )