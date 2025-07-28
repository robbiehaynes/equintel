from dotenv import load_dotenv
import os
import requests
import json

# Check if environment is production
if not os.getenv("ENV") == "production":
  load_dotenv()

# Set up the authentication
auth = (os.getenv("USERNAME"), os.getenv("PASSWORD"))

# Make the request
response = requests.get(os.getenv("API_RES_URL"), auth=auth)

# Raise an exception if the request was unsuccessful
response.raise_for_status()

with open("output/results.json", "w") as f:
    json.dump(response.json(), f, indent=2)

# Save data to Supabase
