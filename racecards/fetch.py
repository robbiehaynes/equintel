from dotenv import load_dotenv
import os
import requests
import json

# Check if environment is production
if not os.getenv("ENV") == "production":
  load_dotenv()

# Set up the authentication
auth = (os.getenv("API_USER"), os.getenv("API_PASS"))

# Make the request
url = str.join([os.getenv("API_URL"), "/racecards/basic"])
response = requests.get(url, auth=auth, params={"day":"today"})

# Raise an exception if the request was unsuccessful
response.raise_for_status()

with open("output/racecards.json", "w") as f:
    json.dump(response.json(), f, indent=2)