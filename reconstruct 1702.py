import pandas as pd

# Load the data and force all column names to lowercase immediately
df = pd.read_csv('target_stars_data.csv')
df.columns = map(str.lower, df.columns)

years_to_rewind = 2026 - 1702 

def backpropagate():
    print(f"🕰️ Rewinding stellar positions by {years_to_rewind} years...")
    
    # Using lowercase names now to match our 'map' above
    df['ra_1702'] = df['ra'] - (df['pmra'] / 3600000 * years_to_rewind)
    df['dec_1702'] = df['dec'] - (df['pmdec'] / 3600000 * years_to_rewind)
    
    # Calculate total drift
    df['drift_arcsec'] = ((df['pmra']**2 + df['pmdec']**2)**0.5) * years_to_rewind / 1000
    
    # Save the updated dataset
    df.to_csv('stars_position_1702.csv', index=False)
    
    print("✨ Reconstruction complete.")
    # Check if we have source_id or just use index
    id_col = 'source_id' if 'source_id' in df.columns else df.columns[0]
    
    for index, row in df.head(10).iterrows():
        print(f"Star {row[id_col]}: Drifted {row['drift_arcsec']:.2f} arcseconds.")

if __name__ == "__main__":
    backpropagate()