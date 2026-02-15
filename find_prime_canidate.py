import pandas as pd

# 1. Load the reconstructed data
df = pd.read_csv('stars_position_1702.csv')

# 2. Define the 'Bullseye' (Center of the Wow! Signal)
WOW_RA = 290.5
WOW_DEC = -27.0

def find_winner():
    print("🔍 Analyzing 1702 coordinates for the best match...")
    
    # Calculate how far each star was from the center of the signal in 1702
    df['distance_from_wow'] = ((df['ra_1702'] - WOW_RA)**2 + (df['dec_1702'] - WOW_DEC)**2)**0.5
    
    # Sort by the closest match
    winners = df.sort_values('distance_from_wow').head(3)
    
    print("\n--- TOP 3 CANDIDATES FOR PROJECT SAGITTARIUS ---")
    for i, (idx, row) in enumerate(winners.iterrows(), 1):
        print(f"\n{i}. STAR ID: {int(row['source_id'])}")
        print(f"   Distance from Bullseye in 1702: {row['distance_from_wow']:.4f} degrees")
        print(f"   Total Drift since 1702: {row['drift_arcsec']:.2f} arcseconds")
        print(f"   Estimated Distance: {1000/row['parallax']:.1f} light-years")

    # Save the top hits to a new file for your paper
    winners.to_csv('prime_candidates.csv', index=False)
    print("\n✅ Results saved to 'prime_candidates.csv'.")

if __name__ == "__main__":
    find_winner()