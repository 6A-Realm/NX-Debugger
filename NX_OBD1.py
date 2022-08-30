from pandas import read_html
from numpy import nan
import json

# Target website
url = read_html("https://switchbrew.org/wiki/Error_codes")

# Define and format tables
modules = url[1]
codes = url[2]
codes = codes.fillna(nan).replace([nan], [None])

# Convert "Name" column to custom format 
combine = json.loads(modules.set_index("Value")["Name"].to_json())
out = {k: {"name": v} for k, v in combine.items()}

# Add to out
for x in range(codes.shape[0]):
    location = codes.iloc[x]
    module = str(location["Module"])
    desc = str(location["Description"])
    notes = location["Notes"]
    out[module].update([(desc, notes)])

# Dumping json
with open("api.json", "w") as outfile:
    parsed = json.dumps(out, indent = 4)
    outfile.write(parsed)
