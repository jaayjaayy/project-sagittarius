from astroquery.gaia import Gaia
import pandas as pd

# Using a real test coordinate near the Wow! source for a "Ping"
query = "SELECT TOP 5 source_id, ra, dec, parallax FROM gaiadr3.gaia_source WHERE parallax > 10"

print("Pinging ESA Gaia Archive...")
job = Gaia.launch_job(query)
results = job.get_results().to_pandas()

if not results.empty:
    results.to_csv('gaia_test_data.csv', index=False)
    print("Signal received! 'gaia_test_data.csv' created.")
else:
    print("Connection made, but no data returned.")