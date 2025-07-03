"""
Equintel - AI-powered horse racing prediction system
"""
from racecards import fetch_from_api
from dotenv import load_dotenv
import os
import json

def main():
    """Main entry point for the Equintel application."""
    print("Welcome to Equintel!")
    print("AI-powered horse racing prediction system")

    load_dotenv()  # Load environment variables from .env file

    # Example API call (replace with actual URL and credentials)
    result = fetch_from_api(
        url=os.getenv("API_URL"),
        username=os.getenv("USERNAME"),
        password=os.getenv("PASSWORD"),
        params={"region_codes": "gb"})
    
    # print("API Response:", result)

    with open("racecards.json", "w") as file:
        json.dump(result, file, indent=4)


if __name__ == "__main__":
    main()
