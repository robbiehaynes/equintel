import requests
import re
from datetime import datetime
from typing import Dict, Any, Optional

def fetch_from_api(url: str, username: str, password: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
  """
  Fetch data from an API using basic authentication.
  
  Args:
    url: The API endpoint URL
    username: Username for basic authentication
    password: Password for basic authentication
    params: Optional query parameters as a dictionary
    
  Returns:
    Dictionary containing the API response data
    
  Raises:
    requests.exceptions.RequestException: If the request fails
  """
  # Set up the authentication
  auth = (username, password)
  
  # Make the request
  response = requests.get(url, auth=auth, params=params)
  
  # Raise an exception if the request was unsuccessful
  response.raise_for_status()
  
  # Parse and return the JSON response
  return process_racecards(response.json())


def process_racecards(data: Dict[str, Any]) -> Dict[str, Any]:
  """
  Process racecard data to extract relevant information.
  
  Args:
    data: Dictionary containing racecard data
    
  Returns:
    Processed dictionary with relevant racecard information
  """
  processed_data = {}

  for racecard in data.get('racecards', []):
    # Extract the racecard ID to use as key
    racecard_id = racecard.get('_id')
    racecard_id = int(racecard_id)
      
    # Create a copy of the racecard data
    racecard_copy = racecard.copy()
      
    # Remove unnecessary fields
    del racecard_copy['_id']
    del racecard_copy['date']
    del racecard_copy['distance']
    del racecard_copy['distance_round']
    del racecard_copy['off_time']
    del racecard_copy['pattern']
    del racecard_copy['prize']
    del racecard_copy['rail_movements']
    del racecard_copy['sex_restriction']
    del racecard_copy['stalls']
    del racecard_copy['betting_forecast']
    del racecard_copy['verdict']
    racecard_copy['runners'] = []

    # Convert fields to appropriate types
    racecard_copy["off_dt"] = datetime.fromisoformat(racecard_copy["off_dt"]).timestamp()
    racecard_copy["distance_f"] = float(racecard_copy["distance_f"])
    racecard_copy["field_size"] = int(racecard_copy["field_size"])
    racecard_copy["race_class"] = int(re.search(r'Class\s+(\d+)', racecard_copy["race_class"]).group(1)) if re.search(r'Class\s+(\d+)', racecard_copy["race_class"]) else 0
    # Extract the number from the jumps field if it exists
    if racecard_copy["jumps"]:
      jumps_match = re.search(r'^(\d+)', racecard_copy["jumps"])
      racecard_copy["jumps"] = int(jumps_match.group(1)) if jumps_match else 0
    else:
      racecard_copy["jumps"] = 0
      
    # Add to processed data
    processed_data[racecard_id] = racecard_copy

  return processed_data