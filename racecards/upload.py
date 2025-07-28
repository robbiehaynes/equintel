import pandas as pd
import os
from supabase import create_client, Client

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def upload_df_to_supabase(df, table_name):
    """
    Upload a DataFrame to a Supabase table.
    
    Args:
        df (pd.DataFrame): The DataFrame to upload.
        table_name (str): The name of the table in Supabase.
    """
    # Convert DataFrame to dictionary format
    data = df.to_dict(orient='records')
    
    # Insert data into the specified table
    try:
        supabase.table(table_name).insert(data).execute()
    except Exception as e:
        raise Exception(f"Error uploading data to {table_name}: {e}")
    
    print(f"Successfully uploaded {len(data)} records to {table_name}.")

df = pd.read_pickle("output/racecards.pkl")
upload_df_to_supabase(df, "racecards")