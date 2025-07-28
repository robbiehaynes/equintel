import pandas as pd
import json

with open("output/racecards.json", "r") as f:
    try:
        response = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error reading JSON: {e}")
        response = {"racecards": []}

total_df = pd.DataFrame()

for racecard in response["racecards"]:
  racecard_df = pd.DataFrame.from_dict(racecard)

  runners_flat = pd.json_normalize(racecard_df['runners'])
  runners_flat.rename(columns={"region":"horse_region"}, inplace=True)

  df_final = pd.concat([racecard_df.copy().drop(columns=['runners']), runners_flat], axis=1)

  df_final = df_final[[
    'race_id', 'course_id', 'off_dt', 'distance_f',
    'region', 'type', 'age_band', 'field_size', 'weather', 'going',
    'surface', 'big_race', 'is_abandoned', 
    # Plus runner details if merged
    'horse_id', 'horse', 'age', 'sex_code', 'horse_region',
    'dam_id', 'sire_id', 'damsire_id', 'trainer_id', 'owner_id',
    'lbs', 'form', 'jockey_id'
  ]]

  df_final["is_abandoned"] = df_final["is_abandoned"].astype(int)
  df_final["going_soft"] = (df_final["going"].str.lower() == "soft").astype(int)
  df_final["going_good"] = (df_final["going"].str.lower() == "good").astype(int)
  df_final.drop(columns=['going'], inplace=True)

  # Append to the total DataFrame
  total_df = pd.concat([total_df, df_final], ignore_index=True)

# Save the final DataFrame to a CSV file
total_df.to_pickle("output/racecards.pkl")