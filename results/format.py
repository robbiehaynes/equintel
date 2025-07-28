import pandas as pd
import json

with open("output/results.json", "r") as f:
    try:
        results_response = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error reading JSON: {e}")
        results_response = {"results": []}

final_results = pd.DataFrame()

for result in results_response['results']:
    results_df = pd.DataFrame([
        {
            'race_id': result['race_id'],
            'horse_id': runner['horse_id'],
            'draw': runner['draw'],
            'position': runner['position']
        }
        for runner in result['runners']
    ])

    results_df['position'] = pd.to_numeric(results_df['position'], errors='coerce')
    results_df['draw'] = pd.to_numeric(results_df['draw'], errors='coerce')

    final_results = pd.concat([final_results, results_df], ignore_index=True)

# Save the final DataFrame to a CSV file
final_results.to_pickle("output/results.pkl")