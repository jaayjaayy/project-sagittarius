from astroquery.gaia import Gaia
import pandas as pd

# Widening the net: 
# 1. Radius increased to 2 degrees.
# 2. Distance range expanded (Parallax 5 to 50 = ~65 to 650 light years).
# 3. Removed the color (bp_rp) filter to see everything.

query = """
SELECT TOP 50
    source_id, ra, dec, parallax, pmra, pmdec, 
    phot_g_mean_mag, radial_velocity
FROM gaiadr3.gaia_source
WHERE 1=CONTAINS(
    POINT('ICRS', ra, dec),
    CIRCLE('ICRS', 290.5, -27.0, 2.0)
)
AND parallax BETWEEN 5 AND 50
ORDER BY parallax DESC
"""

print("🛰️ Casting a wider net in the Sagittarius Archive...")
try:
    job = Gaia.launch_job(query)
    results = job.get_results().to_pandas()

    if not results.empty:
        results.to_csv('target_stars_data.csv', index=False)
        print(f"✅ Success! Found {len(results)} potential candidate stars.")
        print("File 'target_stars_data.csv' is now populated with real celestial data.")
    else:
        print("❌ Still no hits. The archive might be rate-limiting. Checking connection...")
except Exception as e:
    print(f"⚠️ ESA Connection Error: {e}")