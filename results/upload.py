import pandas as pd
from supabase_funcs.upload import upload_df_to_supabase
import sys
sys.path.append('../')

df = pd.read_pickle("output/results.pkl")
upload_df_to_supabase(df, "results")