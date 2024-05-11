# Spotify Artist Search & Album Fetch Script
This Python script utilizes the Spotify API to search for artists and retrieve their albums. It employs OAuth authentication with the client credentials flow to obtain an access token for accessing the Spotify API endpoints.

# Code Explanation:
Environment Variables: The script loads the Spotify client ID and client secret from environment variables using the dotenv package.

Token Retrieval (get_token()): This function retrieves the OAuth token required for accessing the Spotify API. It encodes the client ID and client secret using base64 and sends a POST request to the Spotify token endpoint.

Authorization Header (get_auth_header(token)): This function generates the authorization header required for API requests by appending the access token to the string "Bearer ".

Artist Search (search_for_users(token, artist_name)): Searches for artists on Spotify by name using the provided access token. It constructs the API request URL with the artist name and sends a GET request. It returns the information of the first artist found.

Album Retrieval (get_songs_by_artist(token, artist_id)): Retrieves the albums of a specific artist using their ID. It constructs the API request URL with the artist ID and sends a GET request. It returns a list of albums by the artist.

Output: Finally, the script prints the names of the albums retrieved for the artist "Drake" to the console.

# Usage:
Setup Environment:

Set your Spotify CLIENT_ID and CLIENT_SECRET as environment variables.
Install required Python packages using pip install python-dotenv requests.
Run the Script:

Modify the search_for_users() function call with the desired artist name.
Execute the script to see the albums of the specified artist printed to the console.
Note:
This script is provided for educational purposes only and should be used responsibly and in accordance with the Spotify API terms of service.
